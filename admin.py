import random
admin_keys = {"admin": "admin"}

menu = {1: {'FoodID': 1, 'Name': 'Mutton Briyani','Quantity':'500gm', 'Price': 210,'Discount': 10, 'Stock': 10},
        2: {'FoodID': 2, 'Name': 'Chicken Fried Rice','Quantity':'500gm', 'Price': 260,'Discount': 9, 'Stock': 12},
        3: {'FoodID': 3, 'Name': 'Prawn Noodles','Quantity':'500gm', 'Price': 230,'Discount': 8, 'Stock': 14},
        4: {'FoodID': 4, 'Name': 'Fish Gravy','Quantity':'250ml', 'Price': 180,'Discount': 7, 'Stock': 16},
        5: {'FoodID': 5, 'Name': 'Quail Fry','Quantity':'1 piece', 'Price': 120,'Discount': 6, 'Stock': 18}}
#nested dict

def add_new_item():
    while(True):
        temp = random.randint(1,99)
        if(temp not in menu.keys()):
            foodid = temp
            break
    name = input("Enter the Name: ")
    quantity = input("Enter the Quantity(gm/ml/piece): ")
    price = int(input("Enter the Price(INR) of the item: "))
    discount = int(input("Enter the Discount(%) for item: "))
    stock = int(input("Enter the Stock value of item: "))
    menu[foodid] = {
        "FoodID" : foodid,
        "Name": name,
        "Quantity": quantity,
        "Price": price,
        "Discount": discount,
        "Stock": stock
    }
    print("The Item "+name+ " is successfully added")
    return menu


def edit_from_item():
    f = int(input("Enter the FoodID which you want to edit: "))
    n = input("Enter the Name: ")
    q = input("Enter the Quantity(gm/ml/piece): ")
    p = int(input("Enter the Price(INR): "))
    d = int(input("Enter the Discount(%): "))
    s = int(input("Enter the Stock: "))
    menu[f]["Name"] = n
    menu[f]["Quantity"] = q
    menu[f]["Price"] = p
    menu[f]["Discount"] = d
    menu[f]["Stock"] = s
    print("*****Edited item successfully*****")
    return menu

def show_menu():
    print("*****HERE IS THE MENU OF PY CHETTINAD HOTEL*****")
    for i in menu:
        print("FoodID: ",menu[i]["FoodID"])
        print("Name: ",menu[i]["Name"])
        print("Quantity: ",menu[i]["Quantity"])
        print("Price: ",menu[i]["Price"],"INR")
        print("Discount: ",menu[i]["Discount"],"%")
        print("Stock: ",menu[i]["Stock"])
        print("\n")

def show_usrmenu():
    print("*****THE MENU -->ACCORD HOTEL*****")
    for i in menu:
        print(str(menu[i]["FoodID"])+"."+menu[i]["Name"]+" ("+menu[i]["Quantity"]+") ["+str(menu[i]["Price"])+"]")
    return("\n********Please place your order********")
def remove_item():
    d = int(input("Enter the Food id which you want to remove: "))
    menu.pop(d)
    print("Removed item successfully ")
    return menu
