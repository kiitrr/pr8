def is_integer(n):
    try:
        float_n = float(n)
        return float_n.is_integer()
    except ValueError:
        return False


a = input("Введите первое число (a): ")
b = input("Введите второе число (b): ")
