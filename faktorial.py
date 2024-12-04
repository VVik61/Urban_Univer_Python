"""
Код для вычисления факториала
Источник https://www.cyberforum.ru/python-beginners/thread3186219.html
"""

def f(n):
    print('start=',n)
    if n<=1:
        return 1
    else:
        a = n*f(n-1)
        print(a)
        return a



if __name__ == '__main__':
    print(f(5))
