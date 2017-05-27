"""CLASS ID`s
1 - LiveCreature
2 - MainHero
3 - RandomСreature
4 - Thing
5 - Potion
6 - Сutting
7 - Shooting
8 - Arrow
9 - Magic
10 - Armor
11 - Location
12 - Chest
13 - RandomCutting
"""

import Locations
import Creatures
import Things
import time
from time import *
import os
import sys
import random
import threading
try:
    import pygame
    import tkinter
    from pygame import *
    from tkinter import *
except ModuleNotFoundError:
    print("pygame module not found!")

EXIT = False

sleep_delay = 1 # Recommended - 2 seconds

room1 = Locations.Location("Тюрьма", 1, True)


def fast_win():
    clear()
    print("   хмм", end="")
    sys.stdout.flush()
    sleep(1)
    print(" что ж, не лучший способ проходить игры, но ты победил")
    sleep(3)
    print("\n    Тайна замка так и осталась неразгаданной!")


def clear():
    if get_os() == 'mac os' or get_os() == 'linux':
        os.system('clear')
    elif get_os() == 'windows':
        os.system('cls')


def inventory():
    clear()
    while True:
        if hero.get_inventory():
                print("0 - Удалить вещь из инвентаря")
        else:
            print("1 - Применить предмет")

            if hero.is_equiped_weapon():
                print("2 - Убрать оружие/магию в инвентарь")
            if hero.is_equiped_armor():
                print("3 - Убрать броню в инвентарь")
            if hero.is_equiped_helmet():
                print("4 - Убрать шлем в инвентарь")
            if hero.is_equiped_shield():
                print("5 - Убрать щит в инвентарь")
            try:
                choose = int(input(">"))
            except ValueError:
                continue
            os.system("clear")
            os.system("clear")
            os.system("clear")



    hero.show_inventory()



def play_music_bg():
    pygame.init()
    os.system("clear")
    song = pygame.mixer.Sound('sounds/epic.ogg')
    clock = pygame.time.Clock()
    song.play()
    while True:
        clock.tick(60)
        if EXIT is True:
            break
    pygame.quit()


def get_os():
    from sys import platform as _platform
    o_s = None
    if _platform == "linux" or _platform == "linux2":
        o_s = "linux"
    elif _platform == "darwin":
        o_s = "mac os"
    elif _platform == "win32":
        o_s = "windows"

    return o_s


def stop_music():
    global EXIT
    EXIT = True


def say_hello():
    if get_os() is "mac":
        os.system("open say.app")


def choose_language():
    print("""
        Please, choose your language
        Пожалуйста, выберите ваш язык
        1 - English
        2 - Русский
        """)
    language = input(">")
    return language


def get_into_the_room():
    print("Вы входите в комнату")

    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)


