from services.driver_service import driver
from services.base_service import base

class DriverCLI(driver):

    def driver_register(self):
        name = input("\nEnter your Name : ")
        mobile = int(input("Enter mobile number : "))

        print("Vehicle Type :\n1. Mini Sedan\n2. Sedan\n3. SUV\n4. Auto")
        num = base.get_choice(1,4)
        if num == 1:
            v_type = "Mini Sedan"
        elif num == 2:
            v_type = "Sedan"
        elif num == 3:
            v_type = "SUV"
        elif num == 4:
            v_type = "Auto"
        else:
            print("Please enter valid option.")
            return

        v_num = input("Enter Vehicle Number : ")
        email = input("Enter your Email : ")
        password = input("Enter your password : ")
        c_pass = input("Conform your password : ")

        id = max(self.drivers, default = 0) + 1
        l_num = "LICENSE " + str(max(self.drivers, default = 0) + 1)

        if password == c_pass:
            self.add_driver(id,name,mobile,email,password,l_num,v_type,v_num)
        else:
            print("Password mismatch.")


    def driver_login(self):
        email = input("\nEnter your email : ")
        password = input("Enter your password : ")

        driver = self.login_driver(email,password)

        if driver:
            while True:
                print("\n ------- Driver Module -------\n")
                print("1. Go Online\n2. Go Offline\n3. View Pending Rides\n4. Accept Ride\n5. Complete Ride\n6. Profile\n7. Logout")
                ch = base.get_choice(1,8)

                if ch == 1:
                    self.go_online(driver)

                elif ch == 2:
                    self.go_offline(driver)

                elif ch == 3:
                    self.view_pending_rides(driver)

                elif ch == 4:
                    self.accept_rides(driver)

                elif ch == 5:
                    self.complete_rides(driver)

                elif ch == 6:
                    c = self.edit_profile(driver)
                    if c == 0:
                        break

                elif ch == 7:
                    break

                else:
                    print("Please enter valid choice.")

        else:
            print("Failed to login.")