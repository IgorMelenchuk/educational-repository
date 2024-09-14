class BankAccount:

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance


    @property
    def my_balance(self):
        print('Использована функция getter')
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        print('Использована функция setter')
        self.__balance = value

    #my_balance = my_property_balance.setter(my_balance)
    @my_balance.deleter
    def my_balance(self):
        print('Использована функция delete')
        del self.__balance

    #my_balance = property(my_balance)
    #my_balance = my_balance.setter(set_balance)
    #my_balance = my_balance.deleter(delete_balance)
