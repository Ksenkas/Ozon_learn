import random


#ставка
slot = list(range(0, 37))
color_list = ['красное', 'черное', 'ЗЕРО']
print(*color_list)
print(*slot)

#анализ
bet_clr = 0
a = 0
while a != 1:
    bet = input("Делайте ваши ставки, господа, от 0 до 36 или красное и черное: ")
    if isinstance(bet, str):
        bet.lower()
        if str(bet) == 'красное':
            bet_clr = color_list[0]
            a = 1
            print('Играет красное!')
        if str(bet) == 'черное':
            bet_clr = color_list[1]
            a = 1
            print('Играет черное!')
    elif isinstance(bet, int):
        if int(bet) in range(0, 37):
            a = 1
            print('Го3')

spin = random.choice(slot)
i = spin
clr = 5
if i in range(1, 11) or i in range(19, 29):
    if i%2 != 0:
        clr = color_list[0]
    else:
        clr = color_list[1]
elif i in range(11, 19) or i in range(29, 37):
    if i % 2 != 0:
        clr = color_list[1]
    else:
        clr = color_list[0]
else:
    clr = color_list[2]
#результат
print('Выпало', end=' ')
print(i, clr)


if spin == bet or bet_clr == clr:
    print('winner')
else:
    print('loser')


#
# num = int(input("Под какое количество патронов обойма?: "))
# real_bullets = int(input("Сколько патронов в обойме?: "))
# bullets = [0 for i in range(num-real_bullets)]
# bullets += [1 for j in range(real_bullets)]
# print(bullets)
#
# a = input("Точно хочешь сыграть? Если да, то напиши 1, а если нет, то 0: ")
#
# while a == "1":
#     if random.choice(bullets) == 1:
#         print("Ты проиграл!!! Хочешь сыграть ещё раз?")
#     else:
#         print("Ты выиграл!!! Хочешь сыграть ещё раз?")
#     a = input("Если да, то напиши 1, а если нет, то 0: ")
# print("Спасибо за игру!")