#
# # модули пайтона
#
# import random, time, math
# print (random.randint(1, 100))
# #
# #  7 85 10 6 4 50
# # 1-й модуль - встроенные
#
# from math import pi, e, sin, cos, tan
# print(pi)
# print(e)
# # print(sin)
#
# # 2-й модуль -
#
# from Lesson1 import Big0
# f=Big0()
#
# if __name__ == '__main__':
#     print(pi)
#     print(pi)
#     print(pi)
#
# from lessons import Lesson3
#
# Lesson3.Big0
#

# 3-й модуль - внешние (нужно сперва скачать)
# загружать виртуальное окружение - venv

import colorama as col
from art import tprint

print(col.Fore.Magenta,col.Back.GREEN)
tprint('Hello World')

#
