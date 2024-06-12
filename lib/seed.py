from models.__init__ import CONN, CURSOR
from models.station import Station
from models.vehicle import Vehicle

def seed_database():
    Vehicle.delete_table()
    Vehicle.create_table()

    # Create seed data
    vehicle_1 = Vehicle.create("KCA", "Alex" ,"0727222222")
    vehicle_2 = Vehicle.create("KDA", "Dan", "0727222244")
    vehicle_3 = Vehicle.create("KCK", "Dor", "0754555566")
    vehicle_4 = Vehicle.create("KCM", "Shee", "0722226666")
    vehicle_5 = Vehicle.create("HKDP", "Bree", "0782888888") 

seed_database()
print("Seeded database")