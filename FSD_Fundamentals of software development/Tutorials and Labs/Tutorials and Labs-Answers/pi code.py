pi = 0.0
n = int(input('Enter n term: '))
for i in range(1,n+1):
    if i % 2 == 0:
        pi = pi - (4/(2 * i - 1))
    else:
        pi = pi + (4/(2 * i - 1))

print(pi)

        
