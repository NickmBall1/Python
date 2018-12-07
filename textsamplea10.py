'''How to read a number (8 digits for this example) from the user and print the sum of the digits
We will add some funtions to do this.
We will also split the string into 2 pieces with 4 numbers in this example
This is a sample program for Assignment 9'''
#function to read a number


def readNum():
       num = input("Please enter an 32 digit number and I will split it, and convert it: ")
       return num

#function to check to make sure you have 8 digits


def checkNum(num):
       while len(num) != 32:
              flag = 'error'
              return flag
       else:
              flag = 'true'
              return flag


#function to split the number into 2 strings


def splitNum(num):
       first = num[0:8]
       second = num[8:16]
       third = num[16:24]
       fourth = num[24:32]
       return [first, second, third, fourth]


#function to check to see if they are all numbers and calculate sum


#main function
def converter(num):
    import sys

    first = num[0:8]
    second = num[8:16]
    third = num[16:24]
    fourth = num[24:32]
    print(first)
    f1 = -1
    f2=-1
    f3=-1
    f4=-1
    check = 0
    word1 = []
    word2 = []
    word3 = []
    word4 = []
    #seperates each character
    for x in first:
        word1.append(x)
    #checks to see if 1 or 0
    for c in word1:
        if c == "1":
            check += 1
        elif c == "0":
            check += 1
        else:
            print("Something is not quite right")
            print(check)
            sys.exit(0)
    #checks the length
    if check != 8:
        print("Something is not quite right")
        sys.exit(0)
    #reverse order of list to allow for formula to work
    word1.reverse()
    #makes new array to convert the list of strings to a list of integers
    sword1 = [int(numeric_string) for numeric_string in word1]
    #applies formula
    for t in sword1:
        f1 = f1 + 1
        if t == 1:
            sword1.insert(f1, (2 ** f1))
            sword1.remove(t)
    check=0
    #sums up
    one = sum(sword1)

    # seperates each character
    for x in second:
        word2.append(x)
    # checks to see if 1 or 0
    for c in word2:
        if c == "1":
            check += 1
        elif c == "0":
            check += 1
        else:
            print("Something is not quite right")
            print(check)
            sys.exit(0)
    # checks the length
    if check != 8:
        print("Something is not quite right")
        sys.exit(0)
    # reverse order of list to allow for formula to work
    word2.reverse()
    # makes new array to convert the list of strings to a list of integers
    sword2 = [int(numeric_string) for numeric_string in word2]
    # applies formula
    for t in sword2:
        f2 = f2 + 1
        if t == 1:
            sword2.insert(f2, (2 ** f2))
            sword2.remove(t)
    check=0
    # sums up
    two = sum(sword2)

    # seperates each character
    for x in third:
        word3.append(x)
    # checks to see if 1 or 0
    for c in word3:
        if c == "1":
            check += 1
        elif c == "0":
            check += 1
        else:
            print("Something is not quite right")
            print(check)
            sys.exit(0)
    # checks the length
    if check != 8:
        print("Something is not quite right")
        sys.exit(0)
    # reverse order of list to allow for formula to work
    word3.reverse()
    # makes new array to convert the list of strings to a list of integers
    sword3 = [int(numeric_string) for numeric_string in word3]
    # applies formula
    for t in sword3:
        f3 = f3 + 1
        if t == 1:
            sword3.insert(f3, (2 ** f3))
            sword3.remove(t)
    check=0
    # sums up
    three = sum(sword3)

    # seperates each character
    for x in fourth:
        word4.append(x)
    # checks to see if 1 or 0
    for c in word4:
        if c == "1":
            check += 1
        elif c == "0":
            check += 1
        else:
            print("Something is not quite right")
            print(check)
            sys.exit(0)
    # checks the length
    if check != 8:
        print("Something is not quite right")
        sys.exit(0)
    # reverse order of list to allow for formula to work
    word4.reverse()
    # makes new array to convert the list of strings to a list of integers
    sword4 = [int(numeric_string) for numeric_string in word4]
    # applies formula
    for t in sword4:
        f4 = f4 + 1
        if t == 1:
            sword4.insert(f4, (2 ** f4))
            sword4.remove(t)
    check=0
    # sums up
    four = sum(sword4)

    print("Your ip address is ", one, ".", two, ".", three, ".", four, ".")


def main():
       flag = 'true'

       num = readNum()
       flag = checkNum(num)
       if flag =='true':
           converter(num)
       else:
              print("Not a valid 32 digit number!!")

#call main
main()



