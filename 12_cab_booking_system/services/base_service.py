from models.admin_model import Admin
from models.customer_model import Customer
from models.driver_model import Driver
from models.ride_model import Ride
from models.location_model import Location
import json

class base:
    def __init__(self):
        self.admins = {}
        self.customers = {}
        self.drivers = {}
        self.rides = {}
        self.locations = {}

        self.load_data_admins()
        self.load_data_customers()
        self.load_data_drivers()
        self.load_data_rides()
        self.load_data_favourite_locations()
                


    #  ----------- Admins --------------

    def load_data_admins(self):
        with open("storage\m_admin.json", "r") as file:
            data = json.load(file)

            for cus in data:
                new_admin = Admin(
                    cus["id"],
                    cus["name"],
                    cus["mobile"],
                    cus["email"],
                    cus["password"]
                )
            
                self.admins[new_admin.id] = new_admin

    def save_data_admins(self):
        admins = []

        for admin in self.admins.values():
            admins.append(admin.struct())

        with open("storage\m_admin.json", "w") as file:
            json.dump(admins,file,indent = 4)

    

    #  ----------- Customers --------------

    def load_data_customers(self):
        with open("storage\customer.json", "r") as file:
            data = json.load(file)

            for cus in data:
                new_customer = Customer(
                    cus["id"],
                    cus["name"],
                    cus["mobile"],
                    cus["email"],
                    cus["password"]
                )
            
                self.customers[new_customer.id] = new_customer

    def save_data_customers(self):
        customers = []

        for customer in self.customers.values():
            customers.append(customer.struct())

        with open("storage\customer.json", "w") as file:
            json.dump(customers,file,indent = 4)



    #  ----------- Drivers --------------

    def load_data_drivers(self):
        with open("storage\driver.json", "r") as file:
            data = json.load(file)

            for dir in data:
                new_driver = Driver(
                    dir["id"],
                    dir["name"],
                    dir["mobile"],
                    dir["email"],
                    dir["password"],
                    dir["l_num"],
                    dir["v_type"],
                    dir["v_num"]
                )
                
                new_driver.mode = dir["mode"]
                self.drivers[new_driver.id] = new_driver

    
    def save_data_drivers(self):
        drivers = []

        for driver in self.drivers.values():
            drivers.append(driver.struct())

        with open("storage\driver.json", "w") as file:
            json.dump(drivers,file,indent = 4)



    #  ----------- Rides --------------

    def load_data_rides(self):
        with open("storage\m_ride.json", "r") as file:
            data = json.load(file)

            for rr in data:
                new_ride = Ride(
                    rr["id"],
                    rr["pickup"],
                    rr["drop"],
                    rr["customers_id"],
                    rr["status"],
                    rr["v_type"],
                    rr["fair"]
                )

                new_ride.distance = rr["distance"]
                new_ride.driver = rr["driver"]
                self.rides[new_ride.id] = new_ride

    def save_data_rides(self):
        rides = []

        for ride in self.rides.values():
            rides.append(ride.struct())

        with open("storage\m_ride.json", "w") as file:
            json.dump(rides,file,indent = 4)



    #  ----------- Favourite Locations --------------

    def load_data_favourite_locations(self):
        with open("storage\location.json", "r") as file:
            data = json.load(file)

            for cus in data:
                new_location = Location(
                    cus["id"],
                    cus["place"],
                    cus["c_id"]
                )
            
                self.locations[new_location.id] = new_location

    def save_data_locations(self):
        loc = []

        for location in self.locations.values():
            loc.append(location.struct())

        with open("storage\location.json", "w") as file:
            json.dump(loc,file,indent = 4)


    
    def get_choice(start,end):
        try:
            choice = int(input("Enter your choice : "))

            if choice >= start and choice <= end:
                return choice

            print(f"Please Enter a vaild option in between {start} and {end}")

        except ValueError:
            print("Only integers are allowed.")