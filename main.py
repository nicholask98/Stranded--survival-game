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
    global current_day
    global current_time
    print('---------------------------------------------------')
    print('HUNGER: {}/100  |  THIRST: {}/100  |  HEALTH:{}/100'.format(hunger, thirst, health))
    print('\n\n\n\n\n\n\n')
    print('                        []                         ')
    print('                       \||/                        ')
    print(' Day: {}   Time: {}     /\                         '.format(current_day, current_time))
    print('---------------------------------------------------')
    print('  [1]: Inventory                     [2]: OPTIONS  ')

    choice = int(input())
    clear()
    if choice == 1:
        inventory()
    elif choice == 2:
        options()
    else:
        print('Error')
    input()

def inventory():
    print('Inventory')
    print('                   | INVENTORY |                   ')
    print('---------------------------------------------------')
     #FIXME: Finish Inventory Menu
def options():
    global current_options
    print('                    | OPTIONS |                    ') 
    print('---------------------------------------------------')

    # FIXME: Use enumerate() in for loops for Options user_choice
    # EX. What I want this menu to look like:

    # [0] Back to Home Screen
    # [1] Gather Berries: 1 hour(s)
    # [2] Collect Branches: 2 hour(s)
    # [3] Collect Water from Ocean: 3 hour(s)
    # [4] Start a Fire with (4) branches: 1 hour(s)
    # etc....
    

current_day = 1
current_time = 800

# FIXME: Could keep a dictionary of options with how many hours they are, but keep the current_options a list. Run current_options through the dict to return the hour count.
current_options = ['Gather Berries', 'Collect Branches', 'Collect Water from Ocean']


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
input()
clear()
home_screen()
clear()
