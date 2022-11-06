hostelRecord = {}
Apartmentsb = {}
Apartmentsa = {}
Rooms = {}


# Main Function
def main():

    roomsCounter = 0
    totalDeposit = 0
    amountExcludeDeposit = 0
    amountReceivable = 0
    choice = 'y'
    
    fillApartments()
#    print(Apartmentsa)
#    print(Apartmentsb)

    while(choice == 'y'):
        print("\n-------- Welcome To Hostel Management System --------\n\n")
        print("For Registering a new student to hostel Record press 'a': ")
        print("For Checking Account Information, press 'b': ")
        print("For Performing a Search Over Hostel Record press 'c'")
        
        while(True):
            choice1 = input("\n\nEnter your choice from above given functions: ")
            if(choice1 == 'a' or choice1 == 'b' or choice1 == 'c'):
                break
            else:
                continue
        

    
        if (choice1 == 'a'):
            studentId = registerStudent()
            studentData = allocateRoom(studentId, roomsCounter)

            roomsCounter = roomsCounter + 1

            totalRent = calculateRent(studentData)
            
            print(f"your total rent is {totalRent}")

            paymentRemaining, paid = payRent(totalRent)

            studentData.append(paymentRemaining)

            hostelRecord[studentId] = studentData

            totalDeposit += 100

            amountExcludeDeposit += (paid-100)

            amountReceivable += paymentRemaining
            
            print("\n\n")
            print(hostelRecord)

            f = open("hostelRecord.txt", "w+")

            for student in hostelRecord:
                data = hostelRecord[student]
                datai = ['Name: ', 'Apartment Type: ', 'Internet Subscribed: ', 'Room Type: ', 'Apartment No: ', 'Room No: ']
                print()
                for i in range(6):
                    f.write(f"{datai[i]} {data[i]}\n")
                f.write("\n")
                print()

            f.close()
            

            while(True):
                choice = input("Do you want to Continue Using Hostel Management System(y/n): ")
                if(choice == 'y' or choice == 'n'):
                    break
                else:
                    continue
            
        if(choice1 == 'b'):
            print("\n-------------  Accounts Information  -------------")
            print("For printing total deposit collected press 1: ")
            print("For printing total amount collected excluding deposit press 2: ")
            print("For printing total amount receivable press 3: ")

            print()
            printChoice = int(input("What do you want to print: "))

            if(printChoice == 1):
                print(f"The total Deposit Collected = {totalDeposit}")
                while(True):
                    choice = input("Do you want to Continue Using Hostel Management System(y/n): ")
                    if(choice == 'y' or choice == 'n'):
                        break
                    else:
                        continue

                
            elif(printChoice == 2):
                print(f"The total amount Collected excluding deposit = {amountExcludeDeposit}")
                while(True):
                    choice = input("Do you want to Continue Using Hostel Management System(y/n): ")
                    if(choice == 'y' or choice == 'n'):
                        break
                    else:
                        continue

            elif(printChoice == 3):
                print(f"The total amount Receivable = {amountReceivable}")
                while(True):
                    choice = input("Do you want to Continue Using Hostel Management System(y/n): ")
                    if(choice == 'y' or choice == 'n'):
                        break
                    else:
                        continue

            else:
                print("Invalid Input")
                while(True):
                    choice = input("Do you want to Continue Using Hostel Management System(y/n): ")
                    if(choice == 'y' or choice == 'n'):
                        break
                    else:
                        continue

        
        if(choice1 == 'c'):
            print("\n-------------  Search Options  -------------")
            print("For searching by studentId press 1: ")
            print("For searching by Apartment Type press 2: ")
            print("For searching by Apartment No press 3: ")
            print("For searching by Room No press 4: ")
            
            print()
            printChoice = int(input("What do you want to search by: "))

            if(printChoice == 1):
                sid = input("Enter the id of student you want to search")
                searchById(sid)
                while(True):
                    choice = input("Do you want to Continue Using Hostel Management System(y/n): ")
                    if(choice == 'y' or choice == 'n'):
                        break
                    else:
                        continue
            elif(printChoice == 2):
                while(True):
                    at = input(f"Please Enter your Apartment Type(a/b): ")
                    if(at == 'a' or at == 'b'):
                        break
                    else:
                        continue
                        
                searchByApartmentType(at)
                while(True):
                    choice = input("Do you want to Continue Using Hostel Management System(y/n): ")
                    if(choice == 'y' or choice == 'n'):
                        break
                    else:
                        continue
            elif(printChoice == 3):
                while(True):
                    an = int(input(f"Please Enter your Apartment No(1 to 40): "))
                    if(an > 0 and an < 41):
                        break
                    else:
                        continue

                searchByApartmentNo(an)
                while(True):
                    choice = input("Do you want to Continue Using Hostel Management System(y/n): ")
                    if(choice == 'y' or choice == 'n'):
                        break
                    else:
                        continue
            elif(printChoice == 4):
                
                while(True):
                    rn = int(input("Enter the Room No you want to search(0 to 99): "))
                    if(rn >= 0 and rn < 100):
                        break
                    else:
                        continue
                    
                searchByRoomNo(rn)
                while(True):
                    choice = input("Do you want to Continue Using Hostel Management System(y/n): ")
                    if(choice == 'y' or choice == 'n'):
                        break
                    else:
                        continue


    
    
    
