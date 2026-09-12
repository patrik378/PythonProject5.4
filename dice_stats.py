import random

def simulate_dice(kolvo):
    counter_dice_1 = 0
    counter_dice_2 = 0
    counter_dice_3 = 0
    counter_dice_4 = 0
    counter_dice_5 = 0
    counter_dice_6 = 0
    for i in range(kolvo):
        roll = random.randint(1, 6)
        if roll == 1:
            counter_dice_1 += 1
        if roll == 2:
            counter_dice_2 += 1
        if roll == 3:
            counter_dice_3 += 1
        if roll == 4:
            counter_dice_4 += 1
        if roll == 5:
            counter_dice_5 += 1
        if roll == 6:
            counter_dice_6 += 1
    print(f"1: {counter_dice_1},")
    print(f"2: {counter_dice_2},")
    print(f"3: {counter_dice_3},")
    print(f"4: {counter_dice_4},")
    print(f"5: {counter_dice_5},")
    print(f"6: {counter_dice_6}")
