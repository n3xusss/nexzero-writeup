import pickle
import pickletools

class normal_character():
    def __init__(self,hp,attack,defence):
        self.hp=hp
        self.attack=attack
        self.defence=defence
    def __str__(self):
        return f'the character hp is {self.hp} , attack is {self.attack} , defence is {self.defence}'

class admin_character():
    def __str__(self):
        return open('flag.txt','r').read()

print('welcome to character generator : ')
print('choose option : ')
print('[1] Generate')
print('[2] Load')
print('[3] Exit')
choice = input('>> ')
if choice.strip() not in ['1','2','3']:
    print('invalid option , exiting ....')
    exit(0)
elif int(choice)==3:
    exit(0)
elif int(choice)==1:
    hp = input('what is the character HP ? : ')
    attack = input('what is the character attack points ? : ')
    defence = input('what is the character defence points ? : ')
    character = normal_character(hp,attack,defence)
    print(str(character))
    print("here is the loadable data , so you can import it : "+str(pickle.dumps(character).hex()))
elif int(choice)==2:
    print('enter the loadable payload : ')
    load = bytes.fromhex(input('>> '))
    
    if b'__reduce__' in load:
       print('illegal...')
       exit(0)
    character=pickle.loads(load)
    if hasattr(character,'hp') and hasattr(character,'defence') and hasattr(character,'attack'):
            try:
                print(str(character))
            except:
                print('invalide payload!')
    else:
        print('missing attribute => invalide payload')