'''
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод
выводит сообщение «Запуск отрисовки»; создать три дочерних класса Pen
(ручка), Pencil (карандаш), Handle (маркер); в каждом классе реализовать
переопределение метода draw. Для каждого класса метод должен выводить
уникальное сообщение; создать экземпляры классов и проверить, что
выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Отрисовка ручкой.")


class Pencil(Stationery):
    def draw(self):
        print("Отрисовка карандашом.")


class Handle(Stationery):
    def draw(self):
        print("Отрисовка маркером.")


pen = Pen("черная ручка")
pencil = Pencil("простой карандашик")
marker = Handle("синий маркем")

pen.draw()
pencil.draw()
marker.draw()
