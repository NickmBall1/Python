
myNames = ["Ruby", "Weiss", "Blake", "Yang", "Juane", "Pyrrha", "Ren", "Nora"]
myNumbers = [12, 23, 34, 45, 56, 67, 78, 42]


def num_there(s):
    return any(i.isdigit() for i in s)


def init():
    student = input("Student: ")

    if student.istitle() is False:

        print("Please capitalize students name")
        del student
        init()

    if num_there(student) is True:
        print("Numbers do not belong in names!!!")
        del student
        init()

    while student!='q':
        for x in range(8):
                if myNames[x] == student:
                    print(myNames[x], "'s test score is", myNumbers[x])
                    del student
                    init()
                else:
                    print("The student you have entered does not go to this academy")
                    error=input("Would you like to try again?Y/N")
                    if error in ["y", "Y"]:
                        init()
                    elif error in ["n", "N"]:
                        print("Have a good day")
                        raise SystemExit

    if student == 'q':
        endCheck()


def endCheck():
    check=input("Are you sure you would like to quit?Y/N")
    if check in ["y","Y"]:
        init()
    elif check in ["n","N"]:
        print("Have a good day")
        raise SystemExit


init()
              

