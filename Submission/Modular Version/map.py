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
        DESCRIPTION: '''A strong pungent smell of rotting carcass wafts into your nose.\nYou are not alone here...\n\nA burly Troll lumbers towards you, getting ready to swing its club!\nYou have to KILL it or DIE trying!\n
░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄
░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄
░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█
░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█
░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█
█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█
█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
░░░█░░██░░▀█▄▄▄█▄▄█▄████░█
░░░░█░░░▀▀▄░█░░░█░███████░█
░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█''',
        INSPECT: 'examine',
        TASK: 'task',
        SOLVED: 'solved',
        UP: 'b1',
        DOWN: 'c1',
        LEFT: 'c1',
        RIGHT: 'c2',
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
        INSPECT: 'Looks like you may have to resort to kicking it down.',
        TASK: 'task',
        SOLVED: None,
        UP: 'b2',
        DOWN: 'c2',
        LEFT: 'c1',
        RIGHT: 'c3',
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
        DESCRIPTION: '''The smell of incense burns your nose. Something demonic resides here...\n\nA Witch spawned out of nowhere and prepares to cast her spell!\nYou must KILL her or DIE trying!\n 
                  /\\
                _/__\_
                /( o\\
           /|  // \-'
      __  ( o,    /\\
        ) / |    / _\\
 >>>>==(_(__u---(___ )-----
                   //
                  /__)''',
        INSPECT: None,
        TASK: None,
        SOLVED: None,
        UP: 'b3',
        DOWN: 'c3',
        LEFT: 'c2',
        RIGHT: 'c3',
        MAP_DRAWING: '''----------
|  |  |  |
----------
|  |  |  |
----------
|  |  | X|
----------'''
    },

}