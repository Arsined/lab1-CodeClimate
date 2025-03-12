import math
import random


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_of_three(a, b, c):
    return lcm(lcm(a, b), c)


def play_lcm_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")

    for _ in range(3):  # Number of questions
        a, b, c = (random.randint(1, 20), random.randint(1, 20),
                   random.randint(1, 20))
        print(f"Question: {a} {b} {c}")
        user_answer = int(input("Your answer: "))
        correct_answer = lcm_of_three(a, b, c)

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def generate_geometric_progression(length, ratio):
    return [ratio ** i for i in range(length)]


def play_geometric_progression_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    for _ in range(3):  # Number of questions
        length = random.randint(5, 10)
        ratio = random.randint(2, 5)
        progression = generate_geometric_progression(length, ratio)
        hidden_index = random.randint(0, length - 1)
        hidden_number = progression[hidden_index]
        progression[hidden_index] = '..'

        print(f"Question: {' '.join(map(str, progression))}")
        user_answer = int(input("Your answer: "))

        if user_answer == hidden_number:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{hidden_number}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


play_lcm_game()


play_geometric_progression_game()

