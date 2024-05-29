"""Палиндром: Проверьте, является ли введенная пользователем строка палиндромом
(читается одинаково как слева направо,
так и справа налево, игнорируя пробелы, знаки препинания и регистр)."""

string_str = str(input("Введите строку: "))

chars = set('abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя')
cleaned_string = ''
for char in string_str.lower():
    if char in chars:
        cleaned_string += char

if ''.join(reversed(str(cleaned_string))) == str(cleaned_string):
    print("Это Палиндром")
else:
    print("Это не Палиндром")