#Using import sys to exit the program if user decides to quit the game
import sys

#Main function calls the menu
def main():
    menu()

#Quit function 
def quit():
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
        quit()

#The playNewGame() initializes a new game from the beginning
def playNewGame():
    #temporary
    print("a new game is initialized...")

#The loadCurrentGame() opens a file to the players current level
def loadCurrentGame():
    #temporary
    print("the game is loaded...")
    

'''
The playGame() allows the user to play a new game, load an existing game,
or return to the main menu.
'''
def playGame():
    
    choice = input("""
                      1: NEW GAME
                      2: LOAD GAME
                      3: GO BACK
       
                      Please enter your choice: """)

    if choice == "1":
        playNewGame()
    elif choice == "2":
        loadCurrentGame()
    elif choice == "3":
        menu()
    else:
        print("Invalid choice, please select 1, 2, or 3.")
        playGame()

           
#The main menu()
def menu():
    print("************MAIN MENU**************")
    print()
    
    choice = input("""
                      1: PLAY GAME
                      2: QUIT

                      Please enter your choice: """)

    if choice == "1":
        playGame()
    elif choice == "2":
        quit()  
    else:
        print("You must only select 1 to play or 2 to quit.")
        print("Please try again")
        menu()    

#Main function
main()

