import sys
import os
import time
import copy
from game import solved_places, zonemap, myPlayer, main_game_loop

##### TITLE SCREEN #####


def title_screen_selections():
    option = input('\n> ')
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("info"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit('The game will now exit.')
    while option.lower() not in ['play', 'info', 'quit']:
        print("Please enter a valid command.")
        option = input('\n> ')
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

    print('''             ) )        /\\
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

    print('''             ) )        /\\
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
    option = input('\n> ')
    if option.lower() == 'back':
        title_screen()
    while option.lower() != 'back':
        print('Please enter a valid command')
        option = input('\n> ')


def setup_game():
    os.system('cls')

    ### FIND A WAY TO RESET DICTIONARY ###

    global duplicate_solved_places
    global duplicate_zonemap
    duplicate_solved_places = copy.deepcopy(solved_places)
    duplicate_zonemap = copy.deepcopy(zonemap)
    myPlayer.difficulty = ''
    myPlayer.location = 'b2'
    myPlayer.solves = 0
    myPlayer.game_over = False

    ### NAME COLLECTION ###

    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_name = input('\n> ')
    myPlayer.name = player_name

    ### DIFFICULTY HANDLING ###

    question2 = "Hello, " + myPlayer.name + "! " + \
        "Please choose your difficulty level!\n"
    question2_choices = "There are 3 difficulty levels.\nEasy, Normal, and Hard.\nThe higher the difficulty, the tougher the monsters!\nEasy mode provides a map of your current location.\nYou can't die in easy mode!\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in question2_choices:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_difficulty = input('\n> ')
    valid_difficulty = ['easy', 'normal', 'hard']
    if player_difficulty.lower() == 'easy':
        myPlayer.difficulty = player_difficulty
        myPlayer.strength = 100
        print('You are now on ' + myPlayer.difficulty + ' mode!')
    elif player_difficulty.lower() == 'normal':
        myPlayer.difficulty = player_difficulty
        myPlayer.strength = 15
        print('You are now on ' + myPlayer.difficulty + ' mode!')
    elif player_difficulty.lower() == 'hard':
        myPlayer.difficulty = player_difficulty
        myPlayer.strength = 10
        print('You are now on ' + myPlayer.difficulty + ' mode!')
    while player_difficulty.lower() not in valid_difficulty:
        print('Please choose a valid difficulty!')
        player_difficulty = input('\n> ')
        if player_difficulty.lower() == 'easy':
            myPlayer.difficulty = player_difficulty
            myPlayer.strength = 100
            print('You are now on ' + myPlayer.difficulty + ' mode!')
        elif player_difficulty.lower() == 'normal':
            myPlayer.difficulty = player_difficulty
            myPlayer.strength = 15
            print('You are now on ' + myPlayer.difficulty + ' mode!')
        elif player_difficulty.lower() == 'hard':
            myPlayer.difficulty = player_difficulty
            myPlayer.strength = 10
            print('You are now on ' + myPlayer.difficulty + ' mode!')

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
    choice = input('\n> ')
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
        choice = input('\n> ')
        if choice.upper() == 'Y':
            os.system('cls')
            print('#######################################')
            print("#    Your adventure begins here...    #")
            print('#######################################')
            a = 'You awake and find yourself in an abandoned house...\nYou have no recollections whatsoever on how you got here...'
            b = 'Your surrounding is dimly lit and there is a strong ominous presence in the air...\nIt is imperative that you get out of here as soon as possible.\n'
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