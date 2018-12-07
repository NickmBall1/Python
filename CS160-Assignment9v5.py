
myNames = ["Ruby","Weiss","Blake","Yang","Juane","Pyrrha","Ren","Nora"]
myNumbers = [12, 23, 34, 45, 56, 67, 78, 42]


def num_there(s):
    return any(i.isdigit() for i in s)


def init():
    student = input("Student: ")
    if student =='q':
        raise SystemExit

    if student.istitle() is False:

        print("Please try again\nProgram will fail if name is not capitalize, if numbers are present,")
        del student
        init()




    while student!='q':
        for x in range(0, 8):
                if myNames[x] == student:
                    print(myNames[x], "'s test score is", myNumbers[x])

                    del student
                    init()

        print("The student you have entered does not go to this academy")
        error=input("Would you like to try again?Y/N")
        if error in ["y", "Y"]:
            init()
        elif error in ["n", "N"]:
            print("Have a good day")
            raise SystemExit


def endCheck():
    check=input("Are you sure you would like to quit?Y/N")
    if check in ["y","Y"]:
        print("Have a good day")
        raise SystemExit
    elif check in ["n","N"]:
       init()


init()
              

