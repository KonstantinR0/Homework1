try:
    number1 = int(input("Введите число: "))
    number2 = int(input("Введите число: "))
    result = number1 / number2
except ValueError:
    print("Введено не число!")
except ZeroDivisionError:
    print("Нельзя делить на 0!")
else:
    print(f"Результат: {result}")
finally:
    print("Программа завершена")