import random
import math
from enum import nonmember


def answer_question(questions, correct_answers):
    """проверка ответа"""
    answer = input().lower().strip()
    while answer == '':
        print("Вы ввели пустую строку, введите ещё раз ваш ответ")
        answer = input("ответ: ").lower().strip()
    if answer == questions["answer"]:
        print("верно")
        correct_answers += 1
    else:
        print("неверно")
    return correct_answers

def result(correct_answers):
    """говорит результат в зависимости от процентов
       правильных ответов от всех вопросов"""

    if correct_answers == 100:
        print(f"отлично!")
    elif correct_answers > 50:
        print(f"неплохо, но можно и лучше")
    elif correct_answers == 50:
        print(f"вы ответили ровно на половину вопросов верно, неплохо")
    elif correct_answers < 50:
        print(f"пока слабо, стоит повторить материал")