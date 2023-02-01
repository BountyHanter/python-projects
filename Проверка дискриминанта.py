def sqr(a, b, c):
    d = b ** 2 - 4 * a * c
    print('Уравнение имеет решение' if d < 0 else 'Уравнение не имеет решения')


sqr(int(input()), int(input()), int(input()))