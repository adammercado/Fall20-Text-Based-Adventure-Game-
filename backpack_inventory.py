from Item import Item
import random
backpack_list = []


# These are the commands that can be used to look at and manipulate objects in the backpack


def display_backpack_menu(backpack_list):
    random.shuffle(backpack_list)
    print()
    print("Backpack menu\n")
    print("What would you like to do?\n")
    print("show - Show all objects")
    print("grab - Grab an object")
    print("drop - Drop an object")
    print("exit - Exit the menu\n")


"""def invalid_number(num):
    try:
        x = backpack_list[num]
        return False
    except IndexError:
        return True"""


def show(backpack_list):
    for (i, item) in enumerate(backpack_list):
        print(i, item)
    print()


def grab(backpack_list):
    item = input("Name: ")
    backpack_list.append(item)
    print(item + " was added to your backpack.\n")


def drop(backpack_list):
    number = int(input("Which Item Number do you want to drop?: "))
    orig_inp = backpack_list[number]
    del backpack_list[number]
    print("'{}' was deleted.\n".format(orig_inp))
    """if invalid_number(number):
        print("Invalid item number.\n")
    else:
        orig_inp = backpack_list[number]
        del backpack_list[number]
        print("'{}' was deleted.\n".format(orig_inp))"""


def main():
    backpack_list = ["tome", "walking stick", "compass"]
    display_backpack_menu(backpack_list)
    while True:
        command = input("Enter the option you want: ").lower()
        if command == "show":
            show(backpack_list)
        elif command == "grab":
            grab(backpack_list)
        elif command == "drop":
            drop(backpack_list)
        elif command == "exit":
            break
        else:
            print("That's not a valid command, please try again. \n")


if __name__ == '__main__':
    main()
