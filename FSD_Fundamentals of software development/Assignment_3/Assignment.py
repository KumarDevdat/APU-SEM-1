
user_List = []

def file_Read(choice):
    # Reading Usernames and passwords from admin file into a list.
    if choice == 1:
        f_Hand = open("admin_File.txt", "r")
    else:
        f_Hand = open("customer_File.txt", "r")
    for admin_Data in f_Hand:
        user_List.append(admin_Data)
    f_Hand.close()
    
def file_Write(choice):
    # Writing User name and Password from a list into file.
    if choice == 1:
        f_Hand = open("admin_File.txt", "w")
    else:
        f_Hand = open("customer_File.txt", "w")
    for Data in user_List:
        f_Hand.write(Data)
    f_Hand.close()
    user_list = []

def register(choice):
    # Registering new User as Admin or Customers
    user = input('Create Username: ')
    file_Read(choice)
    if (user+'\n') in user_List:
        print ("That user already exist")
        return False
    else:
        user_List.append(user + '\n')
        password = input('Create Password: ')
        user_List.append(password + '\n')
        file_Write(choice)
        return True

def login(choice):
    # Login Portal for User as Admin or Customers
    user = input('Enter User:\t ')
    file_Read(choice)
    if (user+'\n') in user_List:
        password = input('Enter password:\t ')
        # Position of Password is checked as if it is next to user name access is given if statement is True
        if ((password+'\n') in user_List) and (password+'\n' == user_List[user_List.index(user+'\n')+1]):
            if choice == 1:
                admin()
            else:
                customer()
        else:
            print("Password incorrect!")
        return False
    else:
        print("User Invalid!")
        return True

def car():
    car_List = []

    # Reading cars from file into a list
    f_Hand = open("car.txt", "r")
    for cars in f_Hand:
        car_List.append(cars)
    f_Hand.close()

    # Admin can Modify cars' data.
    print("Enter < 1 > to view all cars.\nEnter < 2 > to add a new car.\nEnter < 3 > to update car details.")
    choice = int(input("Enter < 4 > to Delete Car. \nEnter < 5 > for any other option to exit: \nOption:\t")) 

    if choice == 1:
        # Print all the cars
        for cars in car_List:
            print(cars)
        car_List = []
        
    elif choice == 2:
        # Add a new car
        car_Num = input("Enter Car Number:- \t")
        if not(car_Num+'\n') in car_List:
            f_Hand = open("car.txt", "w")
            f_Hand_Avail = open("availablecars.txt","w")
            car_Name = input("Enter Car Name:- \t")
            car_Color = input("Enter Car Color:- \t")
            car_List.append(car_Num+'\n')
            car_List.append(car_Name+'\n')
            car_List.append(car_Color+'\n')
            for cars in car_List:
                f_Hand.write(cars)
                f_Hand_Avail.write(cars)
            car_List = []
            f_Hand.close()
            f_Hand_Avail.close()
        else:
            print ("\tCar already exist!!!")
            
    elif choice == 3:
        # Modify existing car
        car_Num = input("Enter Car Number:- \t")
        if (car_Num+'\n') in car_List:
            x = car_List.index(car_Num+'\n')
            car_Name = input("Enter Car Name to change  it:- \t")
            car_Color = input("Enter Car Color to change it:- \t")
            car_List[x] = car_Num+'\n'
            car_List[x+1] = car_Name+'\n'
            car_List[x+2] = car_Color+'\n'
            f_Hand = open("car.txt", "w")
            for cars in car_List:
                f_Hand.write(cars)
            car_List = []
            f_Hand.close()
    
    elif choice == 4:
        # Delete car
        car_Num = input("Enter Car Number:- \t")
        if (car_Num+'\n') in car_List:
            x = car_List.index(car_Num+'\n')
            car_List.pop(x)
            car_List.pop(x+1)
            car_List.pop(x+2)
            f_Hand = open("car.txt", "w")
            for cars in car_List:
                f_Hand.write(cars)
            car_List = []
            f_Hand.close()  
    else:
        f_Hand.close()
        exit()
    f_Hand.close()
    
def avilable_Car():
    print("display available car list")
    f_Hand_Avail = open("availablecars.txt", "r")
    for cars in f_Hand_Avail:
        print(cars)
    f_Hand_Avail.close()

