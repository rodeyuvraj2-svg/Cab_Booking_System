from models.customer_model import Customer
from models.ride_model import Ride
from .base_service import base
from models.location_model import Location
from services import distance_service
import math

class customer(base):
    def __init__(self):
        super().__init__()


    def add_customer(self,id,name,mobile,email,password):
        if email in self.customers:
            print("Same email account exists.")
        else:
            new_customer = Customer(id,name,mobile,email,password) 
            self.customers[id] = new_customer
            print("Account created successfully.")
            self.save_data_customers()


    def login_customer(self,email,password):
        for customer in self.customers.values():
            if email == customer.email and password == customer.password:
                return customer


    def book_ride(self,customer):
        if self.drivers:
            print("\n---- Book A Ride ----")
            while True: 
                c = int(input("Select pickup from Favourite\n1. Yes\n2. No"))
                if c == 1:
                    loc = self.view_locations(customer)
                    if loc:
                        pickup = loc.place
                        break
                    else:
                        print("No Favourite Locations.")
                elif c == 2:
                    pickup = input("Enter pickup point : ")
                    break
                else:
                    print("Please enter Integer 1 or 2.")
                    continue
                
            while True: 
                c = int(input("Select Drop point from Favourite\n1. Yes\n2. No"))
                if c == 1:
                    loc = self.view_locations(customer)
                    if loc:
                        drop = loc.place
                        break
                    else:
                        print("No Favourite Locations.")
                elif c == 2:
                    drop = input("Enter drop point : ")
                    break
                else:
                    print("Please enter Integer 1 or 2.")
                    continue

                
            km = math.ceil(distance_service.get_distance(pickup,drop))
            customer_id = customer.id

            max_key = max(self.rides, default=0)
            if max_key == 0:
                id = 1000 + max_key + 1
            else:
                id = max_key + 1
            status = "Pending"

            v_type = None

            while True:
                try:
                    num = int(input("\nVehicle Type :\n1. Mini Sedan\n2. Sedan\n3. SUV\n4. Auto\n5. Cancel booking\nEnter your choice : "))

                    if num == 1:
                        v_type = "Mini Sedan"
                        fare = km * 15
                        driver = self.available_driver(v_type)
                        if driver:
                            print("\nFare : ",fare)
                            confirm = int(input("\nConfirm ride ?\n\n1. Yes\n2. No\nEnter your choice : "))
                            if confirm == 1:
                                break
                            elif confirm == 2:
                                continue
                            else:
                                print("Enter only integers (1 or 2).")
                        else:
                            print("Sorry driver Not available.")
                            continue

                    elif num == 2:
                        v_type = "Sedan"
                        fare = km * 17
                        driver = self.available_driver(v_type)
                        if driver:
                            print("\nFare : ",fare)
                            confirm = int(input("\nConfirm ride ?\n\n1. Yes\n2. No\nEnter your choice : "))
                            if confirm == 1:
                                break
                            elif confirm == 2:
                                continue
                            else:
                                print("Enter only integers (1 or 2).")
                        else:
                            print("Sorry driver Not available.")
                            continue

                    elif num == 3:
                        v_type = "SUV"
                        fare = km * 20 
                        driver = self.available_driver(v_type)
                        if driver:
                            print("\nFare : ",fare)
                            confirm = int(input("\nConfirm ride ?\n\n1. Yes\n2. No\nEnter your choice : "))
                            if confirm == 1:
                                break
                            elif confirm == 2:
                                continue
                            else:
                                print("Enter only integers (1 or 2).")
                        else:
                            print("Sorry driver Not available.")
                            continue

                    elif num == 4:
                        v_type = "Auto"
                        fare = km * 10
                        driver = self.available_driver(v_type)
                        if driver:
                            print("\nFare : ",fare)
                            confirm = int(input("\nConfirm ride ?\n\n1. Yes\n2. No\nEnter your choice : "))
                            if confirm == 1:
                                break
                            elif confirm == 2:
                                continue
                            else:
                                print("Enter only integers (1 or 2).")
                        else:
                            print("Sorry driver Not available.")
                            continue
                    
                    elif num == 5:
                        print("Failed to book a ride")
                        break
                    
                    else:
                        print("Please enter values between 1 and 4.")
                        continue

                    break
                except ValueError:
                    print("Please enter only integers.")

            
            new_ride = Ride(id,pickup,drop,customer_id,status,v_type,fare)
            new_ride.distance = km
            self.rides[new_ride.id] = new_ride
            print("Successfully booked a ride.")
                
            self.save_data_rides()

        else:
            print("Driver is not available.")


    def available_driver(self,v_type):
        self.load_data_drivers()
        for driver in self.drivers.values():
            if v_type == driver.v_type and driver.mode == "online":
                return driver
        return None


