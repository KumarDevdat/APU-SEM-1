
list_Users = []
list_Food = []
list_Order = []
list_Sort = []

def file_Data():
    # Reading data from the users file
    file_User = open("User.txt", "r")
    for data in file_User:  list_Users.append(data)
    file_User.close()

    # Reading data from the food file
    file_Food = open("Food.txt", "r")
    for data in file_Food:  list_Food.append(data)
    file_Food.close()
    
    # Reading data from the orders file
    file_Order = open("Order.txt","r")
    for data in file_Order: list_Order.append(data)
    file_Order.close()

def menu_Main():
    print("\n~- MAIN MENU -~\n")
    choice_Main = input(
        "\n1. ~> Admin \n2. ~> Staff \n3. ~> Customer\n4. ~> Non-Customer\n5. ~> Shutdown\nPlease select your Option:\t")
    if choice_Main == "1":
        key = input("Enter Admin key:\t")
        if login() and key == "0064":
            menu_Admin()
        else:
            print("-{*.*}-\nThis is admin area; Better luck next time!!")
    elif choice_Main == "2":
        key = input("Enter Admin key:\t")
        if login() and key == "0032":
            menu_Staff()    
        else:
            print("-{``^O^``}-\nThis is Staff area; Better luck next time!!")
    elif choice_Main == "3":
        if login():
            menu_Cust()
    elif choice_Main == "4":
        menu_Non_Cust()
    elif choice_Main == "5":
        exit(0)
    else:
        print("\nWrong Option...\t" + choice_Main)
        menu_Main()

def menu_Admin():
    print("\n~- Admin Menu -~\n")
    option = input("1. ~> Food Management\n2. ~> Staff Management\n3. ~> Display all records\n3. ~> Display specific records\n5. ~> Assign Order to Staff\n6. ~> Main-Menu\nPlease select your option:\t")
    if option == "1":
        food_Mgmt()
    elif option == "2":
        staff_Mgmt()
    elif option == "3":
        all_Records()
    elif option == "4":
        specific_Record()
    elif option == "5":
        order_Assign()
    elif option == "6":
        menu_Main()
    else:
        print("Wrong Option:\t" + option)
        menu_Admin()
    menu_Main()

def menu_Staff():
    print("\n~- Staff Menu -~\n")
    for data in list_Order:
        if data.split(",")[1] == str(user):
            print(data.rstrip(","))
            list_Order.remove(data)
            
    file = open("Order.txt","w")
    for data in list_Order:
        file.write(data)
    file.close()
    menu_Main()

def menu_Cust():
    print(" \n~- Customer Menu -~\n")
    option = input(
        "\n1. ~> View food by Category \n2. ~> View food by Items \n3. ~> Place Order\n4. ~> Give feedback\n5. ~> Main Menu\nPlease select your Option:\t")
    if option == "1":
        for food in sorted(list_Food):
            if food.split(",")[0] == food.split(",")[0]:
                print(food.split(",")[0]+" -> "+food.split(",")[1]+" -> RM"+food.split(",")[2])
        list_Sort.clear()
    elif option == "2":
        list_Temp = []
        for food in list_Food:
            list_Temp.append(food.rstrip().split(",")[1])
        for data in sorted(list_Temp): print(data)
    elif option == "3":
        place_Order()
    elif option == "4":
        feedback()
    elif option == "5":
        menu_Main()
    else:
        print("Wrong Option:\t" + option)
        menu_Cust()
    menu_Main()

def menu_Non_Cust():
    print("\n~- Non-Customer -~\n")
    option = input("1. ~> View Food Menu\n1. ~> Register\n3. ~> Main-Menu\n\nPlease select your option:\t")
    if option == "1":
        for food in list_Food: print(food.replace(","," -> "))
    elif option == "2":
        user_Name = input("Please Enter username:\t")
        for user in list_Users:
            if user.split(",")[1] == user_Name.strip():
                print("User Exist...!!")
                found = True
                break
        if not found:
            passw = input("Please Enter your password:\t")
            cust_Name = input("Please Enter Your Name:\t")
            cust_Phone = input("Please Enter Your Contact:\t")
            list_Users.append("1," + user_Name + "," + passw + "," + cust_Name + "," + cust_Phone + "\n")
            print("User registered added Successfully")
            found = True
    elif option == "3":
        menu_Main()
    else:
        print("Wrong Option:\t" + option)
        menu_Non_Cust()

    menu_Main()

