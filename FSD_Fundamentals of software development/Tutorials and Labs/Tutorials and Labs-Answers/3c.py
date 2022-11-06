firstList = ['Football', 'Tennis', 'Rugby']
secondList = ['Squash','Netball','Cricket', 'Volleyball']

firstList.extend(secondList)

length = len(firstList)
print(length)
games = ['Football', 'Tennis', 'Netball', 'Cricket', 'Volleyball']
maximum = max(games)
print(maximum)
games = ['Football', 'Tennis', 'Netball', 'Cricket', 'Volleyball']
minimum = min(games)
print(minimum)
games = ['Football', 'Tennis', 'Netball', 'Cricket', 'Volleyball']
total = sum(games)
print(total)

marks = [67, 56, 90, 55, 84]
total = sum(marks)
print(total)

marks = [67, 56, 90, 55, 84]
average = sum(marks)/len(marks)
print(average)

marks = [67, 56, 'fifty']
minimum = min(marks)
print(minimum)

members = ['John','Kathy','Mary','Gerard']
name = input("Enter a name to search for ")
for member in members:
    if member==name:
        print('Yes!', name, 'is a member.')
        
members = ['John','Kathy','Mary','Gerard']
name = input("Enter a name to search for ")
for member in members:
    if member.lower()==name.lower():
        print('Yes!', name, 'is a member.')  

members = ['John','Kathy','Mary','Gerard']
name = input("Enter a name to search for ")
for member in members:
    if member.lower()==name.lower():
        print('Yes!', member, 'is a member.')  

members = ['John','Kathy','Mary','Gerard', 'Mary']
numberOfOccurance = members.count('John')
print(numberOfOccurance)

members = ['John','Kathy','Mary','Gerard', 'Mary']
numberOfOccurance = members.count('Mary')
print(numberOfOccurance)

guests = []
name = input('Please provide the guest\'s name: ')
guests.append(name)
print(guests)

guests = []
for i in range(5):
    name = input('Please provide the guest\'s name: ')
    guests.append(name)
for guest in guests:
    print(guest)
   
guests = []
for i in range(5):
    name = input('Please provide the guest\'s name: ')
    guests.append(name)
print()
print()
for guest in guests:
    print(guest)

guests = []
while True:
    name = input('Enter guest\'s name (<enter> to end): ')
    if name=="":
        break
    else:
        name=name.capitalize()
        guests.append(name)

for guest in guests:
    print(guest)
    
items = list(range(10))
for item in items:
    print(item)

items = list(range(5,10))
for item in items:
    print(item)
    
items = list(range(5))
print(items[0:5])

items = list(range(5))
print(items[2:4])


