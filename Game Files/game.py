
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
    + [4]: QUIT
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
            return "Exit"
    except:
        os.system("cls")
        on_start()

if on_start() == "Exit":
    os.system("exit")