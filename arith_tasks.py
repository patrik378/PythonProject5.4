import math
import random

def generate_tasks(kolvo):
    counter = 0
    incorrect_counter = 0
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    znaki = ["-", "+"]
    for i in range(kolvo):
        first_number = random.randint(1, 10)
        random_znaki = random.choice(znaki)
        second_number = random.randint(1, 10)
        if random_znaki == "+":
            answer = int(input(f"{first_number}+{second_number} = "))
            if answer == first_number + second_number:
                counter += 1
            else:
                incorrect_counter += 1
        elif random_znaki == "-":
            answer = int(input(f"{first_number}-{second_number} = "))
            if answer == first_number - second_number:
                counter += 1
            else:
                incorrect_counter += 1
    print(f"правильных: {counter}, неправильных: {incorrect_counter}")
