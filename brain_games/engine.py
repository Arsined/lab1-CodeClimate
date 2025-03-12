def run_game(game_logic):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for round in range(3):
        question, correct_answer = game_logic(round)
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if str(user_answer) == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
