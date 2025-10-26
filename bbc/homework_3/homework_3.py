from random import randint, shuffle, choice
from itertools import *

class Food:
    def __init__(self, food, health):
        self.food = food
        self.health = health
    def eat(self):
        print(f'Твоё здоровье поднялось с {self.health} до {self.health + 1}')
        return self.health + 1

class Chest:
    def __init__(self):
        self.quantity = randint(1, 3)
        
    def findings(self):
        items = ['меч', 'щит', 'еда', 'тотем бессмертия', 'снаряжение']
        new_inventory = []
        for i in range(self.quantity):
            item = choice(items)
            del items[items.index(item)]
            new_inventory.append(item)
        return new_inventory
            
        

class Monster:
    def __init__(self, health, sword, shield):
        self.health = health
        self.sword = sword
        self.shield = shield
    def attack(self):
        print('\nБерегись! Монстр тебя атакует!')
        if (self.sword):
            print('Ты убил монстра! Теперь ты real human being and a real hero! Но тепепь у тебя нет меча(\n')
        elif (self.shield):
            print('У тебя есть щит! Ты здорово отбил атаку монстра! Но больше у тебя нет щита(\n')
        else:
            print(f'Тебе здорово прилетело и твоё здоровье упало с {self.health} до {self.health - 1}\n')
            self.health -= 1
            if self.health != 0:
                print('Монстр никуда не ушёл, но ты нашёл в себе силы сбежать\n')
            else:
                print('Кажется тебя добили, но ты не сдавайся! Я думаю найдётся выход\n')
            
        return self.health





items = ['меч', 'щит', 'еда', 'тотем бессмертия', 'снаряжение']

print('Введите уровень сложности: 1 - самый лёгкий (размеры лабиринта 3x3, ловушек - 0, сундуков - 2, пустых комнат - 4, монстров - 1)\n')
print('2 - средний (размеры лабиринта 5x5, ловушек - 5, сундуков - 4, монстров - 2, пустых комнат - 11, порталов - 1)\n')
print('3 - самый высокий (размеры лабиринта 6x6, ловушек - 7, сундуков - 3, монстров - 5, порталов - 1, пустых комнат - 7)\n')
difficulty_level = int(input('Введите уровень сложности: '))

level = [[3, 2, 1, 1, 0, 0, 1], [10, 4, 2, 1, 5, 1, 1], [6, 3, 5, 1, 7, 1, 1]] #количество комнат 
rooms = ['пусто', 'сундук', 'монстр', 'ключ', 'ловушка', 'портал', 'комната с дверью']

if difficulty_level == 1:
    n = 3
elif difficulty_level == 2:
    n = 5                       #размеры лабиринта
else:
    n = 6

level_chars = level[difficulty_level - 1]
level = list()
for i in range(len(level_chars)):
    level.extend([rooms[i]] * level_chars[i])
shuffle(level)
level = ['пусто'] + level
level = [[level[i * n + j] for j in range(n)] for i in range(n)]
#rooms = [['пусто'].extend([])]
# deep copy (редактирование списков либо мод списков)
inventory = []
curr_x, curr_y = 0, 0
health = 3
for i in range(n * n):
    room_now = level[i // n][i % n]
    if room_now == 'монстр':
        traveler = Monster(health, 'меч' in inventory, 'щит' in inventory)
        health = traveler.attack()
        
        if 'меч' in inventory:
            del inventory[inventory.index('меч')]
            level[i // n][i % n] = 'пусто'
        elif 'щит' in inventory:
            del inventory[inventory.index('щит')]
            level[i // n][i % n] = 'пусто'
        else:
            if (health != 3):
                if (inventory.count('еда') > 0):
                    answer = input('Желаешь ли ты поесть, чтобы поднять здоровье на одну единицу? ')
                    if answer.lower() == 'да':
                        traveler = Food(inventory.count('еда'), health)
                        health = traveler.eat()
                        del inventory[inventory.index('еда')]
                if health == 0:
                    if ('тотем бессмертия' in inventory):
                        answer = input('Хотите ли вы использовать тотем бессмертия? ')
                        if answer.lower() == 'да':
                            print('Поздравляю! Вы использовали тотем бесммертия, поэтому ваше здоровье вновь 3 единицы!)\n')
                            del inventory[inventory.index('тотем бессертия')]
                            health = 3
                        else:
                            print('*WASTED*\n')
                            break
                    else:
                        print('WASTED\n')
                        break
    if room_now == 'сундук':
        traveler = Chest()
        chest = traveler.findings()
        if len:
            print(f'В сундуке было только это: {chest[0]}\n')
            answer = input(f'Хотите взять {chest[0]}? ')
            if answer.lower() == 'да':
                inventory.append(chest[0])
        else:
            print('В сундуке вы нашли эти вещи:', ', '.join(chest))
            
            answer = input('Хотите взять всё или только некоторые предметы? (пишите либо все/всё, либо что угодно)')

            if (answer.lower() == 'все' or answer.lower() == 'всё'):
                inventory.extend(chest)
            else:
                for el in chest:
                    answer = input(f'Хотите взять {el}? ')
                    print('\n', end='')
                    if answer == 'Да':
                        inventory.append(el)
