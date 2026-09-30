from project_10_functions import *

cards = [{"question": "как называется язык, в котором написана эта программа?","answer": "питон"},
         {"question": "какой сейчас год?", "answer": "2026"},
         {"question": "что значит car на русском?", "answer": "машина"},
         {"question": "что значит cat на русском?", "answer": "кошка"}]
correct_answers = 0
score_percent = 0


while True:
    while correct_answers != 4:
        question = random.randint(0, 3)
        print(cards[question]["question"])
        correct_answers = answer_question(cards[question], correct_answers)

    print(f"вы ответили на все вопросы правильно, поздравляю!")
    correct_answers = 0
    print("хотите ещё?")

    otvet = input("напишите, 1 (да) или 2 (нет) ").strip()

    while otvet == '':
        print("вы написали пустую строку, повторите ваш вариант ответа")
        otvet = input("ответ: ").strip()
    while otvet != '1' and otvet != '2':
        print("такого варианта нет, повторите ваш ответ")
        otvet = input("введите ответ ещё раз ").strip()
    if otvet == '2':
        break

