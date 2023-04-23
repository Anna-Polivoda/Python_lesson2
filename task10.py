# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


n = int(input('Введите кол-во монет на столе: '))
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input('Введите поочередно стороны монет 0 или 1 : '))
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
if count_zero < count_one:
    print(f"Необходимо перевернуть {count_zero} монет")
else:
    print(f"Необходимо перевернуть {count_one} монет")


# import random
# n = int(input('Введите кол-во монет на столе: '))
# sides = list()
# for i in range(n):
#     sides.append(random.randint(0,1))
# print('Стороны монет: ', *sides, '(где 0 - решка, 1 - орел)')
# count_0 = 0
# count_1 = 0
# for i in range (n):
#     if sides[i] == 0:
#         count_0 += 1
#     else:
#         count_1 += 1
# if count_0 < count_1:
#     print("Необходимо перевернуть ", count_0, " монет")
# else:
#     print("Необходимо перевернуть ", count_1, " монет")

