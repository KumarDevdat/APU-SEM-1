#Devdat Kumar
#TP058340
def menu():
    print("\n\n-------------UNIVERSITY STUDENT APARTMENT MANAGEMENT SYSTEM-------------\n")
    while True:
        print("\n" + "-"* 72 + "\n \nEnter 1 to assign apartment to the student. \nEnter 2 to search for student details.")
        print("Enter 3 to checkout")
        print("Enter 4 to find the total funds collected.\nEnter 5 to setup detabase as empty, all the rooms empty with no student.")
        print("Enter 6 to Exit.")
        choice = int(input("\n\tEnter the number from given options:\t"))
        if choice == 1:
            apt_Available()
        elif choice == 2:
            search_Details()
        elif choice == 3:
            checkout()
        elif choice == 4:
            a = 0
            b = 0
            y, x = total_payment(a,b)
            print("\nTotal rental collected:", x)
            print("total amount collected:", y)
            z = y - x
            print("Total deposit collected:", z)          
        elif choice == 5:
            while True:
                sure = input("Do you want to reset/setup all the data, <yes> or <no>:\t")
                if sure == 'yes':
                    apt_New()
                    break
                elif sure == 'no':
                    break
                else:
                    print("You Entered wrong option")
                    continue 
        elif choice == 6:
            exit()    
        else:
            print("\n\t\tYou Entered wrong option\n " + "\t\t" + "-" * 24 + "\n")
            print()
            continue

        continue

def apt_New():
    
    data_List_1 = []
    room_Stat = 0 
    for i in range(100):    
        data_List_1.append(room_Stat)    
    file_1 = open("Apartment_Available.txt",'w')
    for data_1 in data_List_1:
        file_1.write(str(data_1) + '\n')
    file_1.close()

    data_List_2 = []
    amount = 0
    for j in range(3):    
        data_List_2.append(amount)
    file_2 = open("Funds_collected.txt",'w')
    for data_2 in data_List_2:
        file_2.write(str(data_2) + '\n')
    file_2.close()

    file_3 = open("student_Record.txt",'w')
    file_3.close()
    
    file_4 = open("Checkouts.txt",'w')
    file_4.close()
    
    print("\nNew file is created, with data of all empty rooms, with no student.")
    print("New funds file is created, with no fund's data.")
    print("New student Record file is created with no student's data.")
    print("Checkout student Record file is created with no student's data.")

    
def apt_Available():
    print("-" * 80)
    print("\n\n There are 2 types of Apartments available.\n\n Type A: 2 Single Rooms   -(RM 400/- per single room)-, Kitchen & Laundry.\n Type B: 1 Master Bedroom -(RM 500/- per master room)-, only Laundry,\n\t 2 Single Rooms   -(RM 300/- per single room)-, Kitchen & Laundry.")
    print("\n Type A: Internet(Optional) for RM 50/- \n Type B: Internet(Optional) for RM 40/- \n\n") 
    print("-" * 80)
    print("\n")
    while True:
        apt_Type = str(input("Enter Room Type <A> or <B>:\t")).upper()
        if apt_Type == 'A' or apt_Type == 'B':
            if apt_Type == 'B':
                apt_Type = str(input("Enter Room Type <S> or <M>:\t")).upper()
                if apt_Type == 'S':
                    apt_Type = 'B'
                elif apt_Type == 'M':
                    apt_Type = 'C'
                else:
                    print("You Entered wrong option")
                    continue  
            j, count, apt_Num, room_Num = std_assign(apt_Type)  
            if count != 0:
                print("Currently there are:", count, " free rooms available in Type ", apt_Type ," Apartments")
                x = apt_Assign(j,apt_Type, apt_Num, room_Num)
                break
            else:
                print("Currently there are no rooms available in Type ", apt_Type ," Apartments, please try other type.")
                continue
        else:
            print("You Entered wrong option")
            continue
    
        
def apt_Assign(j,apt_Type, apt_Num, room_Num):
    while True:
        net = input("Do you want to subscribe for Internet connection, <yes> or <no>:\t")
        if net == 'yes' or net == 'no':
            break
        else:
            print("You Entered wrong option")
            continue
    std_Name = input("Enter your name:\t").lower()
    tp_Num = input("Enter your Tp number:\t")
    r = 0
    f_R = 0
    t_Type = 'T'
    r_Type = 'R'
    print("\nYou are assigned Apartment type ", apt_Type," apartment number ",apt_Num," room number ", room_Num,"\n Internet connection = ?", net)    
    price_Deposit = 100
    amount, pay_Type, remain, full_Rent = payment_Type(apt_Type, net, r,f_R)
    price_Rental = amount - price_Deposit
    y = total_payment(price_Deposit, price_Rental)
    std_Record = std_Rec(j,apt_Type, apt_Num, room_Num, net, std_Name, tp_Num, pay_Type, amount,r_Type,remain,t_Type,full_Rent)    
    
        
