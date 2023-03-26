import random


def roll(probability):
    return random.randint(0, 100) < probability


for i in range(10):
    print(roll(30))