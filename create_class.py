"""
Задача "Developer - не только разработчик":
Реализуйте класс House, объекты которого будут создаваться следующим образом:
House('ЖК Эльбрус', 30)
Объект этого класса должен обладать следующими атрибутами:
self.name - имя, self.number_of_floors - кол-во этажей
Также должен обладать методом go_to(new_floor), где new_floor - номер
 этажа(int), на который нужно приехать.
Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести
 строку "Такого этажа не существует".
"""

class House():
    def __init__(self, name, number_of_floors):
            self.name = name
            self.number_of_floors = number_of_floors
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


h1 = House("ЖК Горский", 18)
h1.go_to(5)
print('-' * 10)
input("Для продолжения нажмите Энтер")
h2 = House("Домик в деревне", 2)
h2.go_to(10)