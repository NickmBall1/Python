'''Simple menu to buy coffee
This program uses while loops and finds the total price of coffee
after the customer has finished ordering'''
total = 0
Sqty = 0
Mqty = 0
Lqty = 0
choice = input("Please enter your choice of coffee (S)small, (M)medium, (L)large, (Q)quit: ")
while (choice != 'q'):
       if(choice == 's'):
              Sqty = int(input("How many would you like?"))
              total = total + (Sqty * 1.75)
       elif (choice == 'm'):
              Mqty = int(input("How many would you like?"))
              total = total + (Mqty * 2.75)
       elif (choice == 'l'):
              Lqty = int(input("How many would you like?"))
              total = total + (Lqty * 3.75)
       else:
              print("Illegal size!!")
       choice = input("Please enter your choice of coffee (S)small, (M)medium, (L)large, (Q)quit: ")

#print the total to the user
print("You ordered ", Sqty, " small, ", Mqty, "medium, and", Lqty, "large coffees.")
print("Your total cost is ${0: .2f} {1: .0f}" .format(total, Sqty))
              
