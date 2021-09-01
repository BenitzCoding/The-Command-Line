
"""

Copyright (c) 2021 Benitz Original.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

from imports import *

Start_Screen = """
#----------------------#
|   THE COMMAND LINE   |
#----------------------#

    + [1]: START
    + [2]: HELP
    + [3]: CREDITS
    + [4]: ENTER CODE
    + [5]: QUIT
\n"""
Input = "> "
Invalid = "[Unrecognised Action]\n"

def generate_tasks():
    option = [ "Task", "Scenario" ]
    task_list = [ 
        "Open the gift box.",
        "Turn on the light outside your house.",
        "Go get some food to eat.",
        "Do your homework.",
        "Buy groceries from the convienent store across the street."
    ]
    scenario_list = [ 
        "There is a knock on the door, what do you do?",
        "You feel like someone is staring at you, but there is no-one anywhere near you, what do you do?",
        "You're driving home from work and you hear a distant baby crying, what do you do?",
        "There is blood seeping out from underneth your bed, what do you do?",
        "That was all just a nightmare or... Was it? It looked too real for it to be a dream.",
        "While you were walking home from buying groceries, and on the way home someone is chasing you with a knife."
    ]

    if random.choice(option) == "Task":
        return random.choice(task_list)

    else:
        return random.choice(scenario_list)

def display_credits():
    print("""
#---------------------#
|       CREDITS       |
#---------------------#

[Github]: https://github.com/BenitzCoding/The-Command-Line
[License]: MIT
[Owner]: Benitz Original
[Discord]: Benitz Original#1317
[Website]: https://benitz.me
\n""")
    input("[ENTER TO CONTINUE]\n> ")

def help_action():
    print("""
#----------------------#
|         HELP         |
#----------------------#

When you start the game you will get a task to do
and you have to complete that task by typing it out,
indirectly do finish the task, or sometimes you can
do anything in that scenario. This can lead to very
interesting sentences and this is a interesting game

If you try to just simply type to do the task it would
be a "Unrecognised Action", you will have to make
sentences that means the same thing but say it differently.
\n""")
    input("[ENTER TO CONTINUE]\n> ")

def enter_code():
    code = input("""
#----------------------#
|      ENTER CODE      |
#----------------------#
\n> """)

    if code == "HypeAllTheWay":
        print("This game is still in progress, if you know this code, then you probably are a Python Developer or you got this code from the owner. No matter What it is, you should star and watch this game in the github page, anyway have a nice day!\n\nhttps://github.com/BenitzCoding/The-Command-Line")
        input("\n[ENTER TO CONTINUE]\n> ")

    elif code == "secrets...":
        print("This is neither a horror game nor a story telling game. It's just a command line, tell a good tale to live another day to tell another tale. Mess up a interesting game and fall to your voided death.\n\nRoses are dead, violets are dying, Survive the night, but will one day meet death.")
        print(Style.BRIGHT + Fore.RED + "\n[ENTER TO CONTINUE]")
        input("> ")

def on_start():
    os.system("cls")
    try:
        print(Start_Screen)
        user_input = int(input(Input))
        if user_input == 1:
            os.system("cls")
            start_action()

        elif user_input == 2:
            os.system("cls")
            help_action()
            on_start()

        elif user_input == 3:
            os.system("cls")
            display_credits()
            on_start()

        elif user_input == 4:
            os.system("cls")
            enter_code()
            on_start()

        elif user_input == 5:
            os.system("cls")
            return "Exit"

        else:
            print("[INVALID OPTION ENTER TO CONTINUE]\n> ")
    except:
        os.system("cls")
        on_start()

if on_start() == "Exit":
    os.system("exit")