# My Functions
def fillApartments():
    for i in range(20):
        Apartmentsa[i+1] = []
        Apartmentsb[i+21] = []
        
    

def registerStudent():
    studentId = input("Please Enter your Unique Id for Registeration: ")
    hostelRecord[studentId] = ['Empty']

    print("Student is Registered in Hostel Records")
    print(f"Student's Hostel Record is {hostelRecord}");
    return studentId

def allocateRoom(studentId, roomsCounter):
    studentData = []

    studentName = input(f"Please Enter your Name: ")
    studentData.append(studentName.lower())
        
    while(True):
        apartmentType = input(f"Please Enter your Apartment Type(a/b): ")
        if(apartmentType == 'a' or apartmentType == 'b'):
            studentData.append(apartmentType.lower())
            break
        else:
            continue
    

    while(True):
        internetChoice = input(f"Please Enter if you want subscription of internet(yes/no)")
        if(internetChoice == 'yes' or internetChoice == 'no'):
            studentData.append(internetChoice.lower())
            break
        else:
            continue




    if(studentData[1] == 'b'):
        while(True):
            roomType = input(f"Please Enter your Room Type(single/master): ")
            if(roomType == 'single' or roomType == 'master'):
                studentData.append(roomType.lower())
                break
            else:
                continue

        while(True):
            apartmentNo = int(input(f"We have total 20 Apartments in {studentData[1]} Category, select your apartment(21 to 40): "))
            if(apartmentNo > 20 and apartmentNo < 41):
                break
            else:
                continue
 
        
        roomsList = Apartmentsb[apartmentNo]
    # Checking For Single Room in selected appartment
        if(roomType == 'single'):
            count = 0
            for room in roomsList:
                if(room == 'single'):
                    count += 1

            if(count < 2):
                Apartmentsb[apartmentNo].append('single')
                studentData.append(apartmentNo)
    # if selected apartment dont have the room, checking next available room 
            else:
                for apartment in Apartmentsb:
                    count = 0
                    roomsList = Apartmentsb[apartment]
                    for room in roomsList:
                        if(room == 'single'):
                            count += 1

                    if(count < 2):
                        Apartmentsb[apartment].append('single')
                        studentData.append(apartment)
                        print("your selected apartment has no single room left")
                        print(f"Alocating you room in Apartment No {apartment}")
                        break


    # Checking For Single Room in selected appartment
        if(roomType == 'master'):
            count = 0
            for room in roomsList:
                if(room == 'master'):
                    count += 1

            if(count < 1):
                Apartmentsb[apartmentNo].append('master')
                studentData.append(apartmentNo)
    # if selected apartment dont have the room, checking next available room 
            else:
                for apartment in Apartmentsb:
                    count = 0
                    roomsList = Apartmentsb[apartment]
                    for room in roomsList:
                        if(room == 'master'):
                            count += 1

                    if(count < 1):
                        Apartmentsb[apartment].append('master')
                        studentData.append(apartment)
                        print("your selected apartment has no master room left")
                        print(f"Alocating you room in Apartment No {apartment}")
                        break



    elif(studentData[1] == 'a'):
        roomType = 'single'
        studentData.append(roomType)


        while(True):
            apartmentNo = int(input(f"We have total 20 Apartments in {studentData[1]} Category, select your apartment(1 to 20): "))
            if(apartmentNo > 0 and apartmentNo < 21):
                studentData.append(roomType.lower())
                break
            else:
                continue

        roomsList = Apartmentsa[apartmentNo]
        # Checking For Single Room in selected appartment
        if(roomType == 'single'):
            count = 0
            for room in roomsList:
                if(room == 'single'):
                    count += 1

            if(count < 2):
                Apartmentsa[apartmentNo].append('single')
                studentData.append(apartmentNo)
    # if selected apartment dont have the room, checking next available room 
            else:
                for apartment in Apartmentsa:
                    count = 0
                    roomsList = Apartmentsa[apartment]
                    for room in roomsList:
                        if(room == 'single'):
                            count += 1

                    if(count < 2):
                        Apartmentsa[apartment].append('single')
                        studentData.append(apartment)
                        print("your selected apartment has no single room left")
                        print(f"Alocating you room in Apartment No {apartment}")
                        break

    roomNo = roomsCounter
    Rooms[roomNo] = studentId
    studentData.append(roomNo)