def food_Mgmt():
    print("\n~- Food Management -~\n")
    option = input("1. ~> Add Food\n2. ~> Modify Food\n3. ~> Search Food\n4. ~> Delete Food\n5. ~> Admin-Menu\n\nPlease select your option:\t")
    found = False
    food_Name = input("\nEnter food name:\t")
    food_Type = input("\nEnter food type:\t")
    food_Price = input("\nEnter food price:\t")
    
    if option == "1":
        for food in list_Food:
            if food.split(",")[1] == food_Name.strip():
                found = True
                break
        while not found:
            list_Food.append(food_Type+","+food_Name+","+food_Price+"\n")
            print("Food Item added Successfully")
            found = True
    elif option == "2":
        for i, food in enumerate(list_Food):
            if food.split(",")[1] == food_Name.strip():
                list_Food[i] = food_Type+","+food_Name+","+food_Price+"\n"
                print("Food Item Updated Successfully")
                found = True
                break
    elif option == "3":
        for food in list_Food:
            if food.split(",")[1] == food_Name.strip():
                print(food.rstrip().split(",")[0]+" "+food.rstrip().split(",")[1]+" RM"+food.rstrip().split(",")[2])
                break
    elif option == "4":
        for food in list_Food:
            if food.split(",")[1] == food_Name.strip():
                list_Food.remove(food)
                print("Food Item Deleted Successfully")
                found = True
    elif option == "5":
        menu_Admin()
    else:
        print("Wrong Option:\t" + option)
        food_Mgmt()

    if found:
        file_Food = open("Food.txt", "w")
        for food in list_Food:  file_Food.write(food)
        file_Food.close()
        print("food file updated")

    menu_Admin()

def staff_Mgmt():
    print("\n~- Staff Management -~\n")
    option = input("1. ~>Register Staff\n2. ~>Modify Staff\n3. ~>Search Staff\n4. ~>Delete Staff\n5. ~> Admin-Menu\n\nPlease select your option:\t")
    found = False
    user_Name = input("Please Enter username:\t")

    if option == "1":
        for user in list_Users:
            if user.split(",")[1] == user_Name.strip():
                print("User Exist...!!")
                found = True
                break
        if not found:
            passw = input("Please Enter your password:\t")
            cust_Name = input("Please Enter Your Name:\t")
            cust_Phone = input("Please Enter Your Contact:\t")
            list_Users.append("2," + user_Name + "," + passw + "," + cust_Name + "," + cust_Phone + "\n")
            print("User registered added Successfully")
            found = True
    elif option == "2":
        for i, user in enumerate(list_Users):
            if user.split(",")[1] == user_Name.strip():
                passw = input("Please Enter your password:\t")
                cust_Name = input("Please Enter Your Name:\t")
                cust_Phone = input("Please Enter Your Contact:\t")
                list_Users[i] = "2," + user_Name + "," + passw + "," + cust_Name + "," + cust_Phone + "\n"
                print("User Updated Successfully")
                found = True
                break
    elif option == "3":
        for user in list_Users:
            if user.split(",")[1] == user_Name.strip():
                print(user.split(",")[0]+" "+user.split(",")[1]+" "+user.split(",")[2]+" "+user.split(",")[3])
                break
    elif option == "4":
        for user in list_Users:
            if user.split(",")[1] == user_Name.strip():
                list_Users.remove(user)
                print("User Deleted Successfully")
                found = True
    elif option == "5":
        menu_Admin()
    else:
        print("Wrong Option:\t" + option)
        staff_Mgmt()

    if found:
        file_User = open("User.txt", "w")
        for user in list_Users: file_User.write(user)
        file_User.close()
        print("User file updated")

    menu_Admin()

