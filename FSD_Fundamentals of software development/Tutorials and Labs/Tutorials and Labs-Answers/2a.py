print ('Q1')
x = int(input('Enter selling price'))
y = int(input('Enter buying price'))
z = x - y
if z >=0:
    print('Profit is ', z)
else:
    print('Loss is ', z*-1)

print('Q2')
Student_Name = str(input('Enter name of student'))
Student_Marks = int(input('Enter Number of student'))
if Student_Marks >= 60:
    print (Student_Name, ' has passed the module')
else:
    print (Student_Name, ' has failed the module')

print('Q3')    
Student_Name = str(input('Enter name of student'))
Student_Marks = int(input('Enter Number of student'))
if Student_Marks < 0 and Student_Marks > 100:
    print (Student_Name, 'Invalid Entry')
elif    Student_Marks <= 100 and Student_Marks >= 80:
    print (Student_Name, 'Your Grade is A')
elif    Student_Marks <= 79 and Student_Marks >= 70:
    print (Student_Name, 'Your Grade is B')
elif    Student_Marks <= 69 and Student_Marks >= 60:
    print (Student_Name, 'Your Grade is C')
elif    Student_Marks <= 59 and Student_Marks >= 50:
    print (Student_Name, 'Your Grade is D')
else:
    print (Student_Name, 'Your Grade is F')
