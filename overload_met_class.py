"""
Цель: применить знания о перегрузке арифметических операторов и операторов сравнения.

Задача "Нужно больше этажей":

Необходимо дополнить класс House <задания предыдущих уроков в ф-лах
create_class.py и dunder_met_class.py> следующими специальными методами:
__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
Остальные методы арифметических операторов, где self - x, other - y:

Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
isinstance(other, int) - other указывает на объект типа int.
isinstance(other, House) - other указывает на объект типа House.
"""
class House():
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
        # return self   NotImplemented

h1 = House("ЖК Эльбрус", 10)
h2 = House("ЖК Акация", 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