def std_assign(option):

    file = open("Apartment_Available.txt",'r')
    data = file.read().splitlines()
    file.close()

    count = 0
    count_A = 0
    count_B = 0
    count_C = 0
    count_New = 0
    count_Total_A = 40
    count_Total_B = 40
    count_Total_C = 20
    data_List = []
    
    for x in data:
        count = count + 1
        a = int(x)
        if a == 0:
            if count <= count_Total_A:
                count_A = count_A + 1
            elif count <= count_Total_A + count_Total_B:
                count_B = count_B + 1
            elif count <= count_Total_A + count_Total_B + count_Total_C:
                count_C = count_C + 1
        data_List.append(a)
        
    
    if option == 'A':
        count_New = count_A
    elif option == 'B':
        count_New = count_B
    elif option == 'C':
        count_New = count_C
            
        
    for i in range(count_New):
        if option == 'A':
            j = i 
        elif option == 'B':
            j = i + count_Total_A
        elif option == 'C':
            j = i + count_Total_A + count_Total_B
        if data_List[j] == 0:
            data_List[j] = 1
            if data_List[j] == 1:
                apt_Num = (int(j / 2) + 1)
                if j % 2 == 0:
                    room_Num = 1
                    break
                else:
                    room_Num = 2
                    break
    
    file = open("Apartment_Available.txt",'w')
    for data_New in data_List:
        file.write(str(data_New) + '\n')
    file.close()

    return int(j),int(count_New), int(apt_Num), int(room_Num)

def payment_Type(apt_Type, net,left_Amount,t_amount):
    while True:
        total_Amount, price_Deposit = payment(apt_Type,net)
        
        print("Payment for five months contract: ")
        print("  your are chaged: ", ((total_Amount - price_Deposit)/5)," x  5 = ", (total_Amount - price_Deposit),"\n \t\t\tDeposit = ", price_Deposit,"\n \t\t","-" * 25,"  \n \t\t\t  Total = ",total_Amount)
        
        pay_Type = str(input("do you want to pay, 'full <f> payment' or 'partial <p> payment'\n Enter f or p: "))
        if pay_Type == 'f':
            amount_Pay = total_Amount
            print("please pay RM:", amount_Pay)
            amount = int(input("pay:\t"))
            if amount == amount_Pay:
                remain = 0
                return amount, pay_Type, remain, total_Amount
            else:
                print("You did not pay the exact same amount, please pay again")
                continue

        elif pay_Type == 'p':
            print("you will be charged minimum 50% of your rental fess for five months agreement and RM 100 for deposit as first installment") 
            amount_Pay = int((int(total_Amount)) - int(price_Deposit)) / 2 + int(price_Deposit)
            print("please pay: RM", int(amount_Pay))
            amount = int(input("pay:\t"))
            if amount >= amount_Pay:
                remain = total_Amount - amount
                print("please pay remaining RM",remain," at least RM",remain/4," every month for next 4 months\n\tThankyou!")
                return amount, pay_Type, remain, total_Amount
            else:
                print("You did not pay the exact same amount, please pay again")
                continue        
        else:
            print("You Entered wrong option")
            continue

def payment(apt_Type,internet):
    
    month = 5
    price_Deposit = 100
    total_Deposit = 0
    total_Price_Room = 0
    if apt_Type == 'A':
        price_Room = 400
        if internet == 'yes':
            price_Net = 50
        else:
            price_Net = 0
    elif apt_Type == 'B' or apt_Type == 'C':
        if internet == 'yes':
            price_Net = 40
        else:
            price_Net = 0
        if apt_Type == 'B':
            price_Room = 300
        elif apt_Type == 'C':
            price_Room = 500
            
    
    total_Payment = ((price_Room * month) + price_Deposit + price_Net)
    return int(total_Payment), int(price_Deposit)

def total_payment(price_Deposit,price_Rental):
    file_X = open("Funds_collected.txt",'r')
    data = file_X.read().splitlines()
    count = 0
    for x in data:
        count = count + 1
        value = int(x)
        if count == 1:
            total_Deposit = value
        elif count == 2:
            total_Rental = value
        elif count == 3:
            total = int(value)
    file_X.close()
    
    total_Deposit_New = total_Deposit + price_Deposit
    total_Rental_New = total_Rental + price_Rental
    total_New = total_Deposit_New + total_Rental_New
    
    amount = []
    amount.append(total_Deposit_New)
    amount.append(total_Rental_New)
    amount.append(total_New)
    
    file = open("Funds_collected.txt",'w')
    for data_New in amount:
        file.write(str(data_New) + '\n')
    file.close()
    return total, total_Rental