# "email": "yuvi@gmail.com",
# "password": "Yuvii"


    def my_rides(self,customer):
        found = True
        for ride in self.rides.values():
            if customer.id == ride.customers_id:
                if ride.status == "Pending" or ride.status =="Accepted":
                    print(" ------- My Ride -------")
                    print(f"\nRide ID : {ride.id}\nPickup : {ride.pickup}\nDrop   : {ride.drop}\nFare : {ride.fair}\nStatus : {ride.status}\n\nDriver : {ride.driver}")
                    found = False
        if found:
            print("No rides.")

    
    def ride_history(self,customer):
        complete = False
        print(" ------- Ride History -------")
        for ride in self.rides.values():
            if customer.id == ride.customers_id:
                if ride.status == "Completed":
                    print(f"\nRide ID : {ride.id}\nPickup : {ride.pickup}\nDrop   : {ride.drop}\nStatus : {ride.status}")
                    complete =True
        
        if complete == False:
            print("No rides Completed.")

    
    def favourite_locations(self,customer):
        while True:
            print("\n ------- Favourite Locations -------")
            ch = int(input("\n1. Add Location\n2. View Locations\n3. Delete Location\n4. Exit\nEnter your choice : "))

            if ch == 1:
                loc = input("\nEnter the Location : ")
                id = max(self.locations, default = 0) + 1
                location = Location(id,loc,customer.id)
                self.locations[location.id] = location
                print("Location added successfully")
                self.save_data_locations()

            elif ch == 2:
                if self.locations:
                    print(" ------- Locations -------")
                    for loc in self.locations.values():
                        if customer.id == loc.c_id:
                            print(f"{loc.id}. {loc.place}")
                else:
                    print("No Favourite Locations.")

            elif ch == 3:
                if self.locations:
                    print(" ------- Locations -------")
                    for loc in self.locations.values():
                        if customer.id == loc.c_id:
                            print(f"{loc.id}. {loc.place}")

                    c = int(input("\nEnter the number of the location to delete : "))
                    
                    self.locations.pop(c)
                    print("Location deleted.")     
                    self.save_data_locations()
                else:
                    print("No locations.")           


            elif ch == 4:
                break

            else:
                print("Enter Valid integers between 1-4.")
                continue



    def edit_profile(self,customer):
        while True:
            print("\n  ------- Profile ------- ")
            print(f"\nCustomer ID : {customer.id}\nName : {customer.name}\nMobile : {customer.mobile}\nEmail : {customer.email}")
        
            ch = int(input("\n1. Edit Name\n2. Edit Mobile\n3. Change Password\n4. Delete Account\n5. Exit Profile\nEnter your choice : "))

            if ch == 1:
                name = input("Enter new name : ")
                customer.name = name
                self.customers[customer.id] = customer
                print("Name Updated.")
                self.save_data_customers()

            elif ch == 2:
                mobile = int(input("Enter new mobile number : "))
                customer.mobile = mobile
                self.customers[customer.id] = customer
                print("Mobile Updated.")
                self.save_data_customers()

            elif ch == 3:
                password = input("Enter new password : ")
                customer.password = password
                self.customers[customer.id] = customer
                print("Password Updated.")
                self.save_data_customers()

            elif ch == 4:
                self.customers.pop(customer.id)
                print("Account Deleted.")
                self.save_data_customers()
                return 0
            
            elif ch == 5:
                break
            
            else:
                print("Enter only integers between 1-5.")
                continue
    

    def view_locations(self,customer):
        found = False
        if self.locations:
            print(" ------- Locations -------")
            for loc in self.locations.values():
                if customer.id == loc.c_id:
                    print(f"{loc.id}. {loc.place}")
                    found = True
            if found:
                c = int(input("Enter Location Number : "))
                return self.locations[c]
        else:
            print("No Favourite Locations.")