from os import system, name 
from time import sleep 
import random


# FUNCTIONS

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def new_day(day):
    day += 1
    return day

def home_screen():
    global hunger
    global thirst
    global health
    print('---------------------------------------------------')
    print('HUNGER: {}/100     THIRST: {}/100     HEALTH:{}/100'.format(hunger, thirst, health))
    print('                                                   ')
    print('                                                   ')
    print('                                                   ')
    print('                                                   ')
    print('                                                   ')
    print('                                                   ')
    print('                                                   ')
    print('                        []                         ')
    print('                       \||/                        ')
    print('                        /\                         ')
    print('---------------------------------------------------')
    print('  [1]: Inventory                     [2]: Options  ')

    user_choice = int(input())
    clear()
    if user_choice == 1:
        print('Inventory')
    elif user_choice == 2:
        print('Options')
    else:
        print('Error')
    input()
current_day = 1
current_time = 800

# STATS:
hunger = 80
thirst = 80
health = 80


clear()
print("You wake up on a deserted island. You find a note. It reads: (Press Enter)")
input()
clear()
print("\"We left you here and won't be back for at least the next 50 days.")
print("You should probably figure out how to live on your own\"")

home_screen()
clear()
