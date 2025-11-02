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
        items = ['меч', 'щит', 'еда', 'тотем бессмертия']
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
            print('Ты убил монстра! Теперь ты real human being and a real hero! Но теперь у тебя нет меча(\n')
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

def moving(x, y, operation, n):
    ops = ['ц', 'ф', 'ы', 'в']
    operations = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    
    new_x = x + operations[ops.index(operation)][0]
    new_y = y + operations[ops.index(operation)][1]
    if (new_x >= 0 and new_y >= 0 and new_x < n and new_y < n):
        return new_x, new_y
    else:
        return x, y

print('\nПравила пермещения: ц (клавиша w) - вверх на одну позицию, ф (клавиша a) - влево, ы (клавиша s) - вниз, в (клавиша d) - право\n')

items = ['меч', 'щит', 'еда', 'тотем бессмертия']

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
# deep copy (редактирование списков либо мод списков)
inventory = []
curr_x, curr_y, door_x, door_y = 0, 0, 0, 0

for i in range(n):
    if 'комната с дверью' in level[i]:
        door_x = i
        door_y = level[i].index('комната с дверью')
health = 3
while True:
    room_now = level[curr_x][curr_y]
    print(f'Комната: {room_now.capitalize()}')
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
    elif room_now == 'сундук':
        traveler = Chest()
        chest = traveler.findings()
        if len(chest) == 1:
            print(f'Оххх чорт чорт, в сундуке было только это: {chest[0]}\n')
        else:
            print('В сундуке вы нашли эти вещи:', ', '.join(chest))
            
        for el in chest:
            answer = input(f'Хотите взять {el}? ')
            
            if answer.lower() == 'да':
                if (el in ['щит', 'меч'] and el in inventory):
                    print(f'Обойдёшься! У тебя нет места на ещё один {el}))\n')
                elif (el == 'еда' and health < 3):
                    answer = input('Желаешь ли ты поесть, чтобы поднять здоровье на одну единицу? ')
                    if answer.lower() == 'да':
                        traveler = Food(1, health)
                        health = traveler.eat()
                else:
                    inventory.append(el)
        print('\n', end='')
        chest = []
    elif room_now == 'ключ':
        print('Поздравляю! Вы нашли ключ, он поможет вам сбежать из лабиринта! Теперь найдите дверь.\n')
        inventory.append('ключ')
    elif room_now == 'комната с дверью':
        final = 1
        print('Вы наткнулись на комнаты с дверью! Это прямой выход из этого лабиринта!\n')
        if ('ключ' in inventory):
            print('У вас есть ключ, окрывайте дверь\n')
            if 'чей-то талисман' in inventory:
                print('Вы взглянули на оборотную сторону талисмана, кажется там что-то написано...')
                answer = input('Посмотрите? ')
                if answer.lower() == 'да':
                    print('Тут написано "Обернись". Что за бред?\n')
                    answer = input('Вы хотите обернуться? ')
                    if answer.lower() == 'да':
                        print('\n...')
                        final = 0
            if final:
                print('Поздравляю! Вы прошли игру.')
                print('MISSION COMPLETED')
                break
        else:
            print('Похоже у вас нет ключа, чтобы открыть эту дверь( Поищите получше в лабиринте')
    elif room_now == 'портал':
        print('Вы в комнате с порталом!\n')
        answer = input('Хотите попасть в команту с дверью? ')
        print('\n')
        if answer.lower() == 'да':
            curr_x, curr_y = door_x, door_y
    elif room_now == 'ловушка':
        choice = randint(1, 2)
        if len(inventory) > 0:
            if choice:
                deleted = inventory.pop(randint(0, len(inventory) - 1))
                print(f'Вы попали в ловушку, из вашего инвентаря украли {deleted}\n')
            else:
                spec = ['еда', 'тотем бессмертия', 'чей-то старый талисман']
                added = spec[randint(0, 2)]
                print(f'У вас в инвентарь что-то случайно закотилось! Похоже это: {added}\n')
                inventory.append(added)
        else:
            spec = ['еда', 'тотем бессмертия', 'чей-то старый талисман']
            added = spec[randint(0, 2)]
            print(f'У вас в инвентарь что-то случайно закотилось! Похоже это: {added}\n')
            inventory.append(added)
    x, y = curr_x, curr_y
    while True:
        answer = input('Куда желаете отправится дальше? ')
        print('\n', end='')
        curr_x, curr_y = moving(curr_x, curr_y, answer, n)
        if curr_x != x or curr_y != y:
            break
        print('Вы вышли за пределы лабиринта! Так нельзя, попробуйте ещё раз\n')