#    hostelRecord[studentId] = studentData

#    print(f"StudentData: {studentData}")        
#    print()
 #   print(f"hostelRecord: {hostelRecord}")
  #  print()
#    print(f"Apartments B: {Apartmentsb}")
 #   print(f"Apartments A: {Apartmentsa}")
  #  print()
  #  print(f"Rooms : {Rooms}")
    
    
    return studentData

# Function To Calculate Rent
def calculateRent(studentData):

    monthlyRental = 0
    internetCharges = 0
    deposit = 100

    if(studentData[1] == 'a'):
        monthlyRental = 400
        if(studentData[2] == 'yes'):
            internetCharges = 50
    else:
        if(studentData[3] == 'master'):
            monthlyRental = 500
        else:
            monthlyRental = 300

        if(studentData[2] == 'yes'):
                internetCharges = 40

    totalRent = monthlyRental + internetCharges + deposit
                
    return totalRent        

# Function to Ask for Payment from Student
def payRent(totalRent):
    paid = 0
    paymentRemaining = 0
    mustPay = ((totalRent - 100)//2) + 100 

    while(True):
        choice = input("Do you want to pay 'full' or 'partial': ")
        if(choice == 'full' or choice == 'partial'):
            break
        else:
            continue

    if(choice == 'full'):
        paymentRemaining = 0
        paid = totalRent
    elif(choice == 'partial'):
        while(True):
            paid = int(input(f"Enter Amount you want to pay out of above {mustPay}: "))
            if(paid < mustPay or paid > totalRent):
                continue
            else:
                paymentRemaining = totalRent - paid
                break
        
    return paymentRemaining, paid
 
# Function to search students by id
def searchById(sid):

    for student in hostelRecord:
        if(student != sid):
            continue
        else:
            data = hostelRecord[sid]
            datai = ['Name: ', 'Apartment Type: ', 'Internet Subscribed: ', 'Room Type: ', 'Apartment No: ', 'Room No: ']
            print()
            for i in range(6):
                print(f"{datai[i]} {data[i]}")
            print()
    print()
    return

# Function to search students by apartment Type
def searchByApartmentType(at):

    slist = []
    
    for student in hostelRecord:
        if(hostelRecord[student][1] == at):
            slist.append(hostelRecord[student][0])
    
    print(f"\nStudents in Apartment type {at}\n")
    for student in slist:
        print(student)        
    print()
    return

# Function to search students by apartment No
def searchByApartmentNo(an):

    slist = []
    
    for student in hostelRecord:
        if(hostelRecord[student][4] == an):
            slist.append(hostelRecord[student][0])
    
    print(f"\nStudents in Apartment No {an}\n")
    for student in slist:
        print(student)        
    print()

    return

# Function to search students by room no
def searchByRoomNo(rn):

    slist = []
    
    for student in hostelRecord:
        if(hostelRecord[student][5] == rn):
            slist.append(hostelRecord[student][0])
    
    print(f"\nStudents in Room No {rn}\n")
    for student in slist:
        print(student)        
    print()

    return



# Calling Main
main()



print ("Thank you for using Our Hostel Management System")
