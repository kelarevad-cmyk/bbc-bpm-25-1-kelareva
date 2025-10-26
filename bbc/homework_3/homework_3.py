from random import randint, shuffle
from itertools import *

class Food:
    def __init__(self, food, health):
        self.food = food
        self.health = health
    def eat(self):
        print(f'Твоё здоровье поднялось с {self.health} до {self.health + 1}')
        self.health += 1
        return self.health
    

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
            print('Монстр никуда не ушёл, но ты нашёл в себе силы сбежать\n')
            self.health -= 1
        return self.health





items = ['меч', 'щит', 'еда', 'тотем бессмертия', 'снаряжение']

print('Введите уровень сложности: 1 - самый лёгкий (размеры лабиринта 3x3, ловушка - 0, сундук - 2, пусто - 4, монстр - 1)\n')
print('2 - средний (размеры лабиринта 5x5, ловушка - 5, сундук - 4, монстр - 2, пусто - 11, портал - 1)\n')
print('3 - самый высокий (размеры лабиринта 5x5, ловушка - 7, сундук - 3, монстр - 5, портал - 1, пусто - 7)\n')
difficulty_level = int(input('Введите уровень сложности: '))

level = [[3, 2, 1, 1, 0, 0, 1], [10, 4, 2, 1, 5, 1, 1], [6, 3, 5, 1, 7, 1, 1]] #количество комнат 
rooms = ['пусто', 'сундук', 'монстр', 'ключ', 'ловушка', 'портал', 'комната с дверью']

if difficulty_level == 1:
    n = 3
else:
    n = 5 #размеры лабиринта

level_chars = level[difficulty_level - 1]
level = list()
for i in range(len(level_chars)):
    level.extend([rooms[i]] * level_chars[i])
shuffle(level)
level = ['пусто'] + level
level = [[level[i * n + j] for j in range(n)] for i in range(n)]
#rooms = [['пусто'].extend([])]
# deep copy (редактирование списков либо мод списков)
inventory = ['тотем бессмертия', 'еда']
curr_x, curr_y = 0, 0
health = 1
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
                            print('Поздравляю! Вы использовали тотем бесммертия, поэтому ваш ездоровье вновь 3 единицы!)\n')
                            health = 3
                        else:
                            print('WASTED\n')
