import sys
import math
enter=input("Enter 8 binary digits")
f=-1
check=0
word=[]
sums=0
int(enter)



for x in enter :
    word.append(x)

for c in word:
    if c =="1":

        check+=1
    elif c=="0":

        check+=1
    else:
        print("Something is not quite right")
        print(check)
        sys.exit(0)

if check!=8:
    print("Something is not quite right")
    sys.exit(0)
word.reverse()

sword = [int(numeric_string) for numeric_string in word]
for t in sword:
    f=f+1
    if t==1:
        sword.insert(f,(2**f))
        sword.remove(t)

print("Your decimal number is " )
print(math.fsum(sword))
