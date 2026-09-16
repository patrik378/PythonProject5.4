import random

# def simulate_dice(kolvo):
#     counter_dice_1 = 0
#     counter_dice_2 = 0
#     counter_dice_3 = 0
#     counter_dice_4 = 0
#     counter_dice_5 = 0
#     counter_dice_6 = 0
#     for i in range(kolvo):
#         roll = random.randint(1, 6)
#         if roll == 1:
#             counter_dice_1 += 1
#         if roll == 2:
#             counter_dice_2 += 1
#         if roll == 3:
#             counter_dice_3 += 1
#         if roll == 4:
#             counter_dice_4 += 1
#         if roll == 5:
#             counter_dice_5 += 1
#         if roll == 6:
#             counter_dice_6 += 1
#     print(f"1: {counter_dice_1},")
#     print(f"2: {counter_dice_2},")
#     print(f"3: {counter_dice_3},")
#     print(f"4: {counter_dice_4},")
#     print(f"5: {counter_dice_5},")
#     print(f"6: {counter_dice_6}")

##2
def square_number(n: int) -> int:
    """Выдаёт квадраты чисел"""
    return n * n

##3
def is_even(n: int) -> bool:
    """Если чётное -> True, иначе -> False"""
    if n % 2 == 0:
        return True
    else:
        return False

##4
def repeat_text(text: str, times: int) -> str:
    """Повторяет {text} n {times}"""
    return text * times


##5
def max_of_two(a: int, b: int) -> int:
    """Большее из двух чисел"""
    return max(a, b)

##6
def format_card(name: str, age: int, city: str) -> str:
    """Карточка о человеке"""
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print(f"Город: {city}")

##7
def save_divide(delimoe: int, delitel: int) -> int:
    """находит частное (a:b) двух чисел"""
    return delimoe / delitel

##8
def found_symbol(text: str, symbol: str) -> int:
    """находит и считает нужный символ в тексте"""
    symbol_counter = 0
    for x in text:
        if x == symbol:
            symbol_counter += 1
    return symbol_counter