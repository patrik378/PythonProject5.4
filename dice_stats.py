import math
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

##1, 5.6
def clamp(value: int, min_value: int, max_value: int) -> int:
    if value < min_value:
        return min_value
    if value > max_value:
        return max_value
    return value

##2, 5.6
def build_full_name(first_name: str, last_name: str, middle_name: str ="") -> str:
    """выдаёт фамилию имя отчество"""
    return f"{build_correct_name(first_name)} {build_correct_name(last_name)} {build_correct_name(middle_name)}"

def build_correct_name(first_name: str) -> str:
    correct_first_name = ""
    if first_name[0] == " " or first_name[-1] == " ":
        correct_first_name = first_name.replace(" ", "")
    else:
        correct_first_name = first_name
    return correct_first_name.capitalize()

##3, 5.6
def normalize_space(text: str) -> str:
    """убирает лишние пробелы"""
    return " ".join(text.split())

def count_words(text: str) -> int:
    """считает слова (кол-во всех слов)"""
    return len(text.split())
def average_word_length(text: str) -> int:
    """считает среднюю длину слов"""
    word_length = []
    for i in text.split():
        word_length.append(len(i))
    average = sum(word_length) / len(word_length)
    return average

##4, 5.6
def calc_discount_price(price: int, discount: int) -> float:
    """считает цену со скидкой для товара"""
    return price * (1 - discount / 100)

def calc_total(price: int, kolichestvo: int) -> int:
    """итоговая стоимость"""
    return price * kolichestvo

def build_receipt(name: str, price: int, quantity: int, discount: int) -> str:
    """ввыдаёт чек"""
    return  (f"Товар: {name}\n"
            f"Цена со скидкой: {calc_discount_price(price, discount)}\n"
            f"Количество: {quantity}\n"
            f"Итого: {calc_discount_price(price, discount) * quantity}\n")


##5, 5.6
def build_scores_table(names: list, scores: list) -> list:
    """выдаёт имя и его балл"""
    names_and_scores = zip(names, scores)
    for no, score in enumerate(names_and_scores, 1):
        print(f"{no}) {score[0]} - {score[1]}")

##6, 5.6
def circle_length(radius: int) -> float:
    """длина окружности"""
    return 2*math.pi*radius
def circle_area(radius: int) -> float:
    """площадь круга"""
    return math.pi*(radius**2)
def circle_report(radius: int) -> float:
    """отчёт об окружности"""
    print(f"Радиус: {circle_length(radius)}\nДлина: {circle_length(radius)}\nПлощадь: {circle_area(radius)}")

##7, 5.6
def pick_char(alphabet: str) -> str:
    """выбирает рандомный символ из alphabet"""
    return random.choice(alphabet)
def build_password(length: int, alphabet: str) -> str:
    """генератор паролей"""
    password = ""
    for i in range(length):
        random_reester = random.randint(1,2)
        if random_reester == 1:
            password += pick_char(alphabet).lower()
        elif random_reester == 2:
            password += pick_char(alphabet).upper()
    return password

##8, 5.6
def num_limit(start=0, number=0, end=100) -> int:
    """ограничить число границами"""
    print(f"начало: {start}\nчисло: {number}\nконец: {end}")
def text_report(text: str) -> str:
    """отчёт о тексте"""
    print(f"текст без лишних пробелов: {normalize_space(text)}\nколичество слов: {count_words(text)}\nсредняя длина слов: {average_word_length(text)}")