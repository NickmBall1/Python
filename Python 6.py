Evenlist=[]
Oddlist=[]

n = int(input("What do you want the value of n to be?"))
m = int(input("What do you want the value of m to be?"))
#insures that n and m are correct
if n > m:
    print("n was greater than m, please try again")
    n = int(input("What do you want the value of n to be?"))
    m = int(input("What do you want the value of m to be?"))
for x in range(n, m):
    if x % 2 == 0:
        Evenlist.append(x)
        #print('Even list', Evenlist)
    else:
        Oddlist.append(x)
        #print("Odd list", Oddlist)
sumodd = sum(Oddlist)
sumeven = sum(Evenlist)
print("The sum of the odds is", sumodd)
print("The sum of the evens is", sumeven)
