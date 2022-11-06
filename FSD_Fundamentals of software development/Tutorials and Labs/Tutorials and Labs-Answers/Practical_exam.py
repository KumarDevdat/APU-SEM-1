def getDailySales():
    sales = []
    amount = float(input("Enter sales for first item or <enter -1 to End>:\t")
    while (amount != -1):
        sales.append(amount)
        amount = float(input("Enter sales for next item\t")
    return sales

def totalDailySales(sales):
    total = 0
    for item in sales
        total = total + item
    return total

def avgDailySales(sales):
    total = totalDailySales(sales)
    average = total / len(sales)
    return average

def avgWeeklySales(getDailySales):
    for days in range(7):
        print ("Find averge sales of the day ", days)
        sales = getDailySales()
        average = avgDailySales(sales)
        fhand.write(str(average) + '\n')
        

    
