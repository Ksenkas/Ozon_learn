# сегодня мы с вами попробуем выступить в роли детектива
# у нас есть множество людей, которые пользуется машинной марки, которую пользуется убийца
# есть множество людей, которые живут недалеко от мест преступления
# и множество людей, у которых и работа недалеко от мест преступления
# имена обычно значения неуникальные, но предплоложим, это были бы номер соц страховок

shevrole_owner = ['sam', 'edit', 'semen', 'petr']
work_near = ['konstantin', 'vladislav', 'sam', 'petr', 'edit']
live_near = ['john', 'vladislav', 'olga', 'mike', 'grant', 'covid', 'bilbo']
suspect = []

#убрали дубли из 2 списков
suspect.extend(work_near + live_near)
suspect = list(dict.fromkeys(suspect))
print(suspect)



