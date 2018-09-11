from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm.session import make_transient

from carbonvis.models.paths import Path, Point, Vehicle
from carbonvis.resources.constants import VEHICLE_TYPE_CO2

import transaction
import json

@view_config(route_name='home', renderer='../templates/map.jinja2')
def home(request):
    try:
        if 'vehicle_id' in request.GET:
            vehicle_id = request.GET['vehicle_id']
        else:
            vehicle_id = request.dbsession.query(Vehicle).first().id
        query = request.dbsession.query(Vehicle).filter(Vehicle.id==vehicle_id)
        if query.count() > 0:
            vehicle = query.one()
            paths_to_show = []
            for p in vehicle.paths:
                if p.length > 0 and not p.archived:
                    paths_to_show.append(p)
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)

    return {
        'paths': paths_to_show,
        'project': 'carbonvis',
        'vehicle_id': vehicle_id,
        'vehicles': request.dbsession.query(Vehicle).all(),
        'emissions_list': VEHICLE_TYPE_CO2
    }

def redirect_home(request):
    url = '/'
    if 'vehicle_id' in request.GET:
        url = '/?vehicle_id={}'.format(request.GET['vehicle_id'])
    return HTTPFound(location=url)

@view_config(route_name='merge_paths', renderer='../templates/map.jinja2')
def merge_paths(request):
    try:
        if 'path_ids' not in request.GET or not request.GET['path_ids']:
            return redirect_home(request)

        path_ids = request.GET['path_ids'].split(',')
        if len(path_ids) < 2:
            return redirect_home(request)

        paths = request.dbsession.query(Path).filter(Path.id.in_(path_ids)).all()

        if 'vehicle_id' in request.GET:
            vehicle_id = request.GET['vehicle_id']
        else:
            vehicle_id = paths[0].vehicle_id

        vehicle_item = request.dbsession.query(Vehicle).get(vehicle_id)

        new_path_item = Path()

        with transaction.manager:
            for path in paths:
                for p in path.points:
                    request.dbsession.expunge(p)  # expunge the object from session
                    make_transient(p)  # http://docs.sqlalchemy.org/en/rel_1_1/orm/session_api.html#sqlalchemy.orm.session.make_transient
                    p.id = None
                    request.dbsession.add(p)
                    new_path_item.points.append(p)
                path.archived = True
            request.dbsession.add(new_path_item)
            vehicle_item.paths.append(new_path_item)

    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)

    return redirect_home(request)

@view_config(route_name='save_points', renderer='json')
def save_points(request):
    try:
        if 'points_json' not in request.POST or not request.POST['points_json']:
            return {}
        points_json = request.POST['points_json']
        points = json.loads(points_json)
        [p['id'] for p in points]
        points_dict = {}
        for p in points:
            points_dict[p['id']] = p

        with transaction.manager:
            point_items = request.dbsession.query(Point).filter(Point.id.in_(points_dict.keys())).all()

            for p in point_items:
                p.latitude = points_dict[p.id]['lat']
                p.longitude = points_dict[p.id]['long']

            json_response = {
                'km': p.path.km,
                'footprint': p.path.footprint
            }

    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)

    return json_response




db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_carbonvis_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
