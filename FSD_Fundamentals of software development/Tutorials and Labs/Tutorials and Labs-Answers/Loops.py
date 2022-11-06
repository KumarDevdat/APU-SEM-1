print('Welcome to student registration system\n')
sum = 0
counter = 1 
while counter < 6:
    num = float(input('\tEnter number: '))
    sum = sum + num
    counter= counter +1
    print('\n')
avg = sum /5
print('\nAvegrage of five numbers is: ',avg, '\n')

print('Welcome to student registration system\n')
sum = 0
for counter in range(5):
    num = float(input('\tEnter number: '))
    sum = sum + num
    print('\n')
avg = sum /5
print('\nAvegrage of five numbers is: ',avg)
print('\n')
print('\tThankyou')
