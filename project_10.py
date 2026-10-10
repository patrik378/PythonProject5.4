from project_10_functions import *

## карточки

cards = [{"question": "как называется язык, в котором написана эта программа?","answer": "питон"},
         {"question": "какой сейчас год?", "answer": "2026"},
         {"question": "что значит car на русском?", "answer": "машина"},
         {"question": "что значит cat на русском?", "answer": "кошка"}]


new_card = {}
correct_answers = 0
score_percent = 0
error_answers = []
question_cards = []


while True:
    print(f'---тренажёр карточек---\n1. создать карточку\n2. играть в карточки\n3. выход')

    your_choice = input().lower().strip()

    if your_choice == '1':
        new_card = add_cards(new_card)
        for i in cards:
            if new_card['answer'] == i['answer'] or new_card['question'] == i['question']:
                print(f"ошибка! такая карточка уже есть")
                break
        else:
            cards.append(new_card)

    elif your_choice == '2':
        while True:
            print(f'вы играете в карточки')
            play_cards(cards)

            print(f'хотели бы сыграть ещё раз?\n1. да\n2. нет')
            your_choice = input().lower().strip()
            found_empty_string(your_choice)
            if your_choice == '2':
                break

    elif your_choice == '3':
        break