def test_room(hero):
    os.system("clear")
    print("\n  THIS IS A TEST ROOM\n")
    room_creatures = []

    while True:
        print("")
        if hero.get_inventory():
            print("0 - Удалить вещь из инвентаря")
        print("1 - Все существа в комнате")
        print("2 - Добавить новое существо")
        print("3 - Атаковать существо")
        print("4 - Создать предмет (Добавляется в инвентарь)")
        print("5 - Применить предмет")
        print("6 - Просмотреть инвентарь")
        print("7 - Информация о герое")
        if hero.is_equiped_weapon():
            print("8 - Убрать оружие/магию в инвентарь")
        if hero.is_equiped_armor():
            print("9 - Убрать броню в инвентарь")
        if hero.is_equiped_helmet():
            print("10 - Убрать шлем в инвентарь")
        if hero.is_equiped_shield():
            print("11 - Убрать щит в инвентарь")
        print("111 - Выход")
        try:
            choose = int(input(">"))
        except ValueError:
            print("Неверный ввод!")
            continue
        os.system("clear")
        os.system("clear")
        os.system("clear")

        if choose is 0:
            if hero.get_inventory():
                i = 1
                print("Выберите вещь для удаления: ")
                for obj in hero.get_inventory():
                    print(i, "-", obj.get_name())
                    i += 1
                try:
                    choose = int(input(">"))
                except ValueError:
                    print("Неверный ввод!")
                    continue
                choose -= 1
                rm_obj = hero.get_inventory()[choose]
                hero.remove_from_inventory_by_obj(rm_obj)
                print("\n", rm_obj.get_name(), "удален!\n")
            else:
                print()
                hero.show_inventory()
                print()

        if choose is 1:
            if len(room_creatures) is not 0:
                print("Существа в комнате:\n")
                for obj in room_creatures:
                    obj.info()
                    print("-------------\n")
            else:
                print("\nСейчас в комнате только вы\n")

        elif choose is 2:
            try:
                choose = int(input("\n1 - Рандомное существо\n2 - Существо с заданными параметрами\n>"))
            except ValueError:
                print("Неверный ввод!")
                continue
            if choose is 1:
                rand = random.randint(1, 10)
                rand_creature = Creatures.RandomСreature(rand)
                room_creatures.append(rand_creature)
            elif choose is 2:
                try:
                    name = input("Введите имя: ")
                    health = int(input("Введите здоровье: "))
                    mana = int(input("Введите ману: "))
                    stamina = int(input("Введите выносливость: "))
                    attack = int(input("Введите атаку: "))
                    defense = int(input("Введите защиту: "))
                    creature = Creatures.LiveCreature(name, health, mana, stamina, attack, defense)
                    room_creatures.append(creature)
                except ValueError:
                    print("Неверный ввод!")
                    continue
            print("\n")

        elif choose is 3:
            if len(room_creatures) is 0:
                print("В комнате нет существ!")
            else:
                print("Введите № существа для атаки:\n")
                i = 1
                for obj in room_creatures:
                    print(i, "-", obj.get_name(), end="")
                    i += 1
                try:
                    num = int(input(">"))
                except ValueError:
                    print("Неверный ввод!")
                    continue
                num -= 1

                if num < 0 or num > len(room_creatures):
                    print("Неверный ввод!")

                else:
                    creature = room_creatures[num]
                    creature.health_reduce(hero.attack())
                    room_creatures[num] = creature
                    print("Вы атаковали", creature.get_name(), creature.get_current_health(), "/",
                          creature.get_max_health())

        elif choose is 4:
            print("1 - Создать оружие")
            print("2 - Создать броню")
            print("3 - Создать магию")
            print("4 - создать зелье")

            try:
                choose = int(input(">"))
            except ValueError:
                print("Неверный ввод!")
                continue
            if choose is 1:
                print("1 - Меч")
                print("2 - Клинок")
                print("3 - Топор")
                print("4 - Молот")
                print("5 - Лук")
                print("6 - Арбалет")
                try:
                    choose = int(input(">"))
                    lvl = int(input("Введите уровень оружия (1-10): "))
                except ValueError:
                    print("Неверный ввод!")
                    continue
                if lvl < 1:
                    lvl = 1
                elif lvl > 10:
                    lvl = 10

                obj = Things
                if choose is 1:
                    obj = Things.Cutting("sword", weight=2 * lvl + 2, damage=4 * lvl + 2, type=1, durability=10)
                elif choose is 2:
                    obj = Things.Cutting("dagger", weight=1 * lvl + 1,
                                         damage=2 * lvl + 2, type=2, durability=10)
                elif choose is 3:
                    obj = Things.Cutting("axe", weight=3 * lvl + 2, damage=5 * lvl + 2, type=2, durability=10)
                elif choose is 4:
                    obj = Things.Cutting("hammer", weight=4 * lvl, damage=6 * lvl, type=2, durability=10)
                elif choose is 5:
                    obj = Things.Shooting("bow", weight=2 * lvl, damage=2 * lvl + 1, type=1)
                elif choose is 6:
                    obj = Things.Shooting("crossbow", weight=3 * lvl, damage=2 * lvl + 4, type=2)
                hero.add_to_inventory(obj)

            elif choose is 2:
                print("1 - Броня")
                print("2 - Шлем")
                print("3 - Щит")
                try:
                    choose = int(input(">"))
                    lvl = int(input("Введите уровень брони (1-10): "))
                except ValueError:
                    print("Неверный ввод!")
                if lvl < 1:
                    lvl = 1
                elif lvl > 10:
                    lvl = 10

                obj = Things
                if choose is 1:
                    obj = Things.Armor("armor", 1, lvl * 2 + lvl * 2, lvl * 3)
                elif choose is 2:
                    obj = Things.Armor("helmet", 2, lvl*2, lvl)
                elif choose is 3:
                    obj = Things.Armor("shield", 3, lvl*2 + lvl, lvl*2)
                hero.add_to_inventory(obj)

            elif choose is 3:
                print("1 - фаербол")
                print("2 - ледяная стрела")
                print("3 - лечение")
                print("3 - призыв существа")
                try:
                    choose = int(input(">"))
                    lvl = int(input("Введите уровень заклинания (1-10): "))
                except ValueError:
                    print("Неверный ввод!")
                if lvl < 1:
                    lvl = 1
                elif lvl > 10:
                    lvl = 10

                if choose is 1:
                    obj = Things.Magic(1, 10 + lvl*2)
                elif choose is 2:
                    obj = Things.Magic(2)
                elif choose is 3:
                    obj = Things.Magic(3, 10 + lvl*2)
                elif choose is 4:
                    obj = Things.Magic(4, lvl)
                hero.add_to_inventory(obj)

            elif choose is 4:
                print("1 - здоровье+")
                print("2 - мана+")
                print("3 - здоровье-")
                print("3 - мана-")
                try:
                    choose = int(input(">"))
                    lvl = int(input("Введите уровень зелья (1-10): "))
                except ValueError:
                    print("Неверный ввод!")
                if lvl < 1:
                    lvl = 1
                elif lvl > 10:
                    lvl = 10

                if choose is 1:
                    obj = Things.Potion("heal", 1, lvl)
                elif choose is 2:
                    obj = Things.Potion("mana+", 2, lvl)
                elif choose is 3:
                    obj = Things.Potion("damage", 3, lvl)
                elif choose is 4:
                    obj = Things.Potion("mana-", 4, lvl)
                hero.add_to_inventory(obj)

        elif choose is 5:
            if len(hero.get_inventory()) is 0:
                print()
                hero.show_inventory()
                print()
                continue
            print("Выберите предмет для использования: ")
            inventory = hero.get_inventory()
            i = 1
            for obj in inventory:
                print(i, "-", obj.get_name())
                i += 1
            try:
                choose = int(input(">"))
            except ValueError:
                print("Неверный ввод!")
            if choose < 1:
                choose = 1
            elif choose > len(inventory):
                choose = len(inventory)
                choose -= 1
            choose -= 1
            item = inventory[choose]
            id = item.get_class_id()
            if id is 4:
                print("Этот предмет нельзя использовать!")
            elif id is 5:
                is_used = False
                potion = item
                print("Вы выбрали зелье", item.get_name(), "\nНа кого вы хотитие его применить?")
                i = 1
                print("0 - На себя")
                for creature in room_creatures:
                    print(i, "-", creature.get_name(), end="")
                    i += 1
                try:
                    choose = int(input(">"))
                    lvl = int(input("Введите уровень оружия (1-10): "))
                except ValueError:
                    print("Неверный ввод!")
                print(choose)
                input()
                if choose < 0:
                    print("Choose < 0")
                    choose = 1
                elif choose > len(room_creatures):
                    print("Choose > len")
                    choose = len(room_creatures)
                if choose is 0:
                    hero.use_potion(potion)
                    is_used = True
                else:
                    room_creatures[choose-1].use_potion(potion)
                    is_used = True
                if is_used:
                    if choose is 0:
                        print("Зелье", item.get_name(), "использовано на себя")
                        hero.remove_from_inventory_by_obj(item)
                    else:
                        print("Зелье", item.get_name(), "использовано на",
                              room_creatures[choose-1].get_name())
                        hero.remove_from_inventory_by_obj(item)
            elif id is 6 or id is 7:
                print("Вы выбрали оружие", item.get_name())
                hero.equip_a_weapon(item)
                hero.remove_from_inventory_by_obj(item)

            elif id is 8:
                print("Стрелы используются автоматически!")

            elif id is 9:
                print("Вы выбрали магию", item.get_name())
                hero.equip_a_weapon(item)
                hero.remove_from_inventory_by_obj(item)

            elif id is 10:
                if item.get_type() is 1:
                    print("Вы выбрали броню", item.get_name())
                    hero.put_on_armor(item)
                if item.get_type() is 2:
                    print("Вы выбрали шлем", item.get_name())
                    hero.put_on_helmet(item)
                if item.get_type() is 3:
                    print("Вы выбрали щит", item.get_name())
                    hero.equip_a_shield(item)

        elif choose is 6:
            print()
            hero.show_inventory()
            print()

        elif choose is 7:
            hero.info()

        elif choose is 8:
            if hero.is_equiped_weapon():
                hero.put_a_weapon()

        elif choose is 9:
            if hero.is_equiped_armor():
                hero.take_off_armor()

        elif choose is 10:
            if hero.is_equiped_helmet():
                hero.take_off_helmet()

        elif choose is 11:
            if hero.is_equiped_shield():
                hero.put_a_shield()

        elif choose is 111:
            global EXIT
            EXIT = True
            return hero

        elif choose is 00:
            damage = int(input("Введите урон: "))
            hero.health_reduce(damage)

        for obj in room_creatures:
            if obj.get_current_health() is 0:
                print("Вы убили", obj.get_name())
                room_creatures.remove(obj)


