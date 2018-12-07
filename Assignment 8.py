import math

sums=[]
def endCheck():
    check=input("Is there anything else I can do for you?Y/N")
    if check in ["y","Y"]:
        intialinput()

    elif check in ["n","N"]:
        print("Have a good day")
        raise SystemExit
def intialinput():


    num=input('Please input a number')
    sums.append(num)
    test=int(num)
    while test != 0:
        intialinput()

    else:
        sumt=[int(numeric_string) for numeric_string in sums]
        print(math.fsum(sumt))
        test == 0
        del sums[:]
        del sumt[:]
        endCheck()

intialinput()
