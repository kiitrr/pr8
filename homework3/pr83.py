# Функция для рисования квадрата размером size на size
def draw_square(size):
    for _ in range(size):
        print(' * ' * size)

# Ввод размера квадрата
size_input = input("Введите размер квадрата (целое число): ")

# Проверка на целое число
if size_input.isdigit() and int(size_input) == 10:
    size = int(size_input)
    draw_square(size)
else:
    print("Ошибка: размер квадрата должен быть целым числом 10.")

