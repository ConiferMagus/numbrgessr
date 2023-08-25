
import random

class Num:
    num_to_ges = 0

class User:
    usr_ges = 0
    win = 0

def error(funct):
    print("\nSorry! I didn't get that.\n")
    funct()

def get_num():
    Num.num_to_ges = random.randint(1,20)

def num_reset():
    Num.num_to_ges = 0

def usr_reset():
    User.usr_ges = 0

def get_usr():
    print("\nSelect your number below:")
    choice = input(">>  ")
    if int(choice.isdigit()):
        User.usr_ges = int(choice)
    else:
        error(get_usr)

def logic():
    if User.usr_ges > Num.num_to_ges:
        print("\nThe number to guess is lower.")
        usr_reset()
    elif User.usr_ges < Num.num_to_ges:
        print("\nThe number to guess is higher.")
        usr_reset()
    else: 
        print("\nYou win!")
        User.win = 1

def again():
    affirm = ['y', 'ye', 'yes']
    neg = ['n', 'no']
    choice = input("\nWould you like to play again? (Y/N)\n>>  ")
    if choice.lower() in affirm:
        num_reset()
        User.win = 0
        game()
    elif choice.lower() in neg:
        print("\nThanks for playing!")
    else: error(again)

#GAME
def game():
    get_num()
    for item in range(5):
        if User.win == 0:
            get_usr()
            logic()
    again()

game()
    
    
    
    
    