def payment_Update(sattle_Refund):
    file_X = open("Funds_collected.txt",'r')
    data = file_X.read().splitlines()
    count = 0
    for x in data:
        count = count + 1
        value = int(x)
        if count == 1:
            total_Deposit = value
        elif count == 2:
            total_Rental = value
        elif count == 3:
            total = int(value)
    file_X.close()
    
    total_Deposit_New = total_Deposit - 100
    total_Rental_New = ((total_Rental - sattle_Refund) + 100)
    total_New = total_Deposit_New + total_Rental_New
    
    amount = []
    amount.append(total_Deposit_New)
    amount.append(total_Rental_New)
    amount.append(total_New)
    
    file = open("Funds_collected.txt",'w')
    for data_New in amount:
        file.write(str(data_New) + '\n')
    file.close()
    return total
    
def std_Rec(j,apt_Type, apt_Num, room_Num, net, std_Name, tp_Num, pay_Type, amount,r_Type,remain,t_Type,full_Rent):

    file_Handler = open("student_Record.txt",'a')
    k = int(j) + 1
    data_List = []
    data_List.append(k)
    data_List.append(apt_Type)
    data_List.append(apt_Num)
    data_List.append(room_Num)
    data_List.append(net)
    data_List.append(std_Name)
    data_List.append(tp_Num)
    data_List.append(pay_Type)
    data_List.append(amount)
    data_List.append(r_Type)
    data_List.append(remain)
    data_List.append(t_Type)
    data_List.append(full_Rent)
    data_List.append('\n')

    for data in data_List:
        file_Handler.write(str(data))
    file_Handler.close()

def search_Details():
    file = open("student_Record.txt",'r')
    std_Name = str(input("Enter your name:\t")).lower()
    tp_Num = input("Enter your Tp number:\t")
    for line in file:
        line = line.rstrip()
        if not tp_Num in line:
            continue
        print("\n\t*** " + line + " ***")
        
    for line in file:
        line = line.rstrip()
        if not std_Name in line:
            continue
        print("\n\t*** " + line + " ***")

    file.close()


def checkout():
    lines = []
    count = 0
    value = 0
    file = open("student_Record.txt",'r')
    tp_Num = input("Enter your Tp number:\t")
    for line in file:
        line = line.rstrip()
        lines.append(line)
        count = count + 1
        if not tp_Num in line:
            continue
        print("\n\t*** " + line + " ***")
        x = line

    if x[1] == 'A' or x[1] == 'B' or x[1] == 'C':
        value = int(x[0])
    elif x[2] == 'A' or x[2] == 'B' or x[2] == 'C':
        value = int(x[0:2])
    else:
        value = int(x[0:3])

    file_C_O = open("Checkouts.txt",'a')
    file_C_O.write(str(x) + '\n')
    file_C_O.close()

    for i in range(count):
        if lines[i] == x:
            lines[i] = ''
    file_Std_Rec = open("student_Record.txt",'w')
    for data_Update in lines:
        file_Std_Rec.write(str(data_Update) + '\n')
    file_Std_Rec.close()
        
    
    file_R = open("Apartment_Available.txt",'r')
    data_R = file_R.read().splitlines()
    file.close()
    
    data_List_R = []
    for room_Stat in data_R:
        a = int(room_Stat)
        data_List_R.append(a)
            
    if data_List_R[value - 1] == 1:
        data_List_R[value - 1] = 0
    
    file = open("Apartment_Available.txt",'w')
    for data_New in data_List_R:
        file.write(str(data_New) + '\n')
    file.close()

    t_Amount = 0
    r_Amount = 0
    if x[-5] == 'T':
        t_Amount = int(x[-4:-1]) * 10
        if x[-10] == 'R':
            r_Amount = int(x[-9:-6])
        elif x[-9] == 'R':
            r_Amount = int(x[-8:-6])
        elif x[-8] == 'R':
            r_Amonut - int(x[-7:-6])
            
    elif x[-4] == 'T':
        t_Amount = int(x[-3:-1]) * 10
        if x[-8] == 'R':
            r_Amount = int(x[-7:-5])
        elif x[-7] == 'R':
            r_Amonut - int(x[-6:-5])
        elif x[-6] == 'R':
            r_Amonut - int(x[-5:-5])
            
    elif x[-3] == 'T':
        t_Amonut - int(x[-2:-1]) * 10
        if x[-7] == 'R':
            r_Amonut - int(x[-6:-5])
        elif x[-6] == 'R':
            r_Amonut - int(x[-5:-5])
    total_Payed = t_Amount - r_Amount
    months = input("Enter the number of months lived:\t")
    monthly_Rent = t_Amount / 5
    total_Payable = float(monthly_Rent) * float(months)
    sattle_Refund = total_Payable - total_Payed
    sattle = 0
    refund = 0
    if sattle_Refund < 0:
        sattle = payment_Update(int(-1 * sattle_Refund))
        print("you will get ",(-1 * sattle_Refund))
    elif sattle_Refund > 0:
        refund = payment_Update(int(sattle_Refund))
        print("Please pay ", sattle_Refund)
        p_Remain = input("pay:\t")
    else:
        print("No sattle and Refund")
               
menu()
            