def all_Records():
    print("\n~- Display All records -~\n")
    option = input(
        "1. ~> Food Category\n2. ~> Food Item Catogary-wise\n3. ~> customer Orders\n4. ~> Customer Payment\n5. ~> Admin-Menu\n\nPlease select your option:\t")
    if option == "1":
        for food in sorted(list_Food): print(food.split(",")[0])
    elif option == "2":
        for food in sorted(list_Food):
            if food.split(",")[0] == food.split(",")[0]:
                print(food.split(",")[0]+" -> "+food.split(",")[1]+" -> RM"+food.split(",")[2])
        list_Sort.clear()
    elif option == "3":
        for data in list_Order:
            print(data.rstrip(",")[4:])
    elif option == "4":
        for data in list_Order:
            print(data.split(",")[3])
    elif option == "5":
        menu_Admin()
    else:
        print("Wrong Option:\t" + option)
        all_Records()
    menu_Admin()

def specific_Record():
    print("\n~- Display Specific record -~\n")
    option = input(
        "1. ~> Customer Order\n2. ~> Customer Payment\n3. ~> Menu-Admin\n\nPlease select your option:\t")
    print("\n")
    if option == "1":
        c_Id = input("Enter customer ID:\t")
        for data in list_Order:
            if c_Id == data.split(",")[2]:
                print(data.rstrip(","))
    elif option == "2":
        c_Amount = input("Enter customer Payment amount:\t")
        for data in list_Order:
            if c_Amount == data.split(",")[3]:
                print(data.rstrip(","))
    elif option == "3":
        menu_Admin()
    else:
        print("Wrong Option:\t" + option)
        specific_Record()
    menu_Admin()

def place_Order():
    print("\n~- Create Order -~\n")
    print("Type  ->  Item  ->  Price\n''''''''''''''''''''''''''")
    for food in sorted(list_Food):
        if food.split(",")[0] == food.split(",")[0]:
            print(food.split(",")[0]+" -> "+food.split(",")[1]+" -> RM"+food.split(",")[2])

    total = 0
    list_Ordered_Item = []
    item_Name = input("Please enter the name of item or <-1> to exit:\t")
    while item_Name != "-1":
        found = False
        for data in list_Food:
            if data.split(",")[1] == item_Name:
                item_price = data.split(",")[2]
                item_Quantity = input("Enter the number of Items:\t")
                list_Ordered_Item.append(","+item_Name+","+item_Quantity)
                total = total + int(item_price) * int(item_Quantity)
                found = True
                break
        if not found:
            print("Wrong Input!!!")
        item_Name = input("Please enter the name of item or <-1> to exit:\t")

    print("Please pay:\t"+str(total))
    list_Order.append(str(len(list_Order))+","+"0"+","+str(user)+","+str(total))

    file = open("Order.txt","w")
    for data in list_Order:
        file.write(data)
    for data in list_Ordered_Item:
        file.write(data)
    file.write("\n")
    file.close()

def order_Assign():
    found = False
    print("\n~- Assign Order -~\n")
    staff_Id = input("Enter Staff ID:\t")
    for line in list_Users:
        if line.rstrip().split(",")[1] == staff_Id.strip():
            order_Id = int(input("Enter Order Id:\t"))
            if list_Order[order_Id].rstrip(",")[1] == "0":
                list_Order[order_Id] = list_Order[order_Id][:list_Order[order_Id].index(",0,")]+","+staff_Id+list_Order[order_Id][list_Order[order_Id].index(",0,")+2:]
            else:
                print("Order is already assigned!!")
            found = True
            break
    if not found:
        print('Incorrect username!!')
        order_Assign()

    file = open("Order.txt","w")
    for data in list_Order:
        file.write(data)
    file.close()
    
    menu_Admin()

def login():
    found = False
    global user
    user = input("Enter your Username:")
    passw = input("Enter your password:")
    for line in list_Users:
        if line.rstrip().split(",")[1] == user.strip() and line.rstrip().split(",")[2] == passw.strip():
            print("Success")
            found = True
            return True
    if not found:
        print('Incorrect username or password!')
        return False

def feedback():
    feedback = input("Please write your feedback:\t")
    file = open ("Feedback.txt","a")
    file.write(user+","+feedback)
    file.close()

file_Data()
menu_Main()