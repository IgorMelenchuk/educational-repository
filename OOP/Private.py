class Student:
    def __init__(self, name = 'Def', age = 1, branch = 'Std'):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f'Имя: {self.__name},'f'Возраст: {self.__age}',f'Направление: {self.__branch}')