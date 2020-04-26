number = int(input())
stroka = str(number)
spisok = list(stroka)
#разгые сортировки
#sorted_spisok = reversed(sorted(spisok))
sorted_spisok2 = sorted(spisok, reverse=True)
print(*spisok)