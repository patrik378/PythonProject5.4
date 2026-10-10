import random
import math
from enum import nonmember


def answer_question(questions, correct_answers):
    """проверка ответа"""
    answer = input("ответ: ").lower().strip()
    errors = ''
    while answer == '':
        print("Вы ввели пустую строку, введите ещё раз ваш ответ")
        answer = input("ответ: ").lower().strip()
    if answer == questions["answer"]:
        print("верно")
        correct_answers += 1
    else:
        print("неверно")
        errors = questions["question"]
    return correct_answers

def repeat_errors(errors, answers):
    """прогон по ошибкам"""
    corrects = 0
    while corrects != len(errors):
        nomer = 0
        print(errors[nomer])
        answer = input().lower().strip()
        while answer == '':
            print(f"вы ввели пустую строку\nвведите ещё раз")
            answer = input().lower().strip()
        if answer == answers[nomer]:
            corrects += 1
            print(f'верно')
        else:
            print(f'неверно')


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

def found_empty_string(answer):
    """если ответ может быть пустой строкой,
     чтобы не выдавать ошибку или не тот вариант"""

    while answer == '':
        print(f"упс...\nвы ввели пустую строку! введите её ещё раз")
        answer = input().lower().strip()

def add_cards(new_card):
    """функция для добавления карточку"""

    question_for_cards = input('введите слово на английском: ').lower().strip()
    found_empty_string(question_for_cards)

    answer_for_cards = input('введите перевод для карточки: ').lower().strip()
    found_empty_string(answer_for_cards)

    new_card = {'question': f"что значит {question_for_cards}?", 'answer': answer_for_cards}
    return new_card

def play_cards(cards):
    correct_answers = 0
    score_percent = 0

    while correct_answers <  4:

        question = random.randint(1, len(cards) - 1)

        print(cards[question]['question'])

        correct_answers = answer_question(cards[question], correct_answers)

    correct_answers = 0
    score_percent = 0








