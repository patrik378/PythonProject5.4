from dice_stats import *
import time

while True:
    print("вы используете utility hub!", "выбирайте один и пунктов: 1)(ограничить число), 2)(отчёт об окружности), 3)(отчёт о тексте), 4)(выход)", sep="\n")
    users_choice = int(input())
    if users_choice == 1:
        user_number = int(input("введите число: "))
        user_start_number = int(input("введите начальное число: "))
        user_end_number = int(input("введите конечное число: "))
        print(num_limit(user_start_number,user_number, user_end_number))
    elif users_choice == 2:
        user_radius = int(input("радиус круга: "))
        print(circle_report(user_radius))
    elif users_choice == 3:
        user_text = input("введите вашу строку: ")
        text_report(user_text)
    elif users_choice == 4:
        print("выход...")
        time.sleep(1.5)
        break
