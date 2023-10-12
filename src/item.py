import csv
import pandas


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Добавляем при инициализации экземпляр класса в список
        self.all.append(self)

    def __repr__(self) -> str:
        """Возвращает строку с информацией о классе для разработчика"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Возвращает строку с информацией о классе для пользователя"""
        return f"{self.__name}"

    @property
    def name(self):
        """
        Делает приватным атрибут name
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Задает значение атрибуту name исходя из его длины
        """
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls, filename):
        """
        Открывает файл в формате csv и создает из его данных экземпляры класса
        """
        with open(filename, newline='', encoding='cp1251') as file:
            reader = pandas.read_csv(file)
            items = []
            for i in reader:
                name = str(i['name'])
                price = float(i['price'])
                quantity = int(i['quantity'])
                item = cls(name, price, quantity)
                items.append(item)
            cls.all = items


    @staticmethod
    def string_to_number(str_number: str) -> int:
        """
        Возвращает из строки число в int
        """
        number = str_number.split('.')
        return int(number[0])