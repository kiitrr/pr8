total_sum = 0

while True:
    user_input = input("Введите число (или 'stop'/'end' для завершения): ")

    if user_input.lower() in ['stop', 'end']:
        break

    try:
   
        number = float(user_input)
        

        if number.is_integer():
            total_sum += int(number)  
        else:
            print("Ошибка: введено нецелое число. Пожалуйста, введите целое число.")
    except ValueError:
        print("Ошибка: введено некорректное значение. Пожалуйста, введите число.")
print("Сумма введенных целых чисел:", total_sum)
