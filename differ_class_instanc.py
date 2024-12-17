"""
Цель: понять разницу между атрибутами объекта и класса, дополнив уже существующий
 класс. Применить метод __new__.
Задача "История строительства":
Для решения этой задачи будем пользоваться решением к предыдущей
 задаче "Перегрузка операторов".
В классе House создайте атрибут houses_history = [],
 который будет хранить названия созданных объектов.
Правильней вписывать здание в историю сразу при создании объекта,
 тем более можно удобно обращаться к атрибутам класса используя ссылку
  на сам класс - cls.
Дополните метод __new__ так, чтобы:
 Название объекта добавлялось в список cls.houses_history.
 Название строения можно взять из args по индексу.

Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"
"""

class House():
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history += [(args[0])]
        return super().__new__(cls)

    def __del__(self):
        print(self.name,  "снесён, но он останется в истории")

    def __init__(self, name, number_of_floors):
        # На уровне класса проверяется принадлежность name к типу str,
        # number_of_floors к типу int
        # если name и number_of_floors не соответствуют своим типам,
        # то класс (экземпляр класса) не создается
        if isinstance(name, str) and isinstance(number_of_floors, int):
            self.name = name
            self.number_of_floors = number_of_floors

        else:
            print("Класс не создан! Для его создания введите правильные "
                  "аргументы")
            exit()
    def go_to(self, new_floor):
        """
        выводит на экран(в консоль) значения от 1 до new_floor(включительно)
        """
        if isinstance(new_floor, int):
            print(f'Выводим номера этажей в доме "{self.name}" с 1 по {new_floor}')
            if new_floor > self.number_of_floors or new_floor < 1:
                print("Такого этажа не существует")
            else:
                for i in range(1, new_floor + 1):
                    print(i)
        else:
            print('Неверно указан номер этажа. Следует ввести цифру!')
    def __len__(self):
        """
        Возвращает кол-во этажей здания self.number_of_floors
        """
        return self.number_of_floors
    def __str__(self):
        """
        Возвращает строку: "Название: <название>, кол-во этажей: <этажи>".
        """
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    def __eq__(self, other):
        """ Возвращает True, если кол-во этажей одинаковое у self и у other """
        return (other and isinstance(other, House) and self.number_of_floors ==
                other.number_of_floors)

    def  __lt__(self, other):
        """
        Сравнивает количество этажей у self и у other. Возвращает True, если
        у self количество этажей меньше (<) чем у other
        """
        return (other and isinstance(other, House)
                and self.number_of_floors < other.number_of_floors)

    def  __le__(self, other):
        """
        Сравнивает количество этажей у self и у other. Возвращает True, если
        у self количество этажей меньше либо равно (<=), чем у other
        """
        return (other and isinstance(other, House)
                and self.number_of_floors <= other.number_of_floors)
        # if isinstance(other, House):
        #     return self.number_of_floors <= other.number_of_floors
    def  __gt__(self, other):
        """
        Сравнивает количество этажей у self и у other. Возвращает True, если
        у self количество этажей больше (>), чем у other
        """
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
    def  __ge__(self, other):
        """
        Сравнивает количество этажей у self и у other. Возвращает True, если
        у self количество этажей больше либо равно (<=), чем у other
        """
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
    def  __ne__(self, other):
        """
        Сравнивает количество этажей у self и у other. Возвращает True, если
        у self и other количество этажей не равны (!=)
        """
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        """
        Увеличивает кол-во этажей на переданное значение value, возвращает
        сам объект self
        """
        if isinstance(value, int):
            self.number_of_floors += value
            rez = self
        else:
            rez = NotImplemented
        return rez
    def __iadd__(self, value):
        """
        Увеличивает кол-во этажей на переданное значение value, возвращает
        сам объект self
        """
        return self.__add__(value)
    def __radd__(self, value):
        """
        Увеличивает кол-во этажей на переданное значение value, возвращает
        сам объект self
        """
        return self.__add__(value)


print('История строительства - houses_history')
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
print()
print('Удаления')
del h2
del h3
print(House.houses_history)