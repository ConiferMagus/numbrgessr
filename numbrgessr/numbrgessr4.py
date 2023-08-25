
import random

class Num:
    num_to_ges = 0

class User:
    usr_ges = 0
    win = 0
    diff = 0
    tries = 0
    wins = 0

def error(funct):
    print("\nSorry! I didn't get that.\n")
    funct()
    
def get_diff():
    print("\nChoose your difficulty below: ")
    ind = 1
    lst = ['Easy (1-20)', 'Medium (1-50)', 'Hard (1-100)']
    for item in lst:
        print('[{}]. {}'.format(ind, lst[ind-1]))
        ind+=1
    choice = input("\n>>  ")
    if choice == str(1) or choice.lower() == 'easy':
        User.diff = 1
    elif choice == str(2) or choice.lower() == "medium":
        User.diff = 2
    elif choice == str(3) or choice.lower() == "hard":
        User.diff = 3
    else: error(get_diff)

def get_num():
    if User.diff == 1:
        Num.num_to_ges = random.randint(1,20)
    elif User.diff == 2:
        Num.num_to_ges = random.randint(1,50)
    elif User.diff == 3:
        Num.num_to_ges = random.randint(1,100)

def num_reset():
    Num.num_to_ges = 0

def usr_reset():
    User.usr_ges = 0

def diff_reset():
    User.diff = 0

def get_usr():
    print("\nEnter your number below:")
    choice = input(">>  ")
    if int(choice.isdigit()):
        User.usr_ges = int(choice)
    else:
        error(get_usr)

def logic():
    if User.usr_ges > Num.num_to_ges:
        print("\nThe number to guess is lower.")
        usr_reset()
        if User.tries == 4:
            print("\nYou lose :(")
            print("The correct number was: {}".format(Num.num_to_ges))
        elif User.tries == 3:
            print("\nLast Attempt!")
    elif User.usr_ges < Num.num_to_ges:
        print("\nThe number to guess is higher.")
        usr_reset()
        if User.tries == 4:
            print("\nYou lose :(")
            print("The correct number was: {}".format(Num.num_to_ges))
        elif User.tries == 3:
            print("\nLast Attempt!")
    else: 
        print("\nYou win!")
        User.win = 1
        User.tries = 0
        User.wins += 1

def again():
    affirm = ['y', 'ye', 'yes']
    neg = ['n', 'no']
    choice = input("\nWould you like to play again? (Y/N)\n>>  ")
    if choice.lower() in affirm:
        num_reset()
        User.win = 0
        User.tries = 0
        game()
    elif choice.lower() in neg:
        print("\nThanks for playing!")
        print("\nYour high score is: {}.".format(User.wins))
    else: error(again)

#GAME
def game():
    get_diff()
    get_num()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nYou have won {} times.".format(User.wins))
    for item in range(5):
        if User.win == 0:
            get_usr()
            logic()
            User.tries += 1
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
    again()   