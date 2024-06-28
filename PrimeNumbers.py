n = int(input())
results = []

for x in range (n):
    b = 0
    number = int(input())
    for y in range(1,number+1):
        if (number%y == 0):
            b+=1
    if (b==2):
        results.append("TAK")
    else: 
        results.append("NIE")

for a in results:
    print(a)
