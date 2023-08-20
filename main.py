# n = int(input('Введите колличество монеток: '))
# a = 0
# b = 0
# for i in range(n):
#     x = int(input('Орел(1) или решка(0)? '))
#     if x == 1:
#         a += 1
#     else:
#         b += 1
# print()
# if a > b:
#     print(f'Нужно перевернуть {b} монеток')
# elif a == b:
#     print(f'Колличество монет одинаково, по {b} штук')
# else:
#     print(f'Нужно перевернуть {a} монеток')


s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение: '))
a = 0
for x in range(s):
    for y in range(s):
        if x + y == s and x * y == p:
            a += 1
            print(x, y)