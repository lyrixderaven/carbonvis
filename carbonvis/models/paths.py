from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    Boolean,
    Float,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .meta import Base
from geopy.distance import geodesic
from carbonvis.resources.constants import *

class Point(Base):
    __tablename__ = 'points'
    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    recorded = Column(DateTime)
    event = Column(Text)
    location = Column(Text)
    speed = Column(Integer)
    satellites = Column(Integer)
    heading = Column(Text)
    signal_strength = Column(Float)
    ignitionstate = Column(Text)
    path_id = Column(Integer(), ForeignKey('paths.id'))
    path = relationship("Path", back_populates="points")

    @property
    def js_string(self):
        return "new Point({},{},{},\'{}\')".format(
            self.id,
            self.latitude,
            self.longitude,
            self.recorded.strftime('%d. %m. %Y, %H:%M:%S'))

    @property
    def latlong(self):
        return (self.latitude,self.longitude)

class Path(Base):
    __tablename__ = 'paths'
    id = Column(Integer, primary_key=True)
    points = relationship("Point", cascade="all, delete-orphan")
    vehicle_id = Column(Integer(), ForeignKey('vehicles.id'))
    archived = Column(Boolean, default=False)

    def js_pointlist(self):
        points_latlong = [p.js_string for p in sorted(self.points, key=lambda p: p.recorded)]
        list_string = "[\n{}\n]".format(u',\n'.join(points_latlong))
        return list_string

    @property
    def length(self):
        length = 0
        for (index, point) in enumerate(self.points):
            if index+1 < len(self.points):
                length += geodesic(point.latlong,self.points[index+1].latlong).meters
        return length

    @property
    def km(self):
        return round(self.length / 1000, 2)

    @property
    def start_time(self):
        return min([p.recorded for p in self.points])

    @property
    def end_time(self):
        return max([p.recorded for p in self.points])

    @property
    def duration(self):
        duration = self.end_time - self.start_time
        return str(duration)

    @property
    def footprint(self, vehicle='ucarver'):
        if vehicle in VEHICLE_TYPE_CO2:
            return round(self.km * VEHICLE_TYPE_CO2[vehicle]['emissions'],3)
        else:
            return round(self.km * VEHICLE_TYPE_CO2['ucarver']['emissions'],3)

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    paths = relationship("Path", cascade="all, delete-orphan")

    @property
    def num_trips(self):
        return len(self.paths)

    @property
    def km_driven(self):
        km = 0
        for path in self.paths:
            km += path.km
        return round(km, 2)


Index('path_index', Path.id, unique=True, mysql_length=255)
Index('vehicle_index', Vehicle.id, unique=True, mysql_length=255)
