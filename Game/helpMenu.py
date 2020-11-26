from TextParser.textParser import TextParser

def displayHelpMenu():
    parser = TextParser()
    print("\n")
    print("**** HELP MENU ****")
    print("1. List Look Actions")
    print("2. List Move Actions")
    print("3. List Move Directions")
    print("4. List Use Actions")
    print("5. List Take Actions")
    print("6. List Place Actions")
    print("7. List Game Actions")
    print("8. List Look Prepositions")
    print("9. List Use Prepositions")
    print("10. List Game Items")
    print("11. List Features")
    print("\n")

    choice = input("Enter the number of your choice: ")
    print("\n")
    if choice == "1":
        for look_action in parser.look_actions:
            print(look_action)
    elif choice == "2":
        for move_action in parser.move_actions:
            print(move_action)
    elif choice == "3":
        for move_direction in parser.move_directions:
            print(move_direction)
    elif choice == "4":
        for use_action in parser.use_actions:
            print(use_action)
    elif choice == "5":
        for take_action in parser.take_actions:
            print(take_action)
    elif choice == "6":
        for place_action in parser.place_actions:
            print(place_action)
    elif choice == "7":
        for game_action in parser.game_actions:
            print(game_action)
    elif choice == "8":
        for look_preposition in parser.look_prepositions:
            print(look_preposition)
    elif choice == "9":
        for use_preposition in parser.use_prepositions:
            print(use_preposition)
    elif choice == "10":
        for item in parser.item_list:
            print(item)
    elif choice == "11":
        for feature in parser.feature_list:
            print(feature)
    else:
        print("Invalid menu choice. Please enter a valid number")
    print("\n")
