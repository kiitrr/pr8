while True:
    try:
        # Ввод первого числа
        a = float(input("Введите первое целое число (a): "))
        # Ввод второго числа
        b = float(input("Введите второе целое число (b): "))
        
        # Преобразуем числа в целые
        a = int(a)
        b = int(b)

        # Вывод суммы
        print("Сумма:", a + b)
    except ValueError:
        print("Ошибка: пожалуйста, введите корректные целые числа.")
