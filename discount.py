import random
import string


def get_list_from_file(file_name, func):
    with open(file_name) as input_f:
        return [func(x.strip()) for x in input_f.readlines()]


def list_format(list):
    return list.split(',')

def list_format2(element):
    return float(element)


sale = get_list_from_file('discount.txt', list_format2)
goods = get_list_from_file('goods.txt', list_format)
file_name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))


with open(file_name + ".txt", "w") as result:
    for i in range(len(sale)):
        result.write((goods[i][0]) + " " + str(float(goods[i][1]) * sale[i]) + "\n")


