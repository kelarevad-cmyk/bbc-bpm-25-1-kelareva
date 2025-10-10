class String:
    def __init__(self, text, method, text2=''):
        self.text = text
        self.method = method
        self.text2 = text2

    def lvl1(self):
        if self.method == 1:
            print(f'Метод upper: {self.text.upper()}')
        elif self.method == 2:
            print(f'Метод lower: {self.text.lower()}')
        elif self.method == 3:
            print(f'Метод capitalize: {self.text.capitalize()}')

    def lvl2(self):
        if self.method == 1:
            print(f'Метод find: {self.text.find('круто')}:{self.text.find('круто') + 5}')
        if self.method == 2:
            print(f'Метод index: {self.text.index('круто')}:{self.text.index('круто') + 5}')
        if self.method == 3:
            print(f'Количество букв "о" в строке: {self.text.lower().count('о')}')
        if self.method == 4:
            print(f'Метод replace: "{self.text.replace('круто', 'что-то')}"')

    def lvl3(self):
        print(f'Метод split и join: "{' '.join(self.text.split(','))}"')

    def lvl4(self):
        if self.method == 1:
            for i in range(6):
                print(f'Метод isdigit() для первой строки: {self.text[i]} - {self.text[i].isdigit()}, для второй строки: {self.text2[i]} - {self.text2[i].isdigit()}\n')
        
        if self.method == 2:
            for i in range(6):
                print(f'Метод isalpha()) для первой строки: {self.text[i]} - {self.text[i].isalpha()}, для второй строки: {self.text2[i]} - {self.text2[i].isalpha()}\n')
        
        if self.method == 3:
            print(f'Метод strip() для первой строки: {self.text.strip()}, для второй строки: {self.text2.strip()}\n')
        
    def lvl5(self):
       form_str = ' '.join(self.text.strip().capitalize().split(';'))
       print(f'Приведение строки "{self.text}" к формату: "{form_str}"')



text_for_1 = '''\nДля 1-го уровня сложности есть методы: 1 - upper(), 2 - lower(), 3 - capitalize()'''
text_for_2 = '''\nДля 2-го уровня сложности есть методы: 1 - find(), 2 - index(), 3 - count(), 5 - replace()'''
text_for_3 = '''\nДля 3-го уровня сложности есть метод: split() и join() (выполняются одновременно)'''
text_for_4 = '''\nДля 4-го уровня сложности есть методы: 1 - isdigit(), 2 - isalpha(), 3 - strip()'''
text_for_5 = '''\nДля 5-го уровня сложности есть метод: приведение строки к общепринятому формату'''
text_for_user = [text_for_1, text_for_2, text_for_3, text_for_4, text_for_5]



level = int(input('\nВведите сложность: '))
method = int(input(text_for_user[level - 1] + '\nВведите номер метода в соответствующем уровне: '))
text = input('\nВведите текст: ')

test = String(text, method)

if level == 1:
    test.lvl1()
elif level == 2:
    test.lvl2()
elif level == 3:
    test.lvl3()
elif level == 4:
    text2 = input('\nВведите вторую строку для теста: ')
    test.text2 = text2
    test.lvl4()
elif level == 5:
    test.lvl5()
