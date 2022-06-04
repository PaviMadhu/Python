import admin as aa
from user import User

uhh = User(str, str, str, str, str)
print("HELLO THERE ! Welcome to BREAD AND BAKES")
inp = int(input("Where You want to login select 1.Admin and 2.User and 3.Exit"))
if inp == 1:
    Username = input("Enter the username of admin: ")
    Password = input("Enter the password of admin: ")
    if aa.admin_keys[Username] == Password:
        print("*****You're successfully logged inn*****")
        admin_crawler = True
        while admin_crawler:
            adm_choice = int(input("Choose the options of admin panel 1.ADD NEW FOOD ITEM 2.EDIT FOOD ITEM 3.VIEW MENU 4.REMOVE FOOD ITEM 5.EXIT"))
            if adm_choice == 1:
                aa.add_new_item()
            elif adm_choice == 2:
                aa.edit_from_item()
            elif adm_choice == 3:
                aa.show_inven()
            elif adm_choice == 4:
                aa.remove_item()
            elif adm_choice == 5:
                print(f"You're Exit to the admin panel {Username}")
                admin_crawler = False
            else:
                print("This is the wrong selection please select valid option")
    else:
        print("These are the wrong credentials! SORRY!!!")
elif inp == 2:
    print("Welcome to the user panel")
    username = input("Enter the username here: ")
    password = input("Enter the password here: ")
    if User.login(username, password):
        print(f"You are logged in successfully {username}")
        user_crawler = True
        while user_crawler:
            usr_choice = int(input(f"{username}, Enter the option 1.Register New user 2.Show Menu 3.Place new order 4.Order history 5.Exit 6.Update Profile"))
            if usr_choice == 1:
                uhh.create_user()
                username = input("Enter the New username here: ")
                password = input("Enter the New password here: ")
                if User.login(username, password):
                    print(f"You are logged in successfully {username}")
            elif usr_choice == 2:
                aa.show_inven()
            elif usr_choice == 3:
                uhh.place_order()
            elif usr_choice == 4:
                print(f"Here is your order history, {username}")
                print(uhh.order_history)
            elif usr_choice == 5:
                user_crawler = False
                print("You're Successfully looged out")
            elif usr_choice == 6:
                uhh.update_profile()
                username = input("Enter the username here: ")
                password = input("Enter the password here: ")
                if User.login(username, password):
                    print(f"You are logged in successfully {username}")
            else:
                print("You choose the invalid option")
    else:
        print("These are the wrong credentials! SORRY!!!")
else:
    exit()
