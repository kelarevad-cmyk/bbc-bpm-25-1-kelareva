import math

class Calc:
    
    def __init__(self, a=0, op='', b=0):
        self.a = a
        self.op = op
        self.b = b

    def calc(self):
        if self.op == '+':
            print(f'{a} + {b} = {self.a + self.b}')
        elif self.op == '-':
            print(f'{a} - {b} = {self.a - self.b}')
        elif self.op == '*':
            print(f'{a} * {b} = {self.a * self.b}')
        elif self.op == '/':
            print(f'{a} / {b} = {self.a / self.b}')
        elif self.op == '//':
            print(f'{a} // {b} = {self.a // self.b}')

    def trigonometry(self):
        if self.op > 4 or self.op < 1:
            print('Не существует такого метода((')
        dict_for_methods = {'Синус': math.sin(a), 'Косинус': math.cos(a), 'Тангенс': math.tan(a), 'Котангенс': 1 / math.tan(a)}
        print(f'{list(dict_for_methods.keys())[op - 1]} значения {a} = {dict_for_methods[list(dict_for_methods.keys())[op - 1]]}')


answer = int(input('Выберите: обычный калькулятор - 1, тригонометрический - 0: '))
if answer:
    a, op, b = int(input('Введите первое число: ')), input('\nВведите операцию, которая будет выполняться (+, -, *, /, //): '), int(input('\nВведите второе число: '))
    test = Calc(a, op, b)
    test.calc()
else:
    a = int(input('\nВведите число, функцию которого вы хотите вычислить: '))
    op = int(input('\nВведите функцию, которую вы хотите вычислить (1 - sin, 2 - cos, 3 - tg, 4 - ctg): '))
    test = Calc(a, op)
    test.trigonometry()
