from src.item import Item


class Phone(Item):
    """ Новый класс Phone, наследуется от Item """

    def __init__(self, name: str, price: int, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)  # забираем параметры от родительского класса
        self.__number_of_sim = number_of_sim  # кол-во поддерживаемых сим карт

    @property
    def number_of_sim(self) -> int:
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name
