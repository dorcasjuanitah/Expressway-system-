from models.__init__ import CONN, CURSOR
from models.station import Station
from models.vehicle import Vehicle

def seed_database():
    # Vehicle.delete_table()
    # Vehicle.create_table()
    Station.drop_table()
    Station.create_table()

    # Create seed data
    # vehicle_1 = Vehicle.create("KCA", "Alex" ,"0727222222")
    # vehicle_2 = Vehicle.create("KDA", "Dan", "0727222244")
    # vehicle_3 = Vehicle.create("KCK", "Dor", "0754555566")
    # vehicle_4 = Vehicle.create("KCM", "Shee", "0722226666")
    # vehicle_5 = Vehicle.create("HKDP", "Bree", "0782888888") 

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