def some_words():
    clear()
    print("Я ничего не могу вспомнить", end="")
    sys.stdout.flush()
    sleep(sleep_delay/2)
    for i in range(3):
        print('.', end='')
        sys.stdout.flush()
        sleep(sleep_delay/2)
    sleep(sleep_delay/2)
    print("\n\nКак же меня зовут?")
    name = input(">")
    sleep(sleep_delay/2)
    clear()
    print("\nТочно, вспомнил", end=" ")
    sys.stdout.flush()
    print("меня зовут", name)
    sleep(sleep_delay)
    print("\nНажмите (Enter) чтобы осмотреться.")
    input()
    sleep(sleep_delay)
    clear()
    print("\nКажется я в какой-то... ", end="")
    sleep(sleep_delay/2)
    print("пещере")
    sleep(sleep_delay)
    print("Что я здесь делаю?")
    sleep(sleep_delay)
    print("Где все мои вещи?")
    sleep(sleep_delay)
    print("Ничего не понимаю...")
    sleep(sleep_delay)
    print("Что же делать?")
    sleep(sleep_delay)

    return name


def room_0():
    choose = int
    if len(hero.get_keys()) is not 1:
        key = room1.take_a_key()
    else:
        key = hero.get_keys()[0]

    while True:
        clear()

        print("""
1 - Осмотреть все вокруг себя
2 - Искать выход
3 - Сидеть и ждать чуда
            """)

        try:
            choose = int(input(">"))
        except:
            pass

        if choose is 1:
            if len(hero.get_keys()) is not 1:
                base_knife = Things.Cutting("старый нож", 1, 2, 2)
                hero.add_to_inventory(base_knife)
                sleep(sleep_delay/2)
                print("Ох, кажется мне улыбнулась удача, я нашел какой-то ножик")
                sleep(sleep_delay)
                print("теперь хоть от крыс отбиваться можно")
                sleep(sleep_delay)
                print("Кажется там лежит какой-то бедолага, похоже ему уже никто не поможет...")
                sleep(sleep_delay)
                print("Кто же его так...")
                sleep(sleep_delay)
            else:
                print("Все что можно я уже осмотрел, больше ничего интересного")
                sleep(sleep_delay)
                break

            try:
                сhoose2 = int(input("1 - Обыскать карманы\n(Любая клавиша) - Пойти дальше\n>"))
            except:
                сhoose2 = 2

            if сhoose2 is 1:
                key = room1.take_a_key()
                hero.add_key(key)
                print("В кармане нашелся какой-то ключ, что ж возьму, может пригодится")
                sleep(sleep_delay)
            else:
                pass

            if key in hero.get_keys():
                print(True)
            else:
                print(False)

            break

        elif choose is 2:
            print("Мне кажется, я вижу лазейку, присыпанную камнями")
            sleep(sleep_delay)
            print("не самый лучший вариант, надо поискать еще\n")
            for i in range(5):
                print('.')
                sleep(sleep_delay/2)
            print("\nТаак, вроде с дальнего угла пробивается лучик света, пойду туда, пожалуй\n")
            sleep(sleep_delay/2)
            break

        elif choose is 3:
            print("Ленивая задница, ты же здесь сдохнешь!")
            sleep(sleep_delay)
            print("Нееет, так не пойдет, надо что-то делать")
            sleep(sleep_delay)
            print("Я хочу домой...")

        else:
            pass

    room_1(key)


