# ESCAPE - another Text RPG

A text-based role playing game written in Python 3.

## Game Description
***

You find yourself in an abandoned house and you need to find a way out. Explore the different rooms, solve the riddles and brave the monsters to stand a chance in escaping.

## Prerequisites
***

Before you run the code, make sure you have libdw installed.

```
pip install libdw
```

## Instructions
***

### Setting up the game

Run textRPG.py in your favorite IDE. You will be greeted with a title selections screen. There are 3 options. ***Play*** will start the game, ***info*** brings up the information page and ***quit*** exits the console.

When the game is started, it will ask for your name and the difficulty level desired. Easy mode provides a map of your current location as well as invincibilty against monsters. The higher the difficulty, the more difficult it is to overcome monsters.

The game begins after inputting ***Y*** when prompted.

### Playing the game

In each location you are provided with 3 options - ***move***, ***examine***, and ***quit***. ***Quit*** simply exits the console. When ***move*** is the input, you are generally provided with 4 directions of movement, - ***up***, ***down***, ***left***, ***right*** - unless you are at a deadend in which case the relevant move actions will be displayed. When ***examine*** is the input, the player examines the room for any clues on how to escape the house. When a riddle is shown, input the answer that you think is correct and if so, the counter for number of riddles solved will increase. When the player encounters a monster, he/she will be unable to ***move*** to another location and must face the monster. ***Attack*** will roll a dice for the player and determine his attack strength versus the monster.

### Win condition

Upon reaching a certain number of riddles solved, the player can finally escape the house.

## Code explanation
***

In this section I will attempt to explain what each function does.

```Py
class Player:
    def __init__(self):
        self.name = ''
        self.strength = 0
        self.difficulty = ''
        self.location = 'b2'
        self.solves = 0
        self.game_over = False

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
```

Creating classes for the Player and Monster and using inheritance in classes Witch and Troll.

```Py
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
```

Using libdw's sm class to create a minigame. Each input of string 'kick' returns the next state as well as a string output to prompt the user to enter string 'kick' a few more times until the door is broken.


```Python
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
```

This function codes for the title screen selections. The player can choose to play, read the information page or quit the game. Playing the game calls the setup_game().

```Py
def title_screen():
```

This function prints out the title screen graphics and calls the title_screen_selections() function.

```Py
def help_menu():
```

This function prints out the information menu.

```Py
solved_places = {'a1': False, 'a2': False, 'a3': False,
                 'b1': False, 'b2': True, 'b3': False,
                 'c1': False, 'c2': False, 'c3': False,
                 }
```

This code initialises a dictionary of map locations in the game and assigns a boolean to each key. The values are set to True when the location is solved.

```Py
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
        MAP_DRAWING: '''----------
| X|  |  |
----------
|  |  |  |
----------
|  |  |  |
----------'''
    },
```

This code initialises a nested dictionary of map locations which contains a dictionary of its properties such as location name and description.

```Py
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
```

This function prints the location information such as location name and it's description.

```Py
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
```

This function prompts the user on what the player would like to do in the current location. Available options are move, attack, examine and quit. They call the functions player_move(action), player_examine() and sys.exit() respectively.

```Py
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
```

This function takes in the argument from prompt() and prompts the player on which direction the player would like to move in and calls the movement_handler(destination) function.

```Py
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
```

This function takes in the argument from player_move(action) and sends the player to the desired location and calls the print_location() function.

```Py
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
```

This function prints out the task that needs to be completed in each location, or prints out a combat sequence, or prints out information about the location if all tasks have been completed. If a riddle is displayed, it takes in an input and sends that input to the next function checkpuzzle(puzzle_answer) for checking. If a combat sequence is displayed, attacking rolls a die of 6 sides and pit strength values against opponent.

```Py
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
```

This function first checks if the number of solves is >= 4, in which case it will initiate the game over sequence. Else, it takes in the argument from player_examine() and checks if the answer is correct. If it is, the counter for solves increases by 1. Else, the player_examine() function is called again so that the player can input the correct answer.

```Py
def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
    if myPlayer.game_over is True:
        restart = 'Would you like to restart? Y - Yes, N - No'
        for character in restart:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
        choice = input('\n> ')
        acceptable_actions = ['y', 'n']
        if choice.lower() == 'y':
            title_screen()
        elif choice.lower() == 'n':
            sys.exit('\nThe game will now exit. Thanks for playing!')
        while choice.lower() not in acceptable_actions:
            print('Unknown action, please try again.')
            choice = input('\n> ')
            if choice.lower() == 'y':
                title_screen()
            elif choice.lower() == 'n':
                sys.exit('The game will now exit. Thanks for playing!')
```

This function handles the game loop and when it exits the loop. While the game_over attribute in myPlayer is False, the game will keep prompting the user for the next move by calling prompt(). Else, the function will ask the user if they would like to restart the game. If restarting, the function calls title_screen() and the game restarts, else the console will exit.

```Py
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
```

This function resets the dictionary to its original state. This is to facilitate the scenario whereby the player chooses to restart the game. Then, it asks for the players desired name and difficulty, followed by an introduction to the game and calls the main_game_loop() function and starts the game loop.

```Py
title_screen()
```

When the console is run, this function initialises the game as seen above.

## Deployment
***

Run this command

```Py
python textRPG.py
```

in Anaconda Prompt, or use your favourite IDE.

## Authors
***

* **Chong Chee Kit** - *1004108* - [TheSpaceManatee](https://github.com/thespacemanatee)

## Acknowledgments
***

* autopep8 - formatting
* inspiration
* etc

