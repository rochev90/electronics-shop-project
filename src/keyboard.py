from src.item import Item


class MixinLanguage:
    """ Класс Mixin для метода смены клавиатуры"""

    def __init__(self):
        self.__language = 'EN'


    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language.upper() == 'EN':
            self.__language = 'RU'
            return self

        if self.__language.upper() == 'RU':
            self.__language = 'EN'
            return self


class Keyboard(Item, MixinLanguage):

    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.language})"

    def __str__(self):
        return f"{self.name}"

print(Keyboard.__mro__)
