def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
inner_function()

# РЕЗУЛЬТАТ
# Функция inner_function() не сработает:
# Ошибка  NameError: name 'inner_function' is not defined, т.е.
# inner_function - функция не определена (имя ф-ции не видно в пространстве
# имен модуля namespace.py не найдено)
