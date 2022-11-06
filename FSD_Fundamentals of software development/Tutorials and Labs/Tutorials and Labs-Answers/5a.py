
"Code 1"
rows=int(input("Enter Rows\t"))
for x in range(rows):
    if x % 2 == 1:
        print("@" * (x + 1))
    else:
        print("*" * (x + 1))
                
"Code 2"
rows=int(input("Enter Rows\t"))
for x in range(rows):
    if x % 2 == 1:
        print((" " * (rows - x + 1)) and ("*" * (x + 1)))
    else:
        print((" " * (rows - x + 1)) and ("@" * (x + 1)))


