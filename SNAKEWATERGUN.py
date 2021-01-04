
import random
def game(comp,you):
    if comp==you:
        return None 
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True
print("computer Turn: Snake(s) Water(w) or Gun(g)?")
randno= random.randint(1,3) 
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
elif randno == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
print(f'you chose {you}')
print(f'computer chose {comp}')
a=game(comp,you)
if a== None:
    print('THE GAME IS TIE')
elif a:
    print('YOU WIN')
else:
    print('YOU LOSE ')
