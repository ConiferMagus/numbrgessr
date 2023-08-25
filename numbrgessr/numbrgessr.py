
import random

class Num:
    num_to_ges = 0

class User:
    user_name = ""
    num = 0
    win = 0
    diff = 0

def get_num_ez():
    Num.num_to_ges = random.randint(1,20)

def get_num_med():
    Num.num_to_ges = random.randint(1,50)

def get_num_hard():
    Num.num_to_ges = random.randint(1,100)

def reset_game():
    Num.num_to_ges = 0

def reset_user():
    User.num = 0

def get_user():
    choice = input("\nSelect a number:\n>>  ")
    User.num = int(choice)
    
def chekr():
    if User.num == Num.num_to_ges:
        print("\nYou win!")
        User.win = 1
    elif User.num > Num.num_to_ges:
        print("\nThe correct number is lower.")
        reset_user()
    elif User.num < Num.num_to_ges:
        print("\nThe correct number is higher.")
        reset_user()
    else: pass

def repeater():
    get_user()
    chekr()
    
def game():
    
    print("Welcome to the Number Guesser.")
    
    def dif_select():
    
        dif_list = ["Easy", "Medium", "Hard"]
        print("\nSelect your difficulty:")
        ind = 1
        for item in dif_list:
            print("[{}]. {}".format(ind, item))
            ind += 1
        dif_choice = input("\n>>  ")
        if int(dif_choice) == 1:
            User.diff = 1
        elif int(dif_choice) == 2:
            User.diff = 2
        else: User.diff = 3
    
    dif_select()
    
    def ez_mode():
        ind = 0
        while ind < 5 and User.win == 0:
            repeater()
            ind += 1
    def med_mode():
        ind = 0
        while ind < 5 and User.win == 0:
            repeater()
            ind += 1
    def hard_mode():
        ind = 0
        while ind < 5 and User.win == 0:
            repeater()
            ind += 1
    
    def dif_set():
        if User.diff == 1:
            print("\nYou get 5 chances to guess a number between 1 and 20.")
            get_num_ez()
            ez_mode()
        elif User.diff == 2:
            print("\nYou get 5 chances to guess a number between 1 and 50.")
            get_num_med()
            med_mode()
        else:
            print("\nYou get 5 chances to guess a number between 1 and 100.")
            get_num_hard() 
            hard_mode()
    
    dif_set()

game()
 
 
 
 
 
 
 
 
 