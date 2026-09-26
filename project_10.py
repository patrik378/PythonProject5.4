from project_10_functions import *

cards = [{"question": "как называется язык, в котором написана эта программа?","answer": "питон"},
         {"question": "какой сейчас год?", "answer": "2026"},
         {"question": "что значит car на русском?", "answer": "машина"},
         {"question": "что значит cat на русском?", "answer": "кошка"}]
correct_answers = 0
repeated_questions = []

while True:
    for i in range(len(cards)):
        question = random.randint(0, 3)
        print(cards[question]["question"])
        correct_answers = answer_question(cards[question], correct_answers)

    print(f"у вас {correct_answers} правильных ответов")
    print("хотите ещё?")

    otvet = input("напишите, 1 (да) или 2 (нет) ").strip()

    if otvet == '2':
        break