def room_1(key):
    next_room = int
    clear()

    print("Таак, эта комната похоже на какую-то темницу")
    sleep(sleep_delay)
    print("Тут есть решетчатое окно, так вот откуда пробивался свет")
    sleep(sleep_delay)

    if key in hero.get_keys():
        print("Тут есть дверь, стоит попробовать открыть дверь ключом, что я нашел")
    else:
        print("Дверь скорее всего запрета, но стоит все же попробовать")
        sleep(sleep_delay)
        input("(Enter) - Попытаться открыть дверь\n")
        print("Нет, она точно закрыта")
    sleep(sleep_delay*1.5)

    while True:
        clear()

        if key in hero.get_keys():
            print("1 - Попытаться открыть дверь ключом")
        else:
            print("1 - Продолжать выламывать дверь (серьезно?)")
        print("2 - Попытаться спилить решетки на окне")
        print("3 - Осмотреться получше")
        print("4 - Вернуться назад в пещеру")

        try:
            choose = int(input(">"))
        except:
            continue

        if choose is 1:
            if key in hero.get_keys():
                print("Черт возьми, он подошел!")
                sleep(sleep_delay/2)
                print("Дверь со скрипом открывается", end="")
                sys.stdout.flush()
                sleep(sleep_delay/2)
                for i in range(3):
                    print('.', end='')
                    sys.stdout.flush()
                    sleep(sleep_delay/2)
                print("\n(Enter) - Выйти из темницы")

                next_room = 1
                break
            else:
                print("Вряд ли это поможет, это толстая тюремная дверь из дерева\
                 со стальными прутьями, ее ногой не выбьешь!")
                sleep(sleep_delay)

        elif choose is 2:
            print("Таак, у меня есть какой-то ножик, мне действительно стоит попробовать")
            sleep(sleep_delay/2)

            try:
                choose2 = int(input("1 - Начать пилить(нельзя отменить)\n2 - Да не, бред какой-то\n>"))
            except:
                continue

            if choose2 is 1:
                print("Что ж, ладно...")
                for i in range(3600):
                    clear()
                    print(i, "из и 3600")
                    sleep(1)

                next_room = 2
                break
            else:
                continue

        elif choose is 3:
            print("Похоже что в этой комнате больше ничего нет, даже осматривать нечего")
            continue

        elif choose is 4:
            next_room = 0
            break

    if choose is 1:
        room_2()
    elif choose is 2:
        fast_win()
    elif choose is 4:
        room_0()

