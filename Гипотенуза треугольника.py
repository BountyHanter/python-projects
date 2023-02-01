import math


def hyp(x, y):
    print("%.3f" % (math.sqrt(x ** 2 + y ** 2)))


hyp(int(input()), int(input()))
