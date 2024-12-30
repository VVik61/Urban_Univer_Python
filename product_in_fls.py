"""
                    Задача "Учёт товаров":
                    Необходимо реализовать 2 класса Product и Shop,
                    Объекты класса Product будут создаваться следующим образом -
                     Product('Potato', 50.0, 'Vagetables') и обладать следующими свойствами:
                    Атрибут name - название продукта (строка).
                    Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
                    Атрибут category - категория товара (строка).
                    Метод __str__, который возвращает строку в
                     формате '<название>, <вес>, <категория>'.
                     Все данные в строке разделены запятой с пробелами.

                    Объекты класса Shop будут создаваться следующим
                     образом - Shop() и обладать следующими свойствами:
                    Инкапсулированный атрибут __file_name = 'products.txt'.
                    Метод get_products(self), который считывает всю информацию
                     из файла __file_name, закрывает его и возвращает единую строку со всеми
                     товарами из файла __file_name.

                    Метод add(self, *products), который принимает неограниченное
                     количество объектов класса Product.
                     Добавляет в файл __file_name каждый продукт из products,
                      если его ещё нет в файле (по названию).
                      Если такой продукт уже есть, то не добавляет и выводит
                      строку 'Продукт <название> уже есть в магазине' .
                    """

class Product:
    def __init__(self, name, weight, category):
        self.name = name         # название продукта (строка)
        self.weight = weight     # вес товара (дробное число) (5.4 и т.п.)
        self.category = category # категория товара (строка)

    def __add__(self, other):
        if self.name == other.name:
            other.weight += self.weight
            # print(other.weight)
            # self = other
            print(f'Продукт {self.name} уже был в магазине, его общий вес '
                  f'теперь равен {other.weight}.')
            # self.weight = other.weight
        return other
    def  __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read()

    def add(self, *products):
        product = products[0]
        with open(self.__file_name, 'w') as file:
            for i in range(1, len(products)):
                product.__add__(products[i])
                # print(product.__str__())
                file.write(products[i].__str__()+'\n')
                # product = products[i]


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
# p4 = Product('Spaghetti', 7.6, 'Groceries')

s1.add(p1, p2, p3)

print(s1.get_products())
