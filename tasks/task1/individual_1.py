#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Используя замыкания функций, определите вложенную функцию, которая бы увеличивала
значение переданного параметра на 3 и возвращала бы вычисленный результат. Вызовите
внешнюю функцию для получения ссылки на внутреннюю функцию и присвойте ее
переменной с именем cnt. Затем, вызовите внутреннюю функцию через переменную cnt со
значением k, введенным с клавиатуры.
"""

from fun import fun1


if __name__ == '__main__':
    # Запрашиваем переменную с клавиатуры
    k = float(input("Введите число: "))

    # Присваеваем внешней функции новую переменную
    cnt = fun1(k)

    # Вызов внутренней функции через переменную cnt
    print(cnt)
