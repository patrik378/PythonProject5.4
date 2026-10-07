from project_10_functions import *

## карточки

cards = [{"question": "как называется язык, в котором написана эта программа?","answer": "питон"},
         {"question": "какой сейчас год?", "answer": "2026"},
         {"question": "что значит car на русском?", "answer": "машина"},
         {"question": "что значит cat на русском?", "answer": "кошка"}]

## все нужные переменные

correct_answers = 0
score_percent = 0
error_answers = []
question_cards = []

## меню для карточек и функции с ними

while True:
    while correct_answers != 4:
        question = random.randint(0, 3)
        print(cards[question]["question"])
        correct_answers, error_answer = answer_question(cards[question], correct_answers)
        if error_answer != '':
            question_cards.append(cards[question]['answer'])
            error_answers.append(error_answer)

    ## проверка на кол-во ошибок

    if len(error_answers) == 0:
        print(f'вы ответили на всё верно')
    else:
        print(f"вы ответили почти на все вопросы правильно, поздравляю!")
        print(f"ошибки: {error_answers}\nповторите и запустите программу заного")


    ## сбрасываем все переменные

    correct_answers = 0
    question_cards = []
    error_answers = []

    ## хочет ли пользователь сыграть снова?

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

