def get_word():
    word = input("Введите слово: ")
    return word


def palindrome(word2):
    return word2 == "".join(reversed(word2))


def task2():
    user_input = get_word()
    if palindrome(user_input):
        print("Палиндром")
    else:
        print("Не палиндром")

#проверка палиндромов
#task2()




def get_number():
    number = ""
    while number.isdigit() != True:
        number = input("Введите число: ")
    return int(number)


def prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True


def task1():
    user_num = get_number()
    if prime(user_num):
        print("Простое число")
    else:
        print("Составное число")
    print(user_num)

#проверка простых чисел
task1()






