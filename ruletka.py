import random


#ставка
slot = list(range(0, 37))
color_list = ['красное', 'черное', 'ЗЕРО']
print(*color_list)
print(*slot)

#проверка
bet_clr = 0
a = 0
while a != 1:
    bet = input("Делайте ваши ставки, господа, от 0 до 36 или красное и черное: ")
    if bet.isdigit():
        if int(bet) in slot:
            a = 1
            print('Го3')
    else:
        bet.lower()
        if str(bet) == 'красное':
            bet_clr = color_list[0]
            a = 1
            print('Играет красное!')
        if str(bet) == 'черное':
            bet_clr = color_list[1]
            a = 1
            print('Играет черное!')

#  результат
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

#итог
print('Выпало', end=' ')
print(i, clr)


if str(spin) == bet or bet_clr == clr:
    print('winner')
else:
    print('loser')
