# Python Text RPG
import sys
import os
import time
import random
import copy
from fsm import *

cmd = 'color 0c'
os.system(cmd)

##### PLAYER SETUP #####
class Player:
    def __init__(self):
        self.name = ''
        self.strength = 0
        self.difficulty = ''
        self.location = 'b2'
        self.solves = 0
        self.game_over = False        

myPlayer = Player()

##### MONSTER SETUP #####

class Monster:
    def __init__(self, strength, magic):
        self.strength = strength
        self.magic = magic
    
    def attack(self):
        return self.strength * self.magic

class Troll(Monster):
    def __init__(self, strength):
        self.name = 'Troll'
        super().__init__(strength=strength * 1.2, magic=strength * 0.5)

class Witch(Monster):
    def __init__(self, magic):
        self.name = 'Witch'
        super().__init__(strength=magic * 0.5, magic=magic * 1.7)

myTroll = Troll(random.randint(4,8))
myWitch = Witch(random.randint(4,8))

##### SM MINIGAME #####

class KickDoor(SM):
    def __init__(self):
        self.start_state = 0
    
    def get_next_values(self, state, inp):
        
        if state == 0 and inp.lower() == 'kick':
            next_state = 1
            output = 'The door budges slightly.'
        elif state == 1 and inp.lower() == 'kick':
            next_state = 2
            output = 'The door creaks loudly under your barrage of kicks!'
        elif state == 2 and inp.lower() == 'kick':
            next_state = 1
            output = 'The door explodes!'
            
        return next_state, output

