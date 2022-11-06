"L5Q1-4"
def flightDeparture():
    file = open ("5.txt","a")
    entries = int(input("How many flight detail do you want to enter: "))
    for x in range(entries):
        print("-" * 134)
        flight_Num = input("Enter flight Number: \t")
        departure = input("Enter flight departure city: \t")
        departure_Time = input("Enter depature time: \t")
        arrival = input("Enter flight arrival city: \t")
        arrival_Time = input("Enter arrival time: \t")
        file.write(departure + "\t" + departure_Time + "\t" + arrival + "\t" + arrival_Time + "\n")
    file.close()
    
def flightView():
    file = open("5.txt")
    for line in file:
        print(line)
    file.close()

def searchforflight():
    file = open("5.txt")
    flight_detail = str(input("Enter flight details to Search for flight: \t"))
    for line in file:
        line1 = line.rstrip()
        if flight_detail in line1:
            print("\n\t*** " + line1 + " ***")
    file.close()
    
def menu():
    while True:
        print("-" * 134)
        print("\t Enter 1 to enter flight timings \n\t Enter 2 to view flight timings \n\t Enter 3 to search for flight details \n\t Enter -1 to exit")
        number = int(input("\nEnter the number: "))
        if number == -1:
            break
        elif number == 1:
            flightDeparture()
        elif number == 2:
            flightView()
        elif number == 3:
            searchforflight()
        else:
            print("error \n Enter number again: ")
        continue
menu()


    
