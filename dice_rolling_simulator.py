import random

print("----------------------")
print("    Dice Simulator    ")
print("----------------------\n")


UserInput = int(input("How many times do you want to roll the dice?  "))
for i in range(UserInput):
    number = random.randint(1, 6)
    if number == 1:
        print("----------")
        print("|         |")
        print("|    *    |")
        print("|         |")
        print("----------")
    if number == 2:
        print("----------")
        print("|         |")
        print("|  *   *  |")
        print("|         |")
        print("----------")
    if number == 3:
        print("----------")
        print("|    *    |")
        print("|    *    |")
        print("|    *    |")
        print("----------")
    if number == 4:
        print("----------")
        print("|  *   *  |")
        print("|         |")
        print("|  *   *  |")
        print("----------")
    if number == 5:
        print("----------")
        print("|  *   *  |")
        print("|    *    |")
        print("|  *   *  |")
        print("----------")
    if number == 6:
        print("----------")
        print("|  *   *  |")
        print("|  *   *  |")
        print("|  *   *  |")
        print("----------")

