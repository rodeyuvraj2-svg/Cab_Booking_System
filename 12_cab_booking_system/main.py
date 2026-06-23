from cli.customer_cli import CustomerCLI
from cli.driver_cli import DriverCLI
from cli.admin_cli import AdminCLI

cc = CustomerCLI()
dd = DriverCLI()
aa = AdminCLI()

while True:
    print("\n------- Cab Booking System -------\n")

    try:
        ch = int(input("1. Register\n2. Login\n3. Exit\nEnter your choice : "))
    except ValueError:
        print("Enter only intergers.")


    if ch == 1:
        print(" ----- Registration -----")
        try:
            c = int(input("\n1. Admin\n2. Customer\n3. Driver\nEnter your choice : "))
        except ValueError:
            print("Enter only intergers.")
        
        if c == 1:
            aa.admin_register()

        elif c == 2:
            cc.customer_register()

        elif c == 3:
            dd.driver_register()

        else:
            print("Enter valid choice.")


    elif ch == 2:
        print(" ----- Login -----")
        try:
            c = int(input("\n1. Admin\n2. Customer\n3. Driver\nEnter your choice : "))
        except ValueError:
            print("Enter only intergers.")
        
        if c == 1:
            aa.admin_login()

        elif c == 2:
            cc.customer_login()

        elif c == 3:
            dd.driver_login()

        else:
            print("Enter valid choice.")


    elif ch == 3:
        print("\nThank you for visiting !!!")
        break

    else:
        print("Enter valid choice.")