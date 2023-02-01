def inpt(n):
    print('Заполните элементы массива')
    x = [int(input()) for i in range(n)]
    print('Исходный массив', x)
    print(int(sum(x) / len(x)))


print('Введите размер массива')
inpt(int(input()))
