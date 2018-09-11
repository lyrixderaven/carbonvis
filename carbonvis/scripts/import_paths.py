import os
import sys
import transaction
import re

from datetime import datetime

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from carbonvis.models.meta import Base
from carbonvis.models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from carbonvis.models import Path
from carbonvis.models import Point
from carbonvis.models import Vehicle

from collections import OrderedDict

from progress.bar import Bar

import csv

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> <csvfile> <vehicle_id> [var=value]\n'
          '(example: "%s development.ini foo.csv 1")' % (cmd, cmd))
    sys.exit(1)


EVENT_TYPES_WHITELIST = [
    'Resting GPS Report',
    'Idle Time Report',
    'Ignition On',
    'Ignition Off',
    'Active GPS Report'
]

def main(argv=sys.argv):
    if len(argv) < 3:
        usage(argv)
    config_uri = argv[1]
    csvpath = argv[2]
    vehicle_id = argv[3]
    options = parse_vars(argv[4:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    points = []

    with open(csvpath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=u',', quotechar=u'"')
        for row in reader:
            if 'Date Received' in row[0]:
                continue

            ts = datetime.strptime(row[0], '%m/%d/%Y %I:%M:%S %p')
            event = row[1]

            if event not in EVENT_TYPES_WHITELIST:
                continue


            info = row[2]
            if 'Call Reason = ' not in info:
                continue

            info = info[info.index('Call Reason = '):]
            try:
                call_reason = re.search('Call Reason = .*?,', info)
                if call_reason is not None:
                    call_reason = call_reason.group(0).replace("Call Reason = ","")[:-1]
                location = re.search('Location = .*?\)', info)
                if location is not None:
                    location = location.group(0)

                    adr = re.search('= .*?\(', location)
                    if adr is not None:
                        adr = adr.group(0)[2:-2]

                    latlong = re.search('\((?P<lat>.*),(?P<long>.*)\)', location)
                    if latlong is not None:
                        latitude = latlong.group('lat').strip()
                        longitude = latlong.group('long').strip()
                    else:
                        latitude = None
                        longitude = None
                else:
                    adr = None
                    gps_position = re.search('GPS Position = .*?,', info)
                    if gps_position is not None:
                        gps_position = gps_position.group(0).replace('GPS Position =','')
                        gps_position = gps_position.replace('</font>','')
                        gps_position = gps_position[:-1].strip()
                        latlong = re.search('(?P<lat>.*); (?P<long>.*)', gps_position)
                        if latlong is not None:
                            latitude = latlong.group('lat').strip()
                            longitude = latlong.group('long').strip()
                        else:
                            latitude = None
                            longitude = None

                speed = re.search('Speed = .*?,', info)
                if speed is not None:
                    speed = speed.group(0)
                    speed = int(speed.replace('Speed = ','')[:-5])
                satellites = re.search('Satellites = .*?,', info)
                if satellites is not None:
                    satellites = satellites.group(0)
                    satellites = int(satellites.replace('Satellites = ','')[:-1])
                heading = re.search('Heading = .*?,', info)
                if heading is not None:
                    heading = heading.group(0)
                    heading = heading.replace('Heading = ','')[:-1]
                signal_strength = re.search('Signal Strength = .*?%', info)
                if signal_strength is not None:
                    signal_strength = signal_strength.group(0)
                    signal_strength = float((
                        signal_strength.replace('Signal Strength = ','')[:-1])\
                    .strip('%')) / 100
                ignitionstate = re.search('IgnitionState = .*', info)
                if ignitionstate is not None:
                    ignitionstate = ignitionstate.group(0)
                    ignitionstate = ignitionstate.replace('IgnitionState = ','')

                pt = {
                    'call_reason': call_reason,
                    'location': location,
                    'adr': adr,
                    'latitude': latitude,
                    'longitude': longitude,
                    'speed': speed,
                    'satellites': satellites,
                    'heading': heading,
                    'signal_strength': signal_strength,
                    'ignitionstate': ignitionstate,
                    'recorded': ts
                }
            except:
                import ipdb; ipdb.set_trace()



            points.append(pt)

    print('Scanned {} points'.format(len(points)))

    paths = []
    current_path = None

    sort_points = sorted(points, key=lambda p: p['recorded'])
    for i in range(len(sort_points)):
        p = sort_points[i]
        call_reason = p['call_reason']
        if call_reason == 'Ignition On':
            current_path = []
        if call_reason == 'Ignition Off':
            if current_path:
                paths.append(current_path)
            current_path = None
        if call_reason == 'Active GPS Report' and current_path is not None:
            if i > 0:
                p_prev = sort_points[i-1]
                if p['latitude'] == p_prev['latitude'] and p['longitude'] == p_prev['longitude']:
                    continue
            current_path.append(p)

    reduced_points = 0
    for path in paths:
        reduced_points += len(path)
    print('Reduced to {} points'.format(reduced_points))

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

        if dbsession.query(Vehicle).filter(Vehicle.id==vehicle_id).count() == 0:
            vehicle_item = Vehicle(id=vehicle_id)
            dbsession.add(vehicle_item)
        else:
            vehicle_item = dbsession.query(Vehicle).get(vehicle_id)

        for path in paths:
            path_item = Path()

            bar = Bar('Processing', max=len(path), suffix='[%(index)d/%(max)d] %(percent).1f%% - %(eta_td)s')
            for pt in path:
                point_item = Point(
                    event=pt['call_reason'],
                    location=pt['adr'],
                    latitude=pt['latitude'],
                    longitude=pt['longitude'],
                    speed=pt['speed'],
                    satellites=pt['satellites'],
                    heading=pt['heading'],
                    signal_strength=pt['signal_strength'],
                    ignitionstate=pt['ignitionstate'],
                    recorded=pt['recorded']
                    )
                dbsession.add(point_item)
                path_item.points.append(point_item)
                bar.next()
            bar.finish()
            dbsession.add(path_item)
            vehicle_item.paths.append(path_item)



