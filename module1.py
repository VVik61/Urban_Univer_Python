# # import module2 as m2
#
# # включение в глобальное пространство имен
# # from module2 import a, b, sey_hi   # можно ставить * т.е. - импорт. ВСЁ
# from module2 import sey_hi as sh
#
# # import module2 as m2
#
# print("Привет, я из модуля 1")
#
# # sey_hi()
#
# # print(m2.__name__)
#
# sh()

import sys

for path in sys.path:
    print(path)
