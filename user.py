
import admin as ad

class User:
    login_info = {"Raja": "Raja"}
    userProfile = {"Raja":{"Name":"Raja","Phone Number":7397098776,"Email":"raja@gmail.com","Address":"17, Ramaling street,TN.","Password":"raja1234"}}

    def __init__(self, usrname, fullname, phoneno, email, address, password):
        self.usrname = usrname
        self.fullname = fullname
        self.number = phoneno
        self.email = email
        self.address = address
        self.password = password
        User.login_info[self.usrname] = self.password
        User.userProfile[self.usrname] = {"Name":self.fullname,"Phone Number":self.number,"Email":self.email,"Address":self.address,"Password":self.password}
        self.order_history = {}
        self.orders=1

    @classmethod
    def login(cls, username, password):
        if cls.login_info.get(username) == password:
            print("******** You have logged in Successfully ******")
            return True
        else:
            print("*** SORRY! Login Failed ***")
            return False


    def place_order(self):
        print("Please order items from the MENU shown below.")
        print(ad.show_usrmenu())
        user_choice = int(input("Press '1' to Order or '2' to exit : "))
        if user_choice == 1:
            l1 = list(input("Enter the Food ID here: "))
            foodid=[]
            quan=[]
            ##price=[]
            total=[]
            x=0
            for word in l1:
                if word.isdigit():
                    foodid.append(int(word))
            for id in foodid:
                l2 = int(input(f"Enter the required plates/Quantity for Food ID-{id} here: "))
                quan.append(l2)   
            again_ask = input("Can we confirm this order, Please enter 'YES' or 'NO' :-  ")
            if again_ask == "YES":
                print("\n**********Your Order is***********")
                for k in range(len(foodid)):
                    print(f'''{ad.menu[foodid[k]]["Name"]} ({ad.menu[foodid[k]]["Quantity"]}) [{ad.menu[foodid[k]]["Price"]}] x {(quan[k])} = {quan[k]*ad.menu[foodid[k]]["Price"]}''')
                    total.append(ad.menu[foodid[k]]["Price"]*quan[k])   
                print(f"It costs you {sum(total)}INR in total")
                for l in range(len(foodid)):
                    self.order_history[self.orders] = {
                                    "Item Name":ad.menu[foodid[l]]["Name"],
                                    "Price": ad.menu[foodid[l]]["Price"],
                                    "Quantity": quan[l]
                                    }
                    self.orders+=1
                for m in range(len(foodid)):      
                    final_stock = ad.menu[foodid[m]]["Stock"] - quan[m]
                    ad.menu[foodid[m]]["Stock"] = final_stock
                print("You're order is successfully placed")

            elif again_ask == "NO":
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("Since you selected 2nd option, we cancelled this")
        else:
            print("Entered the invalid choice")

    def update_profile(self):
        updname = input("Enter your Username:- ")
        print("*****Your Profile*******")
        print(User.userProfile[updname])
        nm = input("Enter your Name here: ")
        pn = int(input("Enter your Phone number here: "))
        em = input("Enter your Email here: ")
        ad = input("Enter your Address here: ")
        pd = input("Enter your Password here: ")
        User.userProfile[updname]["Name"] = nm
        User.userProfile[updname]["Phone Number"] = pn
        User.userProfile[updname]["Email"] = em
        User.userProfile[updname]["Address"] = ad
        User.userProfile[updname]["Password"] = pd
        print("*****Edited your Profile successfully*****")
        print(User.userProfile[updname])
        User.login_info[updname]=pd
        
    def orders_history(self):
        ordhist=self.order_history
        for i in ordhist:
            print("Item Name:- ",ordhist[i]["Item Name"])
            print("Price:- ",ordhist[i]["Price"])
            print("Quantity:- ",ordhist[i]["Quantity"])
            print("\n")

        


       

