
number = int(input('Введите произвольное целое число:'))
while number // 10:
    print(number % 10)
    number = number // 10
print(number)
