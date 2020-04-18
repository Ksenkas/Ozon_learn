#загадать число
import random
clue = random.randint (1, 20)
#print (clue)

print("Отгадай число ^_^")
print("Я загадываю число от 1 до 20.")
print("Твоя задача отгадать его. Количестов попыток зависит от уровня сложности.")

#задаем ко-во попыток
steps = [0, 12, 9, 6]
level = int(input ("Выбери уроверь сложности 1, 2 или 3: "))
while 1 > level or level > 3:
    level = int(input("Можно выбрать только 1, 2 или 3! Выбери уровень: "))
counter = steps [level]
print("Ок, играем на уровне: ", level, "|", end=' ')

#игра
user = 0
while user != clue and counter != 0:
    print("Попыток: ", str(counter))
    counter -= 1
    user = int(input("Твой ответ: "))
    if user > clue and counter != 0:
        print("Думай, мое число меньше!")
    elif user < clue and counter != 0:
        print("Хо-Хо, мое число больше!")
    if counter == 0:
        print("Я загалал", clue)
if user != clue:
    print("Утешительное похлопывание по плечу. Ты проиграл!")
else:
    print("Не знаю как, но ты выиграл.")



#Restart
#print("bbb --")

