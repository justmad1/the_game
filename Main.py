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
"""

import Creatures
import Things
import pygame
import time
import os
import sys
import random
import threading
EXIT = False


def play_song():
    global EXIT
    print("i am play")
    pygame.mixer.music.load('sounds/mario.ogg')
    while True:
        pygame.mixer.music.play()
        for i in range(75):
            time.sleep(0.1)
            if EXIT is True:
                pygame.mixer.music.stop()
                return


def get_os():
    from sys import platform as _platform
    o_s = None
    if _platform == "linux" or _platform == "linux2":
        o_s = "linux"
    elif _platform == "darwin":
        o_s = "mac"
    elif _platform == "win32":
        o_s = "windows"

    return o_s


def stop_music():
    os.system("")


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
        print()
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
        choose = int(input(">"))

        if choose is 0:
            if hero.get_inventory():
                i = 1
                print("Выберите вещь для удаления: ")
                for obj in hero.get_inventory():
                    print(i, "-", obj.get_name())
                    i += 1
                choose = int(input(">"))
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
            choose = int(input("\n1 - Рандомное существо\n2 - Существо с заданными параметрами\n>"))
            if choose is 1:
                rand = random.randint(1, 10)
                rand_creature = Creatures.RandomСreature(rand)
                room_creatures.append(rand_creature)
            elif choose is 2:
                name = input("Введите имя: ")
                health = int(input("Введите здоровье: "))
                mana = int(input("Введите ману: "))
                stamina = int(input("Введите выносливость: "))
                attack = int(input("Введите атаку: "))
                defense = int(input("Введите защиту: "))
                creature = Creatures.LiveCreature(name, health, mana, stamina, attack, defense)
                room_creatures.append(creature)
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
                num = int(input(">"))
                num -= 1

                if num < 0 or num > len(room_creatures):
                    print("Неверный ввод!")

                else:
                    creature = room_creatures.pop(num)
                    creature.health_reduce(hero.get_current_attack())
                    room_creatures.append(creature)
                    print(creature.get_current_health())
                    print("Вы атаковали", creature.get_name(), creature.get_current_health(), "/",
                          creature.get_max_health())

        elif choose is 4:
            print("1 - Создать оружие")
            print("2 - Создать броню")
            print("3 - Создать магию")
            print("4 - создать зелье")

            choose = int(input(">"))
            if choose is 1:
                print("1 - Меч")
                print("2 - Клинок")
                print("3 - Топор")
                print("4 - Молот")
                print("5 - Лук")
                print("6 - Арбалет")
                choose = int(input(">"))
                lvl = int(input("Введите уровень оружия (1-10): "))
                if lvl < 1:
                    lvl = 1
                elif lvl > 10:
                    lvl = 10

                obj = Things
                if choose is 1:
                    obj = Things.Сutting("sword", weight=2 * lvl + 2, damage=4 * lvl + 2, type=1, durability=10)
                elif choose is 2:
                    obj = Things.Сutting("dagger", weight=1 * lvl + 1, damage=2 * lvl + 2, type=2, durability=10)
                elif choose is 3:
                    obj = Things.Сutting("axe", weight=3 * lvl + 2, damage=5 * lvl + 2, type=2, durability=10)
                elif choose is 4:
                    obj = Things.Сutting("hammer", weight=4 * lvl, damage=6 * lvl, type=2, durability=10)
                elif choose is 5:
                    obj = Things.Shooting("bow", weight=2 * lvl, damage=2 * lvl + 1, type=1)
                elif choose is 6:
                    obj = Things.Shooting("crossbow", weight=3 * lvl, damage=2 * lvl + 4, type=2)
                hero.add_to_inventory(obj)

            elif choose is 2:
                print("1 - Броня")
                print("2 - Шлем")
                print("3 - Щит")
                choose = int(input(">"))
                lvl = int(input("Введите уровень брони (1-10): "))
                if lvl < 1:
                    lvl = 1
                elif lvl > 10:
                    lvl = 10

                obj = Things
                if choose is 1:
                    obj = Things.Armor("armor", 1, lvl * 2 + lvl * 2, lvl * 3)            # Поменять !!!!!!!!!!!!!
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
                choose = int(input(">"))
                lvl = int(input("Введите уровень заклинания (1-10): "))
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
                choose = int(input(">"))
                lvl = int(input("Введите уровень зелья (1-10): "))
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
            choose = int(input(">"))
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
                choose = int(input(">"))
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
                        print("Зелье", item.get_name(), "использовано на", room_creatures[choose-1].get_name())
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

        for obj in room_creatures:
            if obj.get_current_health() is 0:
                print("Вы убили", obj.get_name())
                room_creatures.remove(obj)


def main():
    pygame.init()
    os.system("clear")
    threading.Thread(target=play_song).start()
    hero = Creatures.MainHero.create()
    say_hello()
    hero = test_room(hero)


main()
