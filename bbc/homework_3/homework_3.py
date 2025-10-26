from random import randint, shuffle
from itertools import *

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
print(level)
level = ['пусто'] + level
level = [[level[i * n + j] for j in range(n)] for i in range(n)]
print(level)
#rooms = [['пусто'].extend([])]
# deep copy (редактирование списков либо мод списков)
curr_x, curr_y = 0, 0
for i in range(n * n):
    print(f'Вы сейчас в комнате, где {level[i // 5][i % 5]}')
