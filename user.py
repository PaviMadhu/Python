import admin as ad
userarray={1: {'Name': 'Pavithra', 'ID':1, 'Phone': '7890567890', 'Email': 'xyz@gmail.com', 'Address': 'Chennai','Password':'Pavithra@7297'}}

class User:
    login_info = {"Pavithra": "Pavithra@7297"}
    userarray=[]

    def __init__(self, name, phoneno, email, address, password):
        self.name = name
        self.number = phoneno
        self.email = email
        self.address = address
        self.password = password
        User.login_info[self.name] = self.password
        self.profile={"Name":name}
        self.order_history = {}

    @classmethod
    def login(cls, username, password):
        if cls.login_info.get(username) == password:
            print("You're are successfully logged into User portal.....")
            return True
        else:
            print("SORRY! These are the Wrong Credentials")
            return False
    
    def create_user(self):
        
            uname=input("Enter the Full user name: ")
            uid=int(input("Enter user ID: "))
            pno=input("Enter the phone number: ")
            email=input("Enter mail id: ")
            address=input("Enter address: ")
            pwd=input("Enter password: ")
            S=User(uname,pno,email,address,pwd)
            userarray[uid] = {
                 "Name": uname,
                 "ID": uid,
                 "Phone": pno,
                 "Email": email,
                 "Address": address,
                 "Password": pwd
            }
			print("Registration successfully completed. Redirecting to login...")
            return userarray
    
    def update_profile(self):
            print("Available user names")
            print(userarray)
            uid = int(input("Enter the user id which you want to edit: "))
            a = input("Enter the User name: ")
            b = input("Enter the Phone Number: ")
            d = input("Enter the Email: ")
            e = input("Enter the Address: ")
            f = input("Enter the Password: ")
            userarray[uid]["Name"] = a
            userarray[uid]["Phone"] = b
            userarray[uid]["Email"] = d
            userarray[uid]["Address"] = e
            userarray[uid]["Password"] =f            
            S=User(a,b,d,e,f)
            return userarray
            print("*****Edited Profile successfully*****")
            
    
    def place_order(self):
        print("What you want to order here in the BREAD AND BAKES menu")
        print(ad.show_inven())
        user_choice = int(input("If you want to order then select 1.YES 2.NO"))
        if user_choice == 1:
            n=int(input("Enter how many items do you want to Order"))
            x=0
            for i in range(n):
             
             itemid = int(input("Enter the Food Item id here: "))
             quan = int(input("Enter the quantity of the Food item: "))
             x += (ad.inven[itemid]["Price"]-ad.inven[itemid]["Discount"]) * quan #Discount is reduced from price
            again_ask = input("Are you still want to order this Enter YES or NO")
            if again_ask == "YES":
                print(f'''Your Food item name is {ad.inven[itemid]["ItemName"]}''')
                print(f'''Your Food Price is {ad.inven[itemid]["Price"]}''')
                print(f'''Discounted Price is {ad.inven[itemid]["Price"]-ad.inven[itemid]["Discount"]}''')
                print(f"This is your quantity {quan}")
                print(f"It costs you {x}INR in total")
                print("You're all set for this order")
                self.order_history[itemid] = {
                    "Food Item Name": ad.inven[itemid]["ItemName"],
                    "Price": ad.inven[itemid]["Price"],
                    "Discounted Price": ad.inven[itemid]["Price"]-ad.inven[itemid]["Discount"],
                    "Quantity ordered": quan
                }
                final_stock = ad.inven[itemid]["Stock"] - quan
                ad.inven[itemid]["Stock"] = final_stock
                print("You're order is successfully placed")

            elif again_ask == "NO":
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")

#def cnu()
       

