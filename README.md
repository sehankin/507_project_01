If this is your first time cloning something from GitHub,
you should consult the GitHub documentary on doing so:
https://help.github.com/articles/cloning-a-repository/

The primary purpose of the code found in SI507F17_project1_cards.py
is to simulate the card game War.  To do this, the code first defines
two classes: Card, which mimics real playing cards by way of variables
such as suit and rank; and Deck, which begins as a set of 52 Card objects
and has methods useful for gameplay such as shuffling and dealing.
The function play_war_game (which takes no input) creates two players,
each equipped with a full Deck, and proceeds to simulate the entire game,
trick by trick, returning the following tuple:
({player who won}, {player 1's score}, {player 2's score})

The file SI507F17_project1_tests.py ran many tests on the code in
SI507F17_project1_cards.py, revealing the following bugs:
-the Card class's string method does not convert (e.g.) "12 of Spades"
to "Queen of Spades" as it's supposed to
-the same is true of the Deck class's string method
-a Deck's sort_cards function, which is supposed to order a Deck's cards
by suit, does not do so if the deck does not have the full 52 cards
-a Deck's deal_hand function will not deal hands greater than 26 cards,
even if the Deck has the full 52 cards

Also included in SI507F17_project1_cards.py is the function show_song,
which takes a string as input and searches for that string on iTunes,
returning a single Song object (whose class variables include title, artist,
and album).

The file SI507F17_project1_cards.py relies on the functions in the file
helper_functions.py for the show_song function to work,
and so its "import helper_functions" statement should be left alone.

This code is best run with Python 3 in a virtual environment.
If you do not already have VirtualEnv installed, run the following command
in your command line:
pip3 install virtualenv

To create a virtual environment, enter the command:
virtualenv --python=python3 {NAME YOU WANT TO GIVE THE VIRTUAL ENVIRONMENT}

To activate the virtual environment, enter the command:
source {SAME NAME}/bin/activate

You will know the virtual environment has been activated when you see its name
in parentheses before your command prompt.  You can deactivate
a virtual environment at any time by entering:
deactivate

You will need to equip your virtual environment with the requests module,
which is not in the Python standard library.  This is best done by installing
the requirements.txt file included in this folder, which will install requests
and the other modules it requires.  To do so, make sure your virtual
environment is activated and then enter this command in the command line:
pip install -r requirements.txt

You're ready to use this code!  Remember, the show_song function searches
for a string that you enter as a parameter, while the play_war_game function
can be called without need of a parameter.  
