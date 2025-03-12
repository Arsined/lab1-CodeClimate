from engine import run_game
from games.lcm_game import lcm_game_logic
from games.progression_game import progression_game_logic


def main():
    print("Choose a game to play:")
    print("1. LCM Game")
    print("2. Geometric Progression Game")

    choice = input("Enter the game number: ")

    if choice == '1':
        run_game(lcm_game_logic)
    elif choice == '2':
        run_game(progression_game_logic)
    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
