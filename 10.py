"""FizzBuzz: Напишите программу, которая выводит числа от 1 до 100.
Но для чисел, кратных трём, вместо числа выведите “Fizz”, а для чисел, кратных пяти, выведите “Buzz”.
Для чисел, кратных как трём, так и пяти, выведите “FizzBuzz”."""
three = 3
five = 5

for i in range(1,101):
    if i == three and i != five:
        print("Fizz")
        three += 3
    elif i != three and i == five:
        print("Buzz")
        five += 5
    elif i == three and i == five:
        print("FizzBuzz")
        three += 3
        five += 5
    else:
        print(i)