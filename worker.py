import copy

from main import Vector


def read():
    first_vector = int(input("Введіть вектор: "))
    number = int(input("Введіть скаляр: "))
    second_vector = int(input("Введіть другий вектор: "))
    working = Vector(first_vector)
    print("Скалярний добуток: ", working * number)
    print("Різниця векторів:", first_vector - second_vector)
    print("Норма вектора: ", working.norm())


read()