def get_choise():
    while True:
        try:
            choose = int(input(">"))
            break
        except:
            continue

    return choose

def room_2():
    room2 = Locations.Location("Коридор темницы", 1)
    room2.add_creature(hero)
    undead_dog = Creatures.LiveCreature("Скелет собаки", 2, d_attack=1)
    room2.add_creature(undead_dog)

    clear()
    print("Я попал в коридор темницы")
    sleep(sleep_delay/2)
    print("Странно... ", end="")
    sleep(sleep_delay/2)
    print("это место кажется мне знакомым")
    sleep(sleep_delay)
    print("Всюду раздаются душераздирающие крики и стоны")
    sleep(sleep_delay)
    print("Кто эти люди? Рабы, жестокие убийцы или же воры?")
    sleep(sleep_delay)
    print("Ладно, надо идти дальше, не могу здесь находится")
    sleep(sleep_delay)

    while True:
        try:
            choose = int(input("1 - Пойти дальше по коридору\n2 - Подойти и поговорить с одним из заключенных\n>"))
        except:
            clear()
            continue

        sleep(sleep_delay)
        if choose is 1:
            break
        elif choose is 2:
            print("-Приветствю, кто ты друг мой?")
            sleep(sleep_delay)
            print("-(Заключенный)Грядущее не ведает отсрочки.")
            sleep(sleep_delay)
            print("-Как и за что ты сюда попал?")
            sleep(sleep_delay)
            print("-(Заключенный)Господь, за грех попасть сюда!")
            sleep(sleep_delay)
            print("-О чём ты говоришь?")
            sleep(sleep_delay)
            print("-(Заключенный)Пророчество уже вот-вот сбудется!")
            sleep(sleep_delay)
            print("-Какое пророчество? Я тебя не понимаю.")
            sleep(sleep_delay)
            print("Видимо поговорить с ними не получится.")
            sleep(sleep_delay)
            print("Кто-то лишил их разума. Нужно выяснить, что здесь происходит.")
            sleep(sleep_delay * 1.5)
            break
        else:
            continue

    for i in range(4):
        print('.')
        sleep(sleep_delay/2)

    clear()
    print("Я слышу какой-то стук по земле", end="")
    sleep(sleep_delay/2)
    print(", он приближается...\n")

    while True:
        print("""
1 - Достать нож и выбежать из-за угла первым
2 - Спрятаться в тени
3 - Стоять и ждать что будет
            """)

        choose = get_choise()
        if choose > 3 or choose < 1:
            continue
        else:
            break

    if choose is 1:
        hero.equip_a_weapon(hero.get_inventory()[0])

        print("ЧТООО ЗА..")
        sleep(sleep_delay/2)
        print("Передо мной стоит скелет огромной собаки... ", end="")
        sleep(sleep_delay)
        sys.stdout.flush()
        print("с горящими красными глазами")
        sleep(sleep_delay)
        print("(Enter) - Атаковать первым")
        input()
        undead_dog.health_reduce(hero.attack())
        room2.remove_creature_by_obj(undead_dog)
        del(undead_dog)
        os.system("clear")
        print("Оо черт..")
        sleep(sleep_delay)
        print("Скелет развалился и глаза больше не горят")
        sleep(sleep_delay)

    elif choose is 2:
        print("Мгновение...", end="")
        sleep(sleep_delay/2)
        sys.stdout.flush()
        print(" и я уже стою в углу")
        sleep(sleep_delay)
        print("Свет сюда не падает, надо задержать дыхание...")
        sleep(sleep_delay)

        for i in range(3):
            sleep(sleep_delay/2)
            print('.')

        print("ЧТООО ЗА..")
        sleep(sleep_delay/2)
        print("Передо мной стоит скелет огромной собаки... ", end="")
        sleep(sleep_delay)
        sys.stdout.flush()
        print("с горящими красными глазами")
        sleep(sleep_delay)
        clear()
        print("Черт, она бросилась на меня!")
        sleep(sleep_delay/2)
        hero.health_reduce(undead_dog.get_current_attack())
        print('\n', hero.get_name(),'\nЗдоровье: ', hero.get_current_health(), "/", hero.get_max_health())
        sleep(sleep_delay)

        while True:
            clear()
            print("В инвентаре сейчас есть:")
            hero.show_inventory()

            print("\n1 - Экипировать нож и ударить\n2 - Ударить рукой")

            choose2 = get_choise()

            if choose2 is 1:
                hero.equip_a_weapon(hero.get_inventory()[0])
                undead_dog.health_reduce(hero.attack())
            elif choose2 is 2:
                undead_dog.health_reduce(hero.attack())
            else:
                continue 

            clear()

            if undead_dog.get_current_health() is 0:
                room2.remove_creature_by_obj(undead_dog)
                del(undead_dog)
                os.system("clear")
                print("Оо черт..")
                sleep(sleep_delay)
                print("Скелет развалился и глаза больше не горят")
                sleep(sleep_delay)
                break
            else:
                print('\n', undead_dog.get_name(),'\nЗдоровье: ', undead_dog.get_current_health(),"/", undead_dog.get_max_health())
                sleep(sleep_delay)
                print("Пес атаковал снова!")
                sleep(sleep_delay/2)
                hero.health_reduce(undead_dog.get_current_attack())
                print('\n', hero.get_name(),'\nЗдоровье: ', hero.get_current_health(), "/", hero.get_max_health())
                sleep(sleep_delay)


    elif choose is 3:
        print("Это точно не лучшая идея")

        for i in range(3):
            sleep(sleep_delay/2)
            print('.')

        print("ЧТООО ЗА..")
        sleep(sleep_delay/2)
        print("Передо мной стоит скелет огромной собаки... ", end="")
        sleep(sleep_delay)
        sys.stdout.flush()
        print("с горящими красными глазами")
        sleep(sleep_delay)
        clear()
        print("Черт, она бросилась на меня!")
        sleep(sleep_delay/2)
        hero.health_reduce(undead_dog.get_current_attack())
        print('\n', hero.get_name(),'\nЗдоровье: ', hero.get_current_health(), "/", hero.get_max_health())
        sleep(sleep_delay)

        while True:
            clear()

            print("\n(Enter) - Ударить рукой")
            choose2 = input()

            undead_dog.health_reduce(hero.attack())

            clear()

            if undead_dog.get_current_health() is 0:
                room2.remove_creature_by_obj(undead_dog)
                del(undead_dog)
                os.system("clear")
                print("Оо черт..")
                sleep(sleep_delay)
                print("Скелет развалился и глаза больше не горят")
                sleep(sleep_delay)
                break
            else:
                print('\n', undead_dog.get_name(),'\nЗдоровье: ', undead_dog.get_current_health(),"/", undead_dog.get_max_health())
                sleep(sleep_delay)
                print("Пес атаковал снова!")
                sleep(sleep_delay/2)
                hero.health_reduce(undead_dog.get_current_attack())
                print('\n', hero.get_name(),'\nЗдоровье: ', hero.get_current_health(), "/", hero.get_max_health())
                sleep(sleep_delay)

        print("Черт возьми, у меня же был нож")
        sleep(sleep_delay)
        print("Надо было не мешкаться...")
        sleep(sleep_delay)

    room_3()


def room_3():
    room3 = Locations.Location("Лаборатория алхимика", 1, True)
    key = room3.take_a_key()


    clear()
    uplevel()
    sleep(sleep_delay)
    print("")


def start_window():
    say_hello()
    print("You are using", get_os())
    sleep(sleep_delay)
    clear()
    # threading.Thread(target=play_music_bg).start()
    sleep(sleep_delay/2)
    clear()
    print('   THE WAY OUT', end='')
    sys.stdout.flush()
    sleep(sleep_delay/2)
    for i in range(3):
        print('.', end='')
        sys.stdout.flush()
        sleep(sleep_delay/2)
    print(" (beta)")
    print("Нажмите (Enter) для начала.")
    input()


def uplevel():
    hero.uplevel()
    print("\n-- Получен новый уровень!")
    hero.info()
    print()


def main():
    room_0()
    stop_music()


clear()
start_window()
name = some_words()
name = "GG"
hero = Creatures.MainHero.create(name)
main()
