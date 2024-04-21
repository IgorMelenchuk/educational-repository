class BankAccount:

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance


    def get_balance(self):
        print('Использована функция getter')
        return self.__balance


    def set_balance(self, value):
        print('Использована функция setter')
        self.__balance = value

    def delete_balance(self):
        print('Использована функция delete')
        del self.__balance


    balance = property(fget=get_balance,fset=set_balance,fdel=delete_balance)