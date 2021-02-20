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
    print('                   | INVENTORY |                   ') #FIXME: Finish Inventory Menu
    print('---------------------------------------------------')

def options():
    global current_options
    print('                    | OPTIONS |                    ') 
    print('---------------------------------------------------')
    
    # for time_required in current_options:
    #     for action in current_options[time_required]:
    #         print(action)

    '''
    for option in current_options:
        print('[{}]: {}'.format(option, current_options[option]))
    '''


# FIXME: figure out how to properly display options on options screen. Print the list index along with the selected
# option so the user can input a choice.

current_day = 1
current_time = 800

options_1 = ['Gather Berries', 'Pick Apples', 'Pick Pears']
options_2 = ['Collect Branches']
options_3 = []
options_4 = []
current_options = [options_1, options_2, options_3, options_4]


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
