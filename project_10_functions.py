import random
import math

def answer_question(questions, correct_answers):
    answer = input().lower().strip()
    if answer == questions["answer"]:
        print("верно")
        correct_answers.append(questions["answer"])
    else:
        print("неверно")
    return correct_answers