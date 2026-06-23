from services.admin_service import admin
from services.base_service import base
from .driver_cli import DriverCLI

class AdminCLI(admin,DriverCLI):

    def admin_register(self):
        name = input("\nEnter your Name : ")
        mobile = int(input("Enter mobile number : "))
        email = input("Enter your Email : ")
        password = input("Enter your password : ")
        c_pass = input("Conform your password : ")
        i_key = int(input("Enter key : "))
        key = 2580

        id = max(self.admins, default = 0) + 1

        if password == c_pass and key == i_key:
            self.add_admin(id,name,mobile,email,password)
        else:
            print("Password mismatch or Key mismatch.")


    def admin_login(self):
        email = input("\nEnter your email : ")
        password = input("Enter your password : ")

        admin = self.login_admin(email,password)

        if admin:
            while True:
                print("\n ------- admin Module -------\n")
                print("1. View Customers\n2. View Drivers\n3. View Rides\n4. Add Driver\n5. Remove Driver\n6. Logout")
                ch = base.get_choice(1,7)

                if ch == 1:
                    self.view_customers()

                elif ch == 2:
                    self.view_drivers()

                elif ch == 3:
                    self.view_rides()

                elif ch == 4:
                    self.driver_register()

                elif ch == 5:
                    self.remove_driver()

                elif ch == 6:
                    break

                else:
                    print("Please enter valid choice")

        else:
            print("Failed to login.")