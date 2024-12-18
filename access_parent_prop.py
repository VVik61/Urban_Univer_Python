"""
Цели: Применить сокрытие атрибутов и повторить наследование.
     Рассмотреть на примере объекта из реального мира.

Задача "Изменять нельзя получать":...
Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это
  любой транспорт, а Sedan(седан) - наследник класса Vehicle.
----------------------
I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:
Атрибут owner(str) - владелец транспорта. (владелец может меняться)
Атрибут __model(str) - модель (марка) транспорта.
   (мы не можем менять название модели)
Атрибут __engine_power(int) - мощность двигателя.
   (мы не можем менять мощность двигателя самостоятельно)
Атрибут __color(str) - название цвета.
   (мы не можем менять цвет автомобиля своими руками)

А так же атрибут класса:
Атрибут класса __COLOR_VARIANTS, в который записан список допустимых
  цветов для окрашивания. (Цвета написать свои)

Каждый объект Vehicle должен содержать следующий методы:
Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
Метод print_info - распечатывает результаты методов
 (в том же порядке): get_model, get_horsepower, get_color; а так же владельца
  в конце в формате "Владелец: <имя>"
Метод set_color - принимает аргумент new_color(str), меняет цвет __color
  на new_color, если он есть в списке __COLOR_VARIANTS, в противном случае
  выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".

Взаимосвязь методов и скрытых атрибутов:
Методы get_model, get_horsepower, get_color находятся в одном классе
 с соответствующими им атрибутами: __model, __engine_power, __color.
  Поэтому атрибуты будут доступны для методов.
Атрибут класса __COLOR_VARIANTS можно получить обращаясь
 к нему через объект(self).
Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').
------------------
II. Класс Sedan наследуется от класса Vehicle, а так же
 содержит следующие атрибуты:
Атрибут __PASSENGERS_LIMIT = 5
 (в седан может поместиться только 5 пассажиров)
"""
class Vehicle:
    __COLOR_VARIANTS =  ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __color, __engine_power):
        if (isinstance(owner, str) and isinstance(__model, str) and
                isinstance(__color, str) and
                isinstance(__engine_power, int)):
            self.owner = owner
            self.__model = __model
            self.__color = __color
            self.__engine_power = __engine_power
        else:
            print('Ошибка в атрибутах. Проверьте и введите их правильно!')
            exit()            # print('После exit') не будет выполнен

    def get_model(self):
        return f'Модель: {self.__model}\n' # "Модель: <название модели 'транспорта>")

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}\n' # "Мощность двигателя: <мощность>"

    def get_color(self):
        return f'Цвет: {self.__color}\n'
            # f'Цвет: {str.upper(self.__color)}'   # "Цвет: <цвет транспорта>"

    def print_info(self):
        return print(self.get_model(), self.get_horsepower(),
                     self.get_color(), f'Владелец: {self.owner}', end='\n')
        # return print('\n', self.get_model(), '\n', self.get_horsepower(),
        #              '\n', self.get_color(), '\n', f'Владелец: {self.owner}')

    def set_color(self, new_color):
        for color_tmp in self.__COLOR_VARIANTS:
            if str.upper(color_tmp) == str.upper(new_color):
                self.__color = new_color
                    # self.__COLOR_VARIANTS[ ] = new_color
                # return f'{new_color} есть в __COLOR_VARIANTS!' # можно
                # ничего не возвращать, т.е. ф-ция вернет None
        else:
            return print(f'Нельзя сменить цвет на {new_color}.')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    # По логике надо здесь ввести quantity - предельно допустимое кол-во
    # пассажиров
    def __init__(self, owner, __model, __color, __engine_power):
        super().__init__(owner, __model, __color, __engine_power)
    # Проверять на то, что не превышено предельно допустимое кол-во пассажиров
    # if quantity > __PASSENGERS_LIMIT:
    #     print(f'Превышено допустимое количество пассажиров!')



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', '500') # для проверки
# ошибочного ввода. Здесь - __engine_power вводится как строка

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()