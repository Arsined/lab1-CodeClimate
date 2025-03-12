import math
import random


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_of_three(a, b, c):
    return lcm(lcm(a, b), c)


def lcm_game_logic(round):
    a, b, c = (random.randint(1, 20), random.randint(1, 20),
               random.randint(1, 20))
    question = f"{a} {b} {c}"
    correct_answer = lcm_of_three(a, b, c)
    return question, correct_answer
