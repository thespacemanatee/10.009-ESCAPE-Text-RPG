# Python Text RPG
import sys
import os
import time
import random
import copy
from map import *
from monsters import Monster, Troll, Witch
from libdw import sm


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
myTroll = Troll(random.randint(4, 8))
myWitch = Witch(random.randint(4, 8))

##### SM MINIGAME #####


class KickDoor(sm.SM):
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


kick_door = KickDoor()
duplicate_solved_places = copy.deepcopy(solved_places)
duplicate_zonemap = copy.deepcopy(zonemap)

##### GAME INTERACTIVITY #####


def print_location():
    print(('#' * (6 + len(duplicate_zonemap[myPlayer.location][LOCATION]))))
    print('# -' +
          '-' *
          len(duplicate_zonemap[myPlayer.location][LOCATION]) +
          '- #')
    print('#  ' + duplicate_zonemap[myPlayer.location][LOCATION] + '  #')
    print('# -' +
          '-' *
          len(duplicate_zonemap[myPlayer.location][LOCATION]) +
          '- #')
    print(('#' * (6 + len(duplicate_zonemap[myPlayer.location][LOCATION]))))
    if myPlayer.difficulty == 'easy':
        print(duplicate_zonemap[myPlayer.location][MAP_DRAWING])
    description = duplicate_zonemap[myPlayer.location][DESCRIPTION]
    for character in description:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

def prompt():
    if myPlayer.location == 'c2':
        if not duplicate_solved_places[myPlayer.location]:
            print(duplicate_zonemap[myPlayer.location][INSPECT])
            player_examine()
    if myPlayer.solves == 4:
        duplicate_zonemap['a2'][DESCRIPTION] = 'Something about this door seems different from before...\n'
        duplicate_zonemap['a2'][TASK] = '\nThe door rumbles...'
        lifted = "\nYou feel the ominous presence in the house being lifted... Something has changed.\n"
        for character in lifted:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)

    print('\n==========================')
    what_to_do = 'What would you like to do?\n'
    for character in what_to_do:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    print('==========================')
    if myPlayer.location == 'c1' and duplicate_solved_places[myPlayer.location] == False:
        print('> attack')
        print('> quit')
        acceptable_actions = ['attack', 'quit']
    elif myPlayer.location == 'c3' and duplicate_solved_places[myPlayer.location] == False:
        print('> attack')
        print('> quit')
        acceptable_actions = ['attack', 'quit']
    else:
        print('> move')
        print('> examine')
        print('> quit')
        acceptable_actions = ['move', 'go', 'travel', 'walk',
                              'quit', 'examine', 'inspect', 'interact', 'look']
    action = input('\n> ')
    while action.lower() not in acceptable_actions:
        print('Unknown action, please try again.')
        action = input('\n> ')
    if action.lower() == 'quit':
        myPlayer.game_over = True
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look', 'attack']:
        player_examine()


