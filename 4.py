"""Проверка на простоту: Попросите пользователя ввести целое число больше 1.
Определите, является ли это число простым (т.е., делится только на себя и на 1)."""

number_int = int(input("Введите целое число больше 1: "))

counter = 0
for i in range(2, number_int):
    if number_int % i == 0:
        counter += 1
if counter == 0:
    print("Простое число")
else:
    print("Составное число")

