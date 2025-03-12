import random


def generate_geometric_progression(length, ratio):
    return [ratio ** i for i in range(length)]


def progression_game_logic(round):
    length = random.randint(5, 10)
    ratio = random.randint(2, 5)
    progression = generate_geometric_progression(length, ratio)
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
