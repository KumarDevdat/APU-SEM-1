#Question of 1,2,3 of 4a is included in this code

def addition(num1,num2):
    sum = int(num1 + num2)
    return sum

def subtract(num1,num2):
    diff = num2 - num1
    if diff < 0:
        diff = (-1 * diff)
    return diff

def multiply(num1,num2):
    mult = num1 * num2
    return mult

def division(num1,num2):
    div = num1 / num2
    return div

def menu_1():
    first_num = int(input("Enter first number "))
    second_num = int(input("Enter second number "))
    while True:
        print ('Enter 1 for sum')
        print ('Enter 2 for differnce')
        print ('Enter 3 for multiplication')
        print ('Enter 4 for division')
        opTion = int(input('Choose the operation from the given options: '))
        if opTion == 1:
            result = addition(first_num,second_num)
            print("sum of first number and second number is ",result)
        elif opTion == 2:
            result = subtract(first_num, second_num)
            print("differnce of first number and second number is ",result)
        elif opTion == 3:
            result = multiply(first_num, second_num)
            print("multiplication of first number and second number is ",result)
        elif opTion == 4:
            result = division(first_num, second_num)
            print("division of first number and second number is ",result)
        else:
            print("Sorry!! you entered the wrong option")
            continue
        break
menu_1()


#Lab 4a question 4

import math
def diameter(f_radius):
    f_dmtr = 2 * f_radius
    return f_dmtr

def circumference(f_radius):
    f_cf = 2 * math.pi * f_radius 
    return f_cf

def area(f_radius):
    f_area = math.pi * f_radius * f_radius
    return f_area

def menu_2():
        while True:
            radius = float(input("Enter the radius of circle "))
            print ("Enter 1 for diameter")
            print ("Enter 2 for area")
            print ("Enter 3 for circumference") 
            choice = int(input("Enter option "))
            if choice == 1:
                dmtr = diameter(radius)
                print("The diameter of circle is ", dmtr)
            elif choice == 2:
                area_c = area(radius)
                print("The area of circle is ", area_c)
            elif choice == 3:
                cf = circumference(radius)
                print("The Cirumference of circle is ", cf)
            else:
                print ("You entered wrong option")
                continue
            break

menu_2()


















































