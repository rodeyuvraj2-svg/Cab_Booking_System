from models.admin_model import Admin
from .base_service import base

class admin(base):
    def __init__(self):
        super().__init__()


    def add_admin(self,id,name,mobile,email,password):
        if email in self.admins:
            print("Same email account exists.")
        else:
            new_admin = Admin(id,name,mobile,email,password) 
            self.admins[id] = new_admin
            print("Account created successfully.")
            self.save_data_admins()


    def login_admin(self,email,password):
        for admin in self.admins.values():
            if email == admin.email and password == admin.password:
                return admin
            

    def view_customers(self):
        self.load_data_customers()
        if self.customers:
            print("\n ------- All customers -------")
            for customer in self.customers.values():
                print(f"\nCustomer ID : {customer.id}\nName : {customer.name}\nMobile : {customer.mobile}\nEmail : {customer.email}")
        else:
            print("\nNo customers.")


    def view_drivers(self):
        self.load_data_drivers()
        if self.drivers:
            print("\n ------- All drivers -------")
            for driver in self.drivers.values():
                print(f"\nDriver ID : {driver.id}\nName : {driver.name}\nMobile : {driver.mobile}\nEmail : {driver.email}")
        else:
            print("\nNo drivers.")
    

    def view_rides(self):
        self.load_data_rides()
        if self.rides:
            print("\n ------- All rides -------")
            for ride in self.rides.values():
                print(f"\nRide ID : {ride.id}\nPickup : {ride.pickup}\nDrop : {ride.drop}\nStatus : {ride.status}")
        else:
            print("\nNo rides.")


    def remove_driver(self):
        self.view_drivers()
        c = int(input("Enter drivers ID to delete : "))

        self.drivers.pop(c)
        print("Account Deleted.")
        self.save_data_drivers()