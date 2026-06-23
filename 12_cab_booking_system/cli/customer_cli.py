from services.customer_service import customer
from services.base_service import base

class CustomerCLI(customer):

    def customer_register(self):
        name = input("\nEnter your Name : ")
        mobile = int(input("Enter mobile number : "))
        email = input("Enter your Email : ")
        password = input("Enter your password : ")
        c_pass = input("Conform your password : ")

        id = max(self.customers, default = 0) + 1

        if password == c_pass:
            self.add_customer(id,name,mobile,email,password)
        else:
            print("Password mismatch.")


    def customer_login(self):
        email = input("\nEnter your email : ")
        password = input("Enter your password : ")

        customer = self.login_customer(email,password)

        if customer:
            while True:
                print("\n ------- Customer Module -------\n")
                print("1. Book Ride\n2. My Rides\n3. Ride History\n4. Favorite Locations\n5. Profile\n6. Logout")
                ch = base.get_choice(1,6)

                if ch == 1:
                    self.book_ride(customer)

                elif ch == 2:
                    self.my_rides(customer)

                elif ch == 3:
                    self.ride_history(customer)

                elif ch == 4:
                    self.favourite_locations(customer)

                elif ch == 5:
                    c = self.edit_profile(customer)
                    if c == 0:
                        break
                elif ch == 6:
                    break

                else:
                    print("Please enter valid choice.")

        else:
            print("Failed to login.")