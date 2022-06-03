admin_keys = {"Pavithra": "Pavithra@7297"}

inven = {1: {'ItemName': 'Pancake', 'ItemID': 1, 'Price': 70, 'Stock': 15},
        2: {'ItemName': 'Waffle', 'ItemID': 2, 'Price': 100, 'Stock': 20},
        3: {'ItemName': 'Cake', 'ItemID': 3, 'Price': 80, 'Stock': 5},
		4: {'ItemName': 'Icecream', 'ItemID': 4, 'Price': 50, 'Stock': 25}}


def add_new_item():
    itemname = input("Enter the Food item name: ")
    itemid = int(input("Enter the Food item id: "))
    price = int(input("Enter the price of the Food item: "))
    stock = int(input("Enter the stock value of Food item: "))
    inven[itemid] = {
        "ItemName": itemname,
        "ItemID": itemid,
        "Price": price,
        "Stock": stock
    }
    print("The Food item "+itemname+ " is successfully added")
    return inven


def edit_from_item():
    item = int(input("Enter the Food item id which you want to edit: "))
    a = input("Enter the Food item name")
    b = int(input("Enter the price of Food item"))
    d = int(input("Enter the stock of the Food item"))
    inven[item]["ItemName"] = a
    inven[item]["Price"] = b
    inven[item]["Stock"] = d
    print("*****Edited Food item successfully*****")
    return inven

def show_inven():
    print("*****MENU FOR BREAD AND BAKES*****")
    for i in inven:
        print("Item Name: ",inven[i]["ItemName"])
        print("Price: ",inven[i]["Price"],"INR")
        print("Item ID: ",inven[i]["ItemID"])

def remove_item():
    d = int(input("Enter the Food Item id which you want to exit"))
    inven.pop(d)
    print("Remove Food item successfully ")
    return inven
