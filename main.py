# Using import sys to exit the program if user decides to quit the game
import sys
from Game.game import Game


# Main function calls the menu
def main():
    menu()


# Quit function
def quit_game():
    print("Are you sure you want to quit?")
    choice = input("""
                      1: YES
                      2: NO

                      Please enter your choice: """)

    if choice == "1":
        sys.exit
    elif choice == "2":
        menu()
    else:
        print("You can only select 1 for yes or 2 for no")
        quit_game()


# The playNewGame() initializes a new game from the beginning
def play_new_game():
    print()
    print("a new game is initialized...")
    game = Game()
    game.start_game()


# The loadCurrentGame() opens a file to the players current level
def load_current_game():
    print()
    print("the game is loaded...")
    game = Game()
    game.load_game()


'''
The playGame() allows the user to play a new game, load an existing game,
or return to the main menu.
'''


def play_game():
    choice = input("""
                      1: NEW GAME
                      2: LOAD GAME
                      3: GO BACK

                      Please enter your choice: """)

    if choice == "1":
        play_new_game()
    elif choice == "2":
        load_current_game()
    elif choice == "3":
        menu()
    else:
        print("Invalid choice, please select 1, 2, or 3.")
        play_game()


# The main menu()
def menu():
    print("************MAIN MENU**************")
    print()

    choice = input("""
                      1: PLAY GAME
                      2: QUIT

                      Please enter your choice: """)

    if choice == "1":
        play_game()
    elif choice == "2":
        quit_game()
    else:
        print("You must only select 1 to play or 2 to quit.")
        print("Please try again")
        menu()


# Main function
if __name__ == '__main__':
    main()
