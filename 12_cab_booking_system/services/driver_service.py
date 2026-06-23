from models.driver_model import Driver
from .base_service import base

class driver(base):
    def __init__(self):
        super().__init__()


    def add_driver(self,id,name,mobile,email,password,l_num,v_type,v_num):
        if email in self.drivers:
            print("Same email account exists.")
        else:
            new_driver = Driver(id,name,mobile,email,password,l_num,v_type,v_num) 
            self.drivers[id] = new_driver
            print("Account created successfully.")
            self.save_data_drivers()


    def login_driver(self,email,password):
        for driver in self.drivers.values():
            if email == driver.email and password == driver.password:
                return driver


    def go_offline(self,driver):
        driver.mode = "offline"
        self.drivers[driver.id] = driver
        print("Driver is offline. Thank you !!")
        self.save_data_drivers()

    
    def go_online(self,driver):
        driver.mode = "online"
        self.drivers[driver.id] = driver
        print("Driver is online.")
        self.save_data_drivers()

    
    def view_pending_rides(self,driver):
        self.load_data_rides()
        print("\n ------- All Pending Rides -------")
        found = False
        for ride in self.rides.values():
            if ride.status == "Pending" and ride.v_type == driver.v_type:
                print(f"\nRide Id : {ride.id}\nPick point : {ride.pickup}\nDrop Point : {ride.drop}")
                found = True
        if not found:
            print("No Pending rides.")
    

    def accept_rides(self,driver):
        self.view_pending_rides(driver)
        ch = int(input("\nEnter the ID of the ride to accept : "))
        for i,ride in self.rides.items():
            if ride.id == ch:
                break
        ride.status = "Accepted"
        ride.driver = driver.name
        self.rides[ride.id] = ride
        print("Ride Accepted.")
        self.save_data_rides()

    
    def complete_rides(self,driver):
        complete = False
        for ride in self.rides.values():
            if ride.status == "Accepted" and ride.driver == driver.name:
                print(f"\nRide Id : {ride.id}\nPick point : {ride.pickup}\nDrop Point : {ride.drop}")
                r = ride
                complete = True
                break
        if complete:
            ch = int(input("\nRide completed ?\n1. Yes\n2. No\n Enter your choice : "))
            if ch == 1:
                r.status = "Completed"
                self.rides[r.id] = r
                print("Ride Completed.")
                self.save_data_rides()
        else:
            print("No ongoing ride.")

    
    def edit_profile(self,driver):
        while True:
            print("\n  ------- Profile ------- ")
            print(f"\nDriver ID : {driver.id}\nName : {driver.name}\nMobile : {driver.mobile}\nEmail : {driver.email}")
        
            ch = int(input("\n1. Edit Name\n2. Edit Mobile\n3. Change Password\n4. Delete Account\n5. Exit Profile\nEnter your choice : "))

            if ch == 1:
                name = input("Enter new name : ")
                driver.name = name
                self.drivers[driver.id] = driver
                print("Name Updated.")
                self.save_data_drivers()

            elif ch == 2:
                mobile = int(input("Enter new mobile number : "))
                driver.mobile = mobile
                self.drivers[driver.id] = driver
                print("Mobile Updated.")
                self.save_data_drivers()

            elif ch == 3:
                password = input("Enter new password : ")
                driver.password = password
                self.drivers[driver.id] = driver
                print("Password Updated.")
                self.save_data_drivers()

            elif ch == 4:
                self.drivers.pop(driver.id)
                print("Account Deleted.")
                self.save_data_drivers()
                return 0
            
            elif ch == 5:
                break
            
            else:
                print("Enter only integers between 1-5.")
                continue
        