def player_move(action):
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
        dest = input('\n> ')
    elif myPlayer.location == 'b1':
        print('> up')
        print('> down')
        print('> right')
        dest = input('\n> ')
    elif myPlayer.location == 'c1':
        print('> up')
        print('> right')
        dest = input('\n> ')
    elif myPlayer.location == 'a2':
        print('> down')
        print('> left')
        print('> right')
        dest = input('\n> ')
    elif myPlayer.location == 'a3':
        print('> down')
        print('> left')
        dest = input('\n> ')
    elif myPlayer.location == 'b3':
        print('> up')
        print('> down')
        print('> left')
        dest = input('\n> ')
    elif myPlayer.location == 'c3':
        print('> up')
        print('> left')
        dest = input('\n> ')
    elif myPlayer.location == 'a2':
        print('> up')
        print('> left')
        print('> right')
        dest = input('\n> ')
    elif myPlayer.location == 'c2':
        print('> up')
        print('> left')
        print('> right')
        dest = input('\n> ')
    else:
        print('> up')
        print('> down')
        print('> left')
        print('> right')
        dest = input('\n> ')

    ### ADD BOUNDARY PERHAPS? ###

    if myPlayer.location == 'a1':
        acceptable_actions = ['down', 'south', 'right', 'east' 'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('\n> ')
    if myPlayer.location == 'a2':
        acceptable_actions = [
            'down',
            'south',
            'left',
            'west',
            'right',
            'east'
            'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('\n> ')
    if myPlayer.location == 'a3':
        acceptable_actions = ['down', 'south', 'left', 'west', 'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('\n> ')
    if myPlayer.location == 'b1':
        acceptable_actions = [
            'up',
            'north',
            'down',
            'south',
            'right',
            'east'
            'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('\n> ')
    if myPlayer.location == 'c1':
        acceptable_actions = ['up', 'north', 'right', 'east' 'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('\n> ')
    if myPlayer.location == 'c2':
        acceptable_actions = [
            'up',
            'north',
            'left',
            'west',
            'right',
            'east'
            'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('\n> ')
    if myPlayer.location == 'c3':
        acceptable_actions = ['up', 'north', 'left', 'west', 'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('\n> ')
    if myPlayer.location == 'b3':
        acceptable_actions = [
            'up',
            'north',
            'down',
            'south',
            'left',
            'west',
            'quit']
        while dest.lower() not in acceptable_actions:
            print('This path leads to nowhere.')
            dest = input('\n> ')

    acceptable_actions = [
        'up',
        'north',
        'down',
        'south',
        'left',
        'west',
        'right',
        'east'
        'quit']
    while dest.lower() not in acceptable_actions:
        print('Unknown action, please try again.')
        dest = input('\n> ')
    if dest in ['up', 'north']:
        destination = duplicate_zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = duplicate_zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = duplicate_zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = duplicate_zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest.lower() == 'quit':
        myPlayer.game_over = True

##### MOVES PLAYER TO DESIRED DESTINATION #####


def movement_handler(destination):
    os.system('cls')
    myPlayer.location = destination
    moved = '\n' + 'You have moved to the ' + \
        duplicate_zonemap[myPlayer.location][LOCATION] + ".\n"
    for character in moved:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    print_location()

##### HANDLES EXAMINE ACTION #####


def player_examine():
    if myPlayer.location == 'c2':
        if not duplicate_solved_places[myPlayer.location]:
            kick_door.start()
            a = input('> kick\n\n> ')
            while a.lower() != 'kick':
                print('You can try kicking the door down...')
                a = input('> kick\n\n> ')
            print(kick_door.step(a))
            a = input('> kick\n\n> ')
            while a.lower() != 'kick':
                print('You might have to kick a few more times...')
                a = input('> kick\n\n> ')
            print(kick_door.step(a))
            a = input('> kick\n\n> ')
            while a.lower() != 'kick':
                print('One more kick should do it!')
                a = input('> kick\n\n> ')
            print(kick_door.step(a))
            duplicate_zonemap[myPlayer.location][LOCATION] = 'Corridor'
            duplicate_zonemap[myPlayer.location][DESCRIPTION] = 'You find yourself in the corridor, with doors leading east and west.\n'
            duplicate_zonemap[myPlayer.location][INSPECT] = '\nYou can sense monsters nearby...'
            duplicate_solved_places[myPlayer.location] = True
            alert = 'You may have alerted nearby monsters...\nYou can now enter.\n'
            for character in alert:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.01)
            print_location()

        else:
            print(duplicate_zonemap[myPlayer.location][INSPECT])
    elif myPlayer.location == 'c1':
        rolled_dice = random.randint(1, 6)
        if duplicate_solved_places[myPlayer.location]:
            print("\nYou have already slain the beast.")
        elif myTroll.attack() <= rolled_dice * myPlayer.strength:
            print('You rolled a ' + str(rolled_dice) + '!')
            print('You have slain the Troll!')
            duplicate_zonemap[myPlayer.location][DESCRIPTION] = 'The rotting smell of the now decomposing Troll you have just slain disgusts you.\n'
            duplicate_solved_places[myPlayer.location] = True

        else:
            print('You rolled a ' + str(rolled_dice) + '!')
            print('You have been slain!\nBetter luck next time!\n')
            myPlayer.game_over = True

    elif myPlayer.location == 'c3':
        rolled_dice = random.randint(1, 6)
        if duplicate_solved_places[myPlayer.location]:
            print("\nYou have already slain the spawn of Salem.")
        elif myWitch.attack() <= rolled_dice * myPlayer.strength:
            print('You rolled a ' + str(rolled_dice) + '!\n')
            print('You have slain the Witch!')
            duplicate_zonemap[myPlayer.location][DESCRIPTION] = 'The carcass of the Witch you have just slain lay crumpled on the floor.\n'
            duplicate_solved_places[myPlayer.location] = True

        else:
            print('You rolled a ' + str(rolled_dice) + '!')
            print('You have been slain!\nBetter luck next time!\n')
            myPlayer.game_over = True
    
    elif myPlayer.location == 'b2':
        a = 'You need to get out of this Cell and start exploring for clues on how to escape...'
        for character in a:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)

    elif duplicate_solved_places[myPlayer.location] == False:
        inspect_puzzle = duplicate_zonemap[myPlayer.location][INSPECT]
        for character in inspect_puzzle:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        inspect_task = duplicate_zonemap[myPlayer.location][TASK]
        for character in inspect_task:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        puzzle_answer = input('\n> ')
        checkpuzzle(puzzle_answer)
    else:
        examined = "\nYou have already examined this area.\n"
        for character in examined:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)


##### CHECK PUZZLE #####


def checkpuzzle(puzzle_answer):
    if myPlayer.location == 'a2':
        if myPlayer.solves >= 4:
            game_over = "\nWithout laying a finger on the door, it creaks - and groans - and opens outward grudgingly...\nThe sunlight blinds you as you momentarily fall backwards...\nThe smell of fresh air and freedom overwhelms you...\nYou have finally escaped!\nCONGRATULATIONS! " + myPlayer.name + "!\nYour adventure ends here.\n"
            for character in game_over:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            myPlayer.game_over = True
            print('''
 ▄████▄   ▒█████   ███▄    █   ▄████  ██▀███   ▄▄▄     ▄▄▄█████▓ █    ██  ██▓    ▄▄▄     ▄▄▄█████▓ ██▓ ▒█████   ███▄    █   ██████ 
▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █  ██▒ ▀█▒▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒ ██  ▓██▒▓██▒   ▒████▄   ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █ ▒██    ▒ 
▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▓██  ▒██░▒██░   ▒██  ▀█▄ ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒░ ▓██▄   
▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▓▓█  ░██░▒██░   ░██▄▄▄▄██░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒  ▒   ██▒
▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ▒▒█████▓ ░██████▒▓█   ▓██▒ ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░▒██████▒▒
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒▒   ▓▒█░ ▒ ░░   ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░
  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░  ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░   ░    ░░▒░ ░ ░ ░ ░ ▒  ░ ▒   ▒▒ ░   ░     ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒  ░ ░
░        ░ ░ ░ ▒     ░   ░ ░ ░ ░   ░   ░░   ░   ░   ▒    ░       ░░░ ░ ░   ░ ░    ░   ▒    ░       ▒ ░░ ░ ░ ▒     ░   ░ ░ ░  ░  ░  
░ ░          ░ ░           ░       ░    ░           ░  ░           ░         ░  ░     ░  ░         ░      ░ ░           ░       ░  
░                                                                                                                                  
''')
        else:
            print("\nThe door won't budge no matter how hard you try.\n")

    else:
        if puzzle_answer.lower() == (
                duplicate_zonemap[myPlayer.location][SOLVED]):
            duplicate_solved_places[myPlayer.location] = True
            myPlayer.solves += 1
            print(
                "\nYou have solved the puzzle! One step closer to being out of this creepy house...\n")
            print("Rooms solved: " + str(myPlayer.solves))
        else:
            print(
                "=============================\nThat is incorrect! Try again.\n=============================")
            player_examine()


##### GAME FUNCTIONALITY #####


def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
    if myPlayer.game_over is True:
        over = 'The game will now exit. Thanks for playing!'
        for character in over:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        sys.exit()
        # restart = 'Would you like to restart? Y - Yes, N - No'
        # for character in restart:
        #     sys.stdout.write(character)
        #     sys.stdout.flush()
        #     time.sleep(0.01)
        # choice = input('\n> ')
        # acceptable_actions = ['y', 'n']
        # if choice.lower() == 'y':
        #     title_screen()
        # elif choice.lower() == 'n':
        #     sys.exit('\nThe game will now exit. Thanks for playing!')
        # while choice.lower() not in acceptable_actions:
        #     print('Unknown action, please try again.')
        #     choice = input('\n> ')
        #     if choice.lower() == 'y':
        #         title_screen()
        #     elif choice.lower() == 'n':
        #         sys.exit('The game will now exit. Thanks for playing!')
    # this handles if puzzles have been solved, enemies defeated, explored
    # everything.