##### TITLE SCREEN #####

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("info"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit('The game will now exit.')
    while option.lower() not in ['play', 'info', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("info"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit('The game will now exit.')


def title_screen():
    os.system('cls')
    
    print('''▓█████   ██████  ▄████▄   ▄▄▄       ██▓███  ▓█████
▓█   ▀ ▒██    ▒ ▒██▀ ▀█  ▒████▄    ▓██░  ██▒▓█   ▀ 
▒███   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██░ ██▓▒▒███   
▒▓█  ▄   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ 
░▒████▒▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██▒ ░  ░░▒████▒
░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░
░ ░  ░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░▒ ░      ░ ░  ░
░   ░  ░  ░  ░          ░   ▒   ░░          ░   
░  ░      ░  ░ ░            ░  ░            ░  ░
              ░                                  ''')

    print('''             ) )        /\   
            =====      /  \\
           _|___|_____/ __ \____________
          |::::::::::/ |  | \:::::::::::|
          |:::::::::/  ====  \::::::::::|
          |::::::::/__________\:::::::::|
          |_________|  ____  |__________|
           | ______ | / || \ | _______ |
           ||  |   || ====== ||   |   ||
           ||--+---|| |    | ||---+---||
           ||__|___|| |   o| ||___|___||
           |========| |____| |=========|
    (^^--^^^^-^^^^^-|________|-^^^--^^^--^^^--)
  (,,, ,, ,,, , ,, ,/________\,,,, ,, ,, , ,, ,,)
'''';'''';';'''''';';';'','',,,' /__________\,,,,',',;'';';'';'';''')

    print('\n###################################################')
    print('#              Welcome to the ESCAPE!             #')
    print('###################################################')
    print('#                    - Play -                     #')
    print('#                    - Info -                     #')
    print('#                    - Quit -                     #')
    print('###################################################')
    print('#               By Chee Kit 1004108               #')
    print('###################################################')
    title_screen_selections()


def help_menu():
    os.system('cls')

    print('''▓█████   ██████  ▄████▄   ▄▄▄       ██▓███  ▓█████
▓█   ▀ ▒██    ▒ ▒██▀ ▀█  ▒████▄    ▓██░  ██▒▓█   ▀ 
▒███   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██░ ██▓▒▒███   
▒▓█  ▄   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ 
░▒████▒▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██▒ ░  ░░▒████▒
░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░
░ ░  ░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░▒ ░      ░ ░  ░
░   ░  ░  ░  ░          ░   ▒   ░░          ░   
░  ░      ░  ░ ░            ░  ░            ░  ░
              ░                                  ''')

    print('''             ) )        /\   
            =====      /  \\
           _|___|_____/ __ \____________
          |::::::::::/ |  | \:::::::::::|
          |:::::::::/  ====  \::::::::::|
          |::::::::/__________\:::::::::|
          |_________|  ____  |__________|
           | ______ | / || \ | _______ |
           ||  |   || ====== ||   |   ||
           ||--+---|| |    | ||---+---||
           ||__|___|| |   o| ||___|___||
           |========| |____| |=========|
    (^^--^^^^-^^^^^-|________|-^^^--^^^--^^^--)
  (,,, ,, ,,, , ,, ,/________\,,,, ,, ,, , ,, ,,)
'''';'''';';'''''';';';'','',,,' /__________\,,,,',',;'';';'';'';''')

    print('\n###################################################')
    print('#                   Help Menu                     #')
    print('###################################################')
    print('# Your objective in this game is to solve all the #')
    print('# the riddles in each room and not die to the     #')
    print('# monsters along the way. Escape the house once   #')
    print('# you have explored all the rooms! GLHF!          #')
    print('#                                                 #')
    print('#                    - Back -                     #')
    print('###################################################')
    option = input('> ')
    if option.lower() == 'back':
        title_screen()
    while option.lower() != 'back':
        print('Please enter a valid command')
        option = input('> ')


##### MAP #####

"""
 a1 a2 a3 # PLAYER STARTS AT b2
----------
|  |  |  | a3
----------
|  | X|  | b3
----------
|  |  |  | c3
----------
"""
LOCATION = ''
DESCRIPTION = 'description'
INSPECT = 'examine'
SOLVED = False
TASK = 'task'
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'
MONSTER = None
MAP_DRAWING = None

solved_places = {'a1': False, 'a2': False, 'a3': False,
                 'b1': False, 'b2': True, 'b3': False,
                 'c1': False, 'c2': False, 'c3': False,
                 }
zonemap = {
    'a1': {
        LOCATION: "Winding Staircase",
        DESCRIPTION: 'You find yourself at the foot of a staircase leading towards... perhaps and exit?\n',
        INSPECT: 'Upon closer examination, there is a riddle inscribed on one of the railings!\n',
        TASK: "It reads, 'What two things can you never eat for breakfast?'\n",
        SOLVED: 'lunch and dinner',
        UP: 'a1',
        DOWN: 'b1',
        LEFT: 'a1',
        RIGHT: 'a2',
        MONSTER: None,
        MAP_DRAWING: '''----------
| X|  |  | 
----------
|  |  |  | 
----------
|  |  |  | 
----------'''
    },
    'a2': {
        LOCATION: "Main Entrance",
        DESCRIPTION: 'You see the exit - but you do not have a key!\nThe door seems too big to kick down as well...\n',
        INSPECT: '',
        TASK: 'Looks like you cannot escape until you have explored all the other rooms...\nThe keyhole seems oddly shaped... you cannot think of any key that might fit this keyhole.\n',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
        MONSTER: None,
        MAP_DRAWING: '''----------
|  | X|  | 
----------
|  |  |  | 
----------
|  |  |  | 
----------'''
    },
    'a3': {
        LOCATION: "Kitchen",
        DESCRIPTION: 'A musty smell filled the air - this kitchen must have been left alone for years...\n',
        INSPECT: 'A goblin-esque creature slumbers out of its corner - much to your surprise - and motions you closer.\n',
        TASK: "'A riddle - you must answer, if it is escape - you desire. Ooohooohoo yesh.'\n'David's father has three sons : Tom, Dick and _____. '\n",
        SOLVED: 'david',
        UP: 'a3',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a3',
        MONSTER: None,
        MAP_DRAWING: '''----------
|  |  | X| 
----------
|  |  |  | 
----------
|  |  |  | 
----------'''
    },
    'b1': {
        LOCATION: "Master Bedroom ",
        DESCRIPTION: 'Whoever lived in this house must have been deranged.\nTorture equipment were strewn all over the room as you tip-toed across,\nmaking your way to the door on the opposite.\n',
        INSPECT: 'You notice a riddle written on the bedsheet in blood.\n',
        TASK: "What's a lifeguard's favorite game?\n",
        SOLVED: 'pool',
        UP: 'a1',
        DOWN: 'c1',
        LEFT: 'b1',
        RIGHT: 'b2',
        MONSTER: None,
        MAP_DRAWING: '''----------
|  |  |  | 
----------
| X|  |  | 
----------
|  |  |  | 
----------'''
    },
    'b2': {
        LOCATION: 'Cell ',
        DESCRIPTION: 'You find yourself in a dank and musty cell.\n',
        INSPECT: 'You need to get out of this hell hole...\n',
        TASK: None,
        SOLVED: True,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
        MONSTER: None,
        MAP_DRAWING: '''----------
|  |  |  | 
                        ----------
|  | X|  | 
----------
|  |  |  | 
----------'''
    },
    'b3': {
        LOCATION: "Bathroom ",
        DESCRIPTION: 'You reek at the smell of fecal matter.\nSomeone must have forgotten to flush the toilet for seemingly... years.\n',
        INSPECT: 'The reflection in the mirror startles you. You could have sworn that your own reflection moved on its own accord.\n',
        TASK: "Suddenly the reflection asks you,\n'I am not alive, but I grow;\nI don't have lungs, but I need air;\nI don't have a mouth, but water kills me.\nWhat am I?\n",
        SOLVED: 'fire',
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b3',
        MONSTER: None,
        MAP_DRAWING: '''----------
|  |  |  | 
----------
|  |  | X| 
----------
|  |  |  | 
----------'''
    },
    'c1': {
        LOCATION: "Dining Hall",
        DESCRIPTION: 'A strong pungent smell of rotting carcass wafts into your nose.\nYou are not alone here...\n\nA burly Troll lumbers towards you, getting ready to swing its club!\nYou have to KILL it or DIE trying!\n',
        INSPECT: 'examine',
        TASK: 'task',
        SOLVED: 'solved',
        UP: 'b1',
        DOWN: 'c1',
        LEFT: 'c1',
        RIGHT: 'c2',
        MONSTER: None,
        MAP_DRAWING: '''----------
|  |  |  | 
----------
|  |  |  | 
----------
| X|  |  | 
----------'''
    },
    'c2': {
        LOCATION: "Unknown",
        DESCRIPTION: 'The door infront of you is locked.\n',
        INSPECT: 'Looks like you may have to resort to kicking it down.\n',
        TASK: 'task',
        SOLVED: None,
        UP: 'b2',
        DOWN: 'c2',
        LEFT: 'c1',
        RIGHT: 'c3',
        MONSTER: None,
        MAP_DRAWING: '''----------
|  |  |  | 
----------
|  |  |  | 
----------
|  | X|  | 
----------'''
    },
    'c3': {
        LOCATION: "Altar",
        DESCRIPTION: 'The smell of incense burns your nose. Something demonic resides here...\n\nA Witch spawned out of nowhere and prepares to cast her spell!\nYou must KILL her or DIE trying!\n',
        INSPECT: None,
        TASK: None,
        SOLVED: None,
        UP: 'b3',
        DOWN: 'c3',
        LEFT: 'c2',
        RIGHT: 'c3',
        MONSTER: None,
        MAP_DRAWING: '''----------
|  |  |  | 
----------
|  |  |  | 
----------
|  |  | X| 
----------'''
    },

}

##### GAME INTERACTIVITY #####

def print_location():
    print(('#' * (6 + len(zonemap[myPlayer.location][LOCATION]))))
    print('# -' + '-' * len(zonemap[myPlayer.location][LOCATION]) + '- #')
    print('#  ' + zonemap[myPlayer.location][LOCATION] + '  #')
    print('# -' + '-' * len(zonemap[myPlayer.location][LOCATION]) + '- #')
    print(('#' * (6 + len(zonemap[myPlayer.location][LOCATION]))))
    if myPlayer.difficulty == 'easy':
        print(zonemap[myPlayer.location][MAP_DRAWING])
    description = zonemap[myPlayer.location][DESCRIPTION]
    for character in description:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

def prompt():
    if myPlayer.location == 'c2':
        if solved_places[myPlayer.location] == False:
            print(zonemap[myPlayer.location][INSPECT])
            player_examine()
    if myPlayer.solves == 4:
        zonemap['a2'][DESCRIPTION] = 'Something about this door seems different from before...\n'
        zonemap['a2'][TASK] = 'The door rumbles...'
        lifted = "You feel the ominous presence in the house being lifted... Something has changed.\n"
        for character in lifted:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        # print("You feel the ominous presence in the house being lifted... Something has changed.")

    print('\n==========================')
    what_to_do = 'What would you like to do?\n'
    for character in what_to_do:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    print('==========================')
    if myPlayer.location == 'c1' and solved_places[myPlayer.location] == False:
        print('> attack')
        print('> quit')
        acceptable_actions = ['attack', 'quit']
    elif myPlayer.location == 'c3' and solved_places[myPlayer.location] == False:
        print('> attack')
        print('> quit')
        acceptable_actions = ['attack', 'quit']
    else:
        print('> move')
        print('> examine')
        print('> quit')
        acceptable_actions = ['move', 'go', 'travel', 'walk',
        'quit', 'examine', 'inspect', 'interact', 'look']
    action = input('> ')
    while action.lower() not in acceptable_actions:
        print('Unknown action, please try again.')
        action = input('> ')
    if action.lower() == 'quit':
        sys.exit('The game will now exit.')
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look', 'attack']:
        player_examine()

def player_move(myAction):
    print('\n' + '================================')
    move_to = 'Where would you like to move to?\n'
    for character in move_to:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    print('================================')
    if myPlayer.location == 'a1':
        print('> down')
        print('> right')
        dest = input('>' )
    elif myPlayer.location == 'b1':
        print('> up')
        print('> down')
        print('> right')
        dest = input('>' )
    elif myPlayer.location == 'c1':
        print('> up')
        print('> right')
        dest = input('>' )
    elif myPlayer.location == 'a2':
        print('> down')
        print('> left')
        print('> right')
        dest = input('>' )
    elif myPlayer.location == 'a3':
        print('> down')
        print('> left')
        dest = input('>' )
    elif myPlayer.location == 'b3':
        print('> up')
        print('> down')
        print('> left')
        dest = input('>' )
    elif myPlayer.location == 'c3':
        print('> up')
        print('> left')
        dest = input('>' )
    elif myPlayer.location == 'a2':
        print('> up')
        print('> left')
        print('> right')
        dest = input('>' )
    else:
        print('> up')
        print('> down')
        print('> left')
        print('> right')
        dest = input('>' )

    ### ADD BOUNDARY PERHAPS? ###

    if myPlayer.location == 'a1':
        acceptable_actions = ['down', 'south', 'right', 'east' 'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('> ')
    if myPlayer.location == 'a2':
        acceptable_actions = ['down', 'south', 'left', 'west', 'right', 'east' 'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('> ')
    if myPlayer.location == 'a3':
        acceptable_actions = ['down', 'south', 'left', 'west', 'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('> ')
    if myPlayer.location == 'b1':
        acceptable_actions = ['up', 'north', 'down', 'south', 'right', 'east' 'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('> ')
    if myPlayer.location == 'c1':
        acceptable_actions = ['up', 'north', 'right', 'east' 'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('> ')
    if myPlayer.location == 'c2':
        acceptable_actions = ['up', 'north', 'left', 'west', 'right', 'east' 'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('> ')
    if myPlayer.location == 'c3':
        acceptable_actions = ['up', 'north', 'left', 'west', 'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('> ')
    if myPlayer.location == 'b3':
        acceptable_actions = ['up', 'north', 'down', 'south', 'left', 'west', 'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('> ')

    acceptable_actions = ['up', 'north', 'down', 'south', 'left', 'west', 'right', 'east' 'quit']
    while dest.lower() not in acceptable_actions:
        print('Unknown action, please try again.')
        dest = input('> ')
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest.lower() == 'quit':
        sys.exit('The game will now exit.')

##### MOVES PLAYER TO DESIRED DESTINATION #####

def movement_handler(destination):
    myPlayer.location = destination
    moved = '\n' + 'You have moved to the ' + zonemap[myPlayer.location][LOCATION] + ".\n"
    for character in moved:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    print_location()

##### HANDLES EXAMINE ACTION #####

def player_examine():
    if myPlayer.location == 'c2':
        if solved_places[myPlayer.location] == False:
            kick_door = KickDoor()
            kick_door.start()
            a = input('> ')
            while a.lower() != 'kick':
                print('You can try kicking the door down...')
                a = input('> ')
            print(kick_door.step(a))
            a = input('> ')
            while a.lower() != 'kick':
                print('You might have to kick a few more times...')
                a = input('> ')
            print(kick_door.step(a))
            a = input('> ')
            while a.lower() != 'kick':
                print('One more kick should do it!')
                a = input('> ')
            print(kick_door.step(a))
            zonemap[myPlayer.location][LOCATION] = 'Corridor'
            zonemap[myPlayer.location][DESCRIPTION] = 'You find yourself in the corridor, with doors leading east and west.\n'
            zonemap[myPlayer.location][INSPECT] = 'You can sense monsters nearby...\n'
            solved_places[myPlayer.location] = True
            alert = 'You may have alerted nearby monsters...\nYou can now enter.\n'
            for character in alert:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.01)
            print_location()

        else:
            print(zonemap[myPlayer.location][INSPECT])
    elif myPlayer.location == 'c1':
        rolled_dice = random.randint(1,6)
        zonemap[myPlayer.location][MONSTER] = myTroll
        if solved_places[myPlayer.location] == True:
            print("You have already slain the beast.")
        elif myTroll.attack() <= rolled_dice * myPlayer.strength:
            print('You rolled a ' + str(rolled_dice) + '!')
            print('You have slain the Troll!')
            zonemap[myPlayer.location][DESCRIPTION] = 'The rotting smell of the now decomposing Troll you have just slain disgusts you.\n'
            zonemap[myPlayer.location][MONSTER] = None
            solved_places[myPlayer.location] = True
        else:
            print('You rolled a ' + str(rolled_dice) + '!')
            print('You have been slain!\nBetter luck next time!')
            sys.exit('The game will now exit.')

    elif myPlayer.location == 'c3':
        rolled_dice = random.randint(1,6)
        zonemap[myPlayer.location][MONSTER] = myWitch
        if solved_places[myPlayer.location] == True:
            print("You have already slain the spawn of Salem.")
        elif myWitch.attack() <= rolled_dice * myPlayer.strength:
            print('You rolled a ' + str(rolled_dice) + '!')
            print('You have slain the Witch!')
            zonemap[myPlayer.location][DESCRIPTION] = 'The carcass of the Witch you have just slain lay crumpled on the floor.\n'
            zonemap[myPlayer.location][MONSTER] = None
            solved_places[myPlayer.location] = True
        else:
            print('You rolled a ' + str(rolled_dice) + '!')
            print('You have been slain!\nBetter luck next time!')
            sys.exit('The game will now exit.')

    elif solved_places[myPlayer.location] == False:
        inspect_puzzle = zonemap[myPlayer.location][INSPECT]
        for character in inspect_puzzle:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        inspect_task = zonemap[myPlayer.location][TASK]
        for character in inspect_task:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        # print('\n' + (zonemap[myPlayer.location][INSPECT]))
        # print((zonemap[myPlayer.location][TASK]))
        puzzle_answer = input("> ")
        checkpuzzle(puzzle_answer)
    else:
        examined = "You have already examined this area.\n"
        for character in examined:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)

##### CHECK PUZZLE #####

def checkpuzzle(puzzle_answer):
	if myPlayer.location == 'a2':
		if myPlayer.solves >= 4:
			game_over = "Without laying a finger on the door, it creaks - and groans - and opens outward grudgingly...\nThe sunlight blinds you as you momentarily fall backwards...\nThe smell of fresh air and freedom overwhelms you...\nYou have finally escaped!\nCONGRATULATIONS! "+ myPlayer.name + "!\nYour adventure ends here."
			for character in game_over:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.05)
			myPlayer.game_over = True
            # sys.exit('The game will now exit.')
		else:
			print("The door won't budge no matter how hard you try.")

	else:
		if puzzle_answer.lower() == (zonemap[myPlayer.location][SOLVED]):
			solved_places[myPlayer.location] = True
			myPlayer.solves += 1
			print("You have solved the puzzle! One step closer to being out of this creepy house...")
			print("\nRooms solved: " + str(myPlayer.solves))
		else:
			print("=============================\nThat is incorrect! Try again.\n=============================")
			player_examine()


##### GAME FUNCTIONALITY #####

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
    # this handles if puzzles have been solved, enemies defeated, explored everything.

def setup_game():
    os.system('cls')

    ### NAME COLLECTION ###

    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_name = input('> ')
    myPlayer.name = player_name

    ### DIFFICULTY HANDLING ###

    question2 = "Hello, " + myPlayer.name + "! " + "Please choose your difficulty level!\n"
    question2_choices = "There are 3 difficulty levels.\nEasy, Normal, and Difficult.\nThe higher the difficulty, the tougher the monsters!\nEasy mode provides a map of your current location.\nYou can't die in easy mode!\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in question2_choices:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_difficulty = input('> ')
    valid_difficulty = ['easy', 'normal', 'difficult']
    if player_difficulty.lower() == 'easy':
        myPlayer.difficulty = player_difficulty
        myPlayer.strength = 100
        print('You are now on ' + myPlayer.difficulty + ' mode!')
    elif player_difficulty.lower() == 'normal':
        myPlayer.difficulty = player_difficulty
        myPlayer.strength = 15
        print('You are now on ' + myPlayer.difficulty + ' mode!')
    elif player_difficulty.lower() == 'difficult':
        myPlayer.difficulty = player_difficulty
        myPlayer.strength = 10
        print('You are now on ' + myPlayer.difficulty + ' mode!')
    while player_difficulty.lower() not in valid_difficulty:
        print('Please choose a valid difficulty!')
        player_difficulty = input('> ')
        if player_difficulty.lower() == 'easy':
            myPlayer.difficulty = player_difficulty
            myPlayer.strength = 100
            print('You are now on ' + myPlayer.difficulty + ' mode!')
        elif player_difficulty.lower() == 'normal':
            myPlayer.difficulty = player_difficulty
            myPlayer.strength = 15
            print('You are now on ' + myPlayer.difficulty + ' mode!')
        elif player_difficulty.lower() == 'difficult':
            myPlayer.difficulty = player_difficulty
            myPlayer.strength = 10
            print('You are now on ' + myPlayer.difficulty + ' mode!')

    # question3 = "Welcome, " + player_name + " the " + player_difficulty + ".\n"
    # for character in question3:
    #     sys.stdout.write(character)
    #     sys.stdout.flush()
    #     time.sleep(0.01)

    ### INTRODUCTION ###

    speech1 = 'Greetings ' + myPlayer.name + '!\n'
    speech2 = "You are about to find yourself in an adventure where YOU are the HERO!\nOr will you... "
    speech3 = "Just make sure you don't get too lost...\n"
    speech4 = "Heh heh heh heh...\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)

    start_game_prompt = "Would you like to begin? Enter Y to start or N if you're too afraid to play!\n"
    for character in start_game_prompt:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    choice = input('> ')
    valid_choices = ['Y', 'N']
    if choice.upper() == 'Y':
        os.system('cls')
        print('#######################################')
        print("#    Your adventure begins here...    #")
        print('#######################################')
        a = 'You awake and find yourself in an abandoned house...\nYou have no recollections whatsoever on how you got here...\n'
        b = 'Your surrounding is dimly lit and there is a strong ominous presence in the air...\nIt is imperative that you get out of here as soon as possible.'
        for character in a:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        for character in b:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        main_game_loop()
    elif choice.upper() == 'N':
        sys.exit('The game will now exit.')
    while choice.upper() not in valid_choices:
        print('Please enter a valid option!')
        choice = input('> ')
        if choice.upper() == 'Y':
            os.system('cls')
            print('#######################################')
            print("#    Your adventure begins here...    #")
            print('#######################################')
            a = 'You awake and find yourself in an abandoned house...\nYou have no recollections whatsoever on how you got here...'
            b = 'Your surrounding is dimly lit and there is a strong ominous presence in the air...\nIt is imperative that you get out of here as soon as possible.'
            for character in a:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.02)
            for character in b:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.02)
            main_game_loop()
        elif choice.upper() == 'N':
            sys.exit('The game will now exit.')

title_screen()