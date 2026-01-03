from abc import ABC, abstractmethod

full_dictionary = {}

class Base_classes(ABC):

    @abstractmethod
    def add_new_work(self):
        pass

    @abstractmethod
    def output_info(self):
        pass

    @abstractmethod
    def delete_work(self):
        pass


class English_learning(Base_classes):

     def __init__(self):
         pass
    # короче я хз какой функционал писать в функуцию добавления инфы для составления задания подумай
     def add_new_work(self):
         pass
    # эта хуйня для вывода в терминал текущего задания по видеоролику
     def output_info(self):
         pass
     # это соответсвенно удаление задание для ролика
     def delete_work(self):

         pass
# класс для работы с словарем где ключ это номер видеоролика значение объект класса English_learning так же будут методы добавления удаления и просмотра
# не могу сразу весь функционал прописать так как много не знаю
class Dictionary(English_learning):
    def __init__(self):
        super().__init__()
        self.name_dict = full_dictionary
        self.last_number = 0

    def add_new_object(self):
        obj = English_learning
        for x in self.name_dict.keys():
            last_number = x
        if self.last_number == 0:
            self.name_dict[1] = obj.add_new_work()
        else:
            self.name_dict[x] = obj.add_new_work()

    def delete_obj(self):
        pass






