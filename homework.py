try:
    number1 = int(input("Введите число: "))
    number2 = int(input("Введите число: "))
    result = number1/number2
except ValueError:
    print("Введено не число!")
except ZeroDivisionError:
    print("Число не равно нулю")
else:
    print(f"Результат: {result}")
finally:
    file.close()
    print("Программа завершена")