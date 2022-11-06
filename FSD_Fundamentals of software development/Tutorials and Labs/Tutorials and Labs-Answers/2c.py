'''
print("L2CQ1")
for x in range(0,15):
    f_temp = int(input("Enter temperature in Fahrenheit\n"))
    c_temp = float((f_temp - 32) * 5 / 9)
    print ("Temperature in Celsius is ",c_temp)
print("All tempertures have processed")
'''
'''
print ("L2CQ2")
counter = 0
total = 0
marks  = 0
name = input("Enter the name of student ")
marks = int(input("Enter the marks of a Student between 0 to 100 and to end enter 999 "))
while marks >= 0 and marks <= 100:
    total = total + marks
    counter = counter + 1
    name = input("Enter the name of student ") 
    marks = int(input("Enter the marks of a Student between 0 to 100 and to end enter 999 "))
if counter > 0:    
    avg = total / counter
else:
    print ("number of students are 0 so avg is ")
print("the average of clss is ", avg)
'''         
'''
print ("L2CQ2")

while True:
    assign_marks = int(input("Enter assignment marks "))
    if assign_marks < 25:
        print("your assignment marks are less than 25, plese redo assignment")
        continue
    test_marks = int(input("Enter test marks "))
    if test_marks < 25:
        print("your test marks are less than 25, plese redo test")
        continue
    exam_marks = int(input("Enter Exam marks "))
    if exam_marks < 50:
        print("your exam marks are less than 50, plese redo exam")
        continue
    print("You have passed the module")
    break
'''























