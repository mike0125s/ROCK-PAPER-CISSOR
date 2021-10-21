import random
def gameWin(Comp,you):
    if Comp==you:
        return None
    elif Comp=='s':
        if you == 'p':
            return True
        elif you == 'c':
            return False
    elif Comp=='p':
        if you == 'c':
            return True
        elif you == 's':
            return False
    elif Comp=='c':
        if you == 's':
            return True
        elif you == 'p':
            return False                





print("Comp Turn: Stone(s) Paper(p) Cissor(c)? ")
randno = random.randint(1,3)
if randno==1:
    Comp = 's'
elif randno==2:
    Comp = 'p'
elif randno==3:
    Comp = 'c'

you =    input("Your Turn: Stone(s) Paper(p) Cissor(c)? ")  
a=gameWin(Comp,you)       
if a ==None:
    print("Game has Tie")
elif a:
    print("You win!!")
else:
    print("Game Over!")        