def booked_Car():
    car_List = []
    f_Hand = open("bookedcars.txt", "r")
    for cars in f_Hand:
        car_List.append(cars)
    f_Hand.close()
    car_Num = input("Enter car number to find booked car:\t")
    if (car_Num+'\n') in car_List:
        x = car_List.index(car_Num+'\n')
        car_Name = input("Enter Car Name to change  it:- \t")
        car_Color = input("Enter Car Color to change it:- \t")
        print(car_List[x])
        print(car_List[x+1])
        print(car_List[x+2])    

def return_Car():
    car_List = []
    car_Num = input("Enter Car Number:- \t")
    car_List.append(car_Num)
    car_Name = input("Enter Car Name to change  it:- \t")
    car_List.append(car_Name)
    car_Color = input("Enter Car Color to change it:- \t")
    car_List.append(car_Color)
    # Add returned car back to available cars.
    f_Hand = open("availablecars.txt", "w")
    for cars in car_List:
        f_Hand.write(cars)
    car_List = []
    f_Hand.close()

def book_Car(): 
    car_List= []
    f_Hand_Avail = open("availablecars.txt", "r")
    for cars in f_Hand_Avail:
        car_List.append(cars)
    f_Hand_Avail.close()
    car_Num = input("Enter car number from list to book the car:\t")
    # remove the booked car from available cars.  
    if (car_Num+'\n') in car_List:
        x = car_List.index(car_Num+'\n')
        car_List.pop(x)
        car_List.pop(x+1)
        car_List.pop(x+2)
        f_Hand = open("availablecars.txt", "w")
        for cars in car_List:
            f_Hand.write(cars)
        car_List = []
        f_Hand.close()

        # Adding payment to payment file 
        data_List = []
        f_Hand2 = open("customer_Payment.txt", "w")
        c_Id = input("Enter customer Id:\t")
        data_List.append(c_Id)
        Payment = input("Enter Payment:\t")
        data_List.append(Payment)
        time = input("Enter Time")
        data_List.append(time)
        for data in data_list:
            f_Hand2.write(data)
        f_Hand2.close()
        data_List = []
    else:
        print("Car not found")
        
def customer_Payment():
    # Checking specific customer payment
    data_List = []
    f_Hand = open("customer_Payment.txt", "r")
    for data in f_Hand:
        data_List.append(data)
    c_Id = input("To check payments. \nEnter customer Id:\t")
    if (c_Id+'\n') in data_List:
        x = car_List.index(car_Num+'\n')
        print(data_List[x])
        print(data_List[x+1])
              
    data_List = []
    f_Hand.close()    

def time_duration():
    # Checking specific customer payment
    data_List = []
    f_Hand = open("customer_Payment.txt", "r")
    for data in f_Hand:
        data_List.append(data)
    time = input("To check booking. \nEnter time:\t")
    if (time+'\n') in data_List:
        x = car_List.index(car_Num+'\n')
        print(data_List[x-2])
        print(data_List[x-1])
        print(data_list[x])      
    data_List = []
    f_Hand.close()   

    
def admin():
    print("Enter < 1 > to Modify car details. \nEnter < 2 > to view available cars.")
    print("Enter < 3 > to Customer Payment for a specific time duration.")
    print("Enter < 4 > to Search for Specific Car Booking. \nEnter < 5 > Specific Customer Payment")
    print("Enter < 6 > to Retun a Rented Car. \nEnter < 7 > or any other option to Exit.")
    choice = int(input("Enter the Choice:\t"))
    if choice == 1:
        car()
    elif choice == 2:
        avilable_Car()
    elif choice == 3:
        time_duration()
    elif choice == 4:
        booked_Car()
    elif choice == 5:
        customer_Payment()
    elif choice == 6:
        return_Car()
    else:
        exit()
    
    
def customer():
    print("Enter < 1 > View details of cars to be rented out.")
    print("Enter < 2 > Select and Book a car.")
    print("Enter < 3 > or any other option to exit.")
    choice = int(input("Choice:\t"))
    if choice == 1:
        avilable_Car()
    elif choice == 2:
        book_Car()
    else:
        exit()

print(("Enter < 1 > to register. \nEnter < 2 > to  Login."))
option = int(input("Enter < 3 > to Check Avilable cars \nEnter < 4 > or any other option to exit. \nOption:\t"))
if option == 1:
    reg_Choice = int(input("Enter < 1 > for Admin Register. \nEnter < 2 > for Customer Register. \nchoice: \t"))
    register(reg_Choice)
elif option == 2:
    login_Choice = int(input("Enter < 1 > for Admin Login. \nEnter < 2 > for Customer Login. \nchoice: \t"))
    login(login_Choice)
elif option == 3:
    avilable_Car()
else:
    exit()
