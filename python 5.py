import random
bn=0
gn=0
bad=0
gad=0
choice = input("Boy (b), Girl (g) or Quit (q): ")
while (choice!='q'):
    if choice== 'b' :
        b=random.randint(1,40)
        bn+=1
        bad+=b

        print("Boy score:" ,b)
        
        choice = input("Boy (b), Girl (g) or Quit (q): ")
    elif choice=='g' :
        g=random.randint(1,40)
        gn+=1
        gad+=g
        print("Girl score:",g)
        choice = input("Boy (b), Girl (g) or Quit (q): ")

else:
    ba=bad/bn
    ga=gad/gn

    print("Boy Average is: ",ba)
    print("Girl Average is:",ga)
