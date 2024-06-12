#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.station import Station

def seed_database():
    Station.drop_table()
    Station.create_table()

    # Create seed data
    station_1 = Station.create("Westlands")
    station_2 = Station.create("The Mall Westlands")
    station_3 = Station.create("Museum Hill Roundabout")
    station_4 = Station.create("CBD")
    station_5 = Station.create("Haille Selassie")
    station_6 = Station.create("Bunyala")
    station_7 = Station.create("Capital Center")
    station_8 = Station.create("Ole Sereni")
    station_9 = Station.create("Eastern Bypass")
    station_10 = Station.create("JKIA")
    station_11 = Station.create("SGR")
    station_12 = Station.create("Syokimau")


seed_database()
print("Seeded database")
