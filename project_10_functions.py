import random
import math

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