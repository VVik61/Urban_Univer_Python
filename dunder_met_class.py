"""
Дополнить класс House <задание предыдущего урока в ф-ле create_class.py>  следующими специальными методами:
__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
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

	
h1 = House("ЖК Эльбрус", 10)
h2 = House("ЖК Акация", 20)
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))
