"L5Q1-4"
def flightDeparture():
    schedules = []
    entries = int(input("How many flight detail do you want to enter: "))
    for x in range(entries):
        print("-" * 134)
        sch = []
        flight_Num = input("Enter flight Number: \t")
        sch.append(flight_Num)
        departure = input("Enter flight departure city: \t")
        sch.append(departure)
        departure_Time = input("Enter depature time: \t")
        sch.append(departure_Time)
        arrival = input("Enter flight arrival city: \t")
        sch.append(arrival)
        arrival_Time = input("Enter arrival time: \t")
        sch.append(arrival_Time)
        schedules.append(sch)
        return schedules
        
def flightView():
    view = open("5_Sversion.txt")
    for line in view:
        print("\n\t*** " + line + " ***")
    view.close()

def searchforflight():
    search = open("5_Sversion.txt")
    flight_detail = str(input("Enter flight details to Search for flight: \t"))
    for line in search:
        line = line.rstrip()
        if not flight_detail in line:
            continue
        print("\n\t*** " + line + " ***")
    search.close()
    
def menu():
    while True:
        print("-" * 134)
        print("\t Enter 1 to enter flight timings \n\t Enter 2 to view flight timings \n\t Enter 3 to search for flight details \n\t Enter -1 to exit")
        number = int(input("\nEnter the number: "))
        if number == -1:
            break
        elif number == 1:
            flight_Entry = open("5_Sversion.txt","a")
            flightDeparture_data = str(flightDeparture())
            flight_Entry.write(flightDeparture_data)
            flight_Entry.close()
        elif number == 2:
            flightView()
        elif number == 3:
            searchforflight()
        else:
            print("error /n Enter number again: ")
        continue
menu()


    
