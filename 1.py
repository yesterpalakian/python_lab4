'''
Класс Example. В нём пропишите 3 (метода) функции.
Две переменные задайте статически, две динамически.
Первый метод: создайте переменную и выведите её.
Второй метод: верните сумму 2-ух глобальных переменных.
Третий метод: верните результат возведения первой динамической
переменной во вторую динамическую переменную.
Создайте объект класса. Напечатайте оба метода. Напечатайте переменную a.
'''


class Example:
    static_variable_1 = 5
    static_variable_2 = 6

    def __init__(self, dynamic_variable_1, dynamic_variable_2):
        self.dynamic_variable_1 = dynamic_variable_1
        self.dynamic_variable_2 = dynamic_variable_2

    def method1(self):
        var = "переменная"
        print(var)

    def method2(self):
        return Example.static_variable_1 + Example.static_variable_2

    def method3(self):
        return self.dynamic_variable_1 ** self.dynamic_variable_2


class_obj = Example(dynamic_variable_1=2, dynamic_variable_2=3)
class_obj.method1()

sum = class_obj.method2()
print("сумма 2-ух глобальных переменных:", sum)

extent = class_obj.method3()
print("возведение первой динамической переменной во вторую динамическую переменную:", extent)
