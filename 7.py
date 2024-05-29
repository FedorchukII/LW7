"""Подсчет гласных и согласных:
Попросите пользователя ввести строку.
Посчитайте количество гласных и согласных букв в этой строке"""


string_str = str(input("Введите строку: "))

chars1 = set('aeiouyаеёиоуыэюя')
chars2 = set('bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхчцшщ')
Achar = 0
Bchar = 0
for char in string_str.lower():
    if char in chars1:
        Achar += 1

for char in string_str.lower():
    if char in chars2:
        Bchar += 1

print(f"В строке {Achar} гласных и {Bchar} согласных")
