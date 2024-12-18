import random

def intro():
    print("Welcome to the Cave Adventure!")
    print("You are standing at the entrance of a dark cave.")
    print("You can go 'left' or 'right'. What do you choose?")

def left_path():
    print("\nYou chose to go left.")
    print("You walk deeper into the cave and find a treasure chest!")
    print("Do you want to open it? (yes/no)")

    choice = input("> ").strip().lower()
    if choice == "yes":
        if random.random() < 0.7:  # 70% chance of finding treasure
            print("Congratulations! You found a pile of gold!")
        else:
            print("Oh no! The chest was a trap! You fell into a pit.")
            game_over()
    elif choice == "no":
        print("You wisely decided not to open the chest and safely return to the entrance.")
        start_game()
    else:
        print("Invalid choice. Try again.")
        left_path()

def right_path():
    print("\nYou chose to go right.")
    print("You encounter a hungry bear!")
    print("Do you want to 'run' or 'stay'?")

    choice = input("> ").strip().lower()
    if choice == "run":
        print("You managed to escape the bear and return to the entrance!")
        start_game()
    elif choice == "stay":
        print("The bear attacks you! You have been defeated.")
        game_over()
    else:
        print("Invalid choice. Try again.")
        right_path()

def game_over():
    print("Game Over! Would you like to play again? (yes/no)")
    choice = input("> ").strip().lower()
    if choice == "yes":
        start_game()
    else:
        print("Thanks for playing!")

def start_game():
    intro()
    choice = input("> ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Try again.")
        start_game()

if __name__ == "__main__":
    start_game()
