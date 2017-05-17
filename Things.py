import random


class Thing(object):
    __id = 4

    def get_class_id(self):
        return self.__id

    def __init__(self, name="1", cost=1, weight=1):
        self.__name = name
        self.__cost = cost
        self.__weight = weight

    def info(self):
        print(self.__name, "\nСтоимость: ", self.__cost, "\nВес: ", self.__weight)

    def get_name(self):
        return self.__name

    def get_cost(self):
        return self.__cost

    def get_weight(self):
        return self.__weight

    def reduce_weight(self, r):
        if self.__weight - r < 1:
            self.__weight = 1
        else:
            self.__weight -= r


class Potion(Thing):
    __id = 5

    def get_class_id(self):
        return self.__id

    def __init__(self, name="Лечение", type=1, value=1):
        """1 - Add health; 2 - Add mana; 3 - Reduce health; 4 - Reduce mana"""
        Thing.__init__(self, name, value**2, 1)
        self.__type = type
        self.__value = value
        self.__is_used = False

    def info(self):
            print(self.get_name(), "\nСтоимость: ", self.get_cost(), "\nВес: ", self.get_weight())
            if self.__type is 1:
                print("Добавляет здоровья: ", self.__value)
            if self.__type is 2:
                print("Добавляет маны: ", self.__value)
            if self.__type is 3:
                print("Отнимает здоровья: ", self.__value)
            if self.__type is 4:
                print("Отнимает маны: ", self.__value)

    def get_is_used(self):
        return self.__is_used

    def get_value(self):
        return self.__value

    def get_type(self):
        return self.__type

    def reduce_weight(self, r):
        print("Невозможно уменьшить вес зелья!")


class Weapon(Thing):                                        # !!   Do not use  !!
    """Class not for use, only for inheritance"""           # !!!!!!!!!!!!!!!!!!!
    def __init__(self, name, weight, damage, level):
        self.__damage = damage
        self.__level = level
        Thing.__init__(self, name, self.__damage*2, weight)

    def get_damage(self):
        return self.__damage

    def get_level(self):
        return self.__level

    def increase_damage(self, i):
        self.__damage += i

    def reduce_damage(self, r):
        if r > self.__damage:
            self.__damage = 0
        else:
            self.__damage -= r


class Cutting(Weapon):
    __id = 6
    __max_durability = 10

    def get_class_id(self):
        return self.__id

    def __init__(self, name="Простой меч", weight=5, damage=10, type=1, durability=10, level=1):
        """1 - Sword; 2 - dagger; 3 - axe; 4 - hammer"""
        self.__type = type
        self.__durability = durability
        self.__is_magic = False
        Weapon.__init__(self, name, weight, damage, level)

    def info(self):
        print(self.get_name(), "\nУрон:", self.get_damage(), "\nВес:", self.get_weight(),
              "\nПрочность:", self.__durability, "\nУровень оружия:", self.get_level())

    def reduce_durability(self, r=1):
        self.__durability -= r

    def increase_durability(self, i=1):
        if i + self.__durability > self.__max_durability:
            self.__durability = self.__max_durability
        else:
            self.__durability += i

    def get_durability(self):
        return self.__durability

    def get_type(self):
        return self.__type


class Shooting(Weapon):
    __id = 7

    def get_class_id(self):
        return self.__id

    def __init__(self, name="Простой лук", weight=3, damage=5, type=1):
        """1 - Bow; 2 - Crossbow;"""
        self.__type = type
        self.__is_magic = False
        Weapon.__init__(self, name, weight, damage)

    def info(self):
        print(self.get_name(), "\nУрон:", self.get_damage(), "\nВес:", self.get_weight(),
              "\nУровень оружия:", self.get_level())

    def get_type(self):
        return self.__type

    def get_shoot_damage(self, arrow):
        shoot_damage = self.get_damage() + arrow.get_damage()
        return shoot_damage


class Arrow(Weapon):
    __id = 8

    def get_class_id(self):
        return self.__id

    def __init__(self, damage=3):
        self.__weight = 0
        Weapon.__init__(self, "Стрела", self.__weight, damage)

    def info(self):
        print(self.get_name(), "\nУрон:", self.get_damage())


class Magic(Thing):
    __id = 9

    def get_class_id(self):
        return self.__id

    def __init__(self, type=1, value=7):
        """1 - Fireball; 2 - Frost arrow; 3 - Heal; 4 - Summon a creature"""
        self.__damage = 0
        self.__heal = 0
        self.__summon = False
        self.__can_freeze = False
        self.__type = type
        self.__summon_lvl = None
        if type is 1:
            self.__name = "Фаербол"
            self.__damage = value
        elif type is 2:
            self.__name = "Ледяная стрела"
            self.__can_freeze = True
            self.__damage = 1
        elif type is 3:
            self.__name = "Лечение"
            self.__heal = value
        elif type is 4:
            self.__name = "Призыв существа"
            self.__summon = True
            self.__summon_lvl = value
        self.__weight = 0
        Thing.__init__(self, self.__name, value**2, self.__weight)

    def info(self):
        print(self.get_name())
        if self.__type is 1:
            print("Урон:", self.__damage)
        elif self.__type is 2:
            print("Урон:", self.__damage, "\nЗамораживает противника")
            self.__damage = 1
        elif self.__type is 3:
            print("Лечение:", self.__heal)
        elif self.__type is 4:
            print("Призывает случайное уровневое сущесвто")
            self.__summon = True

    def get_type(self):
        return self.__type

    def get_damage(self):
        return self.__damage

    def get_heal(self):
        return self.__heal

    def get_summon(self):
        return self.__summon

    def get_can_freeze(self):
        return self.__can_freeze

    def add_damage(self, add=1):
        if self.__type is 1:
            self.__damage += add

    def add_heal(self, add=1):
        if self.__type is 3:
            self.__heal += add

    def reduce_weight(self, r):
        print("Невозможно снизить вес магии!")


class Armor(Thing):
    __id = 10

    def get_class_id(self):
        return self.__id

    def __init__(self, name="Простая броня", type=1, value=3, weight=6):
        """1 - Armor; 2 - Helmet; 3 - Shield"""
        self.__name = name
        self.__type = type
        self.__value = value
        self.__is_magic = False
        Thing.__init__(self, self.__name, value ** 2, weight)

    def info(self):
        print(self.get_name(), "\nПрочность:", self.__value, "\nВес:", self.get_weight(),
            "\nСтоимость:", self.get_cost())

    def get_type(self):
        return self.__type

    def get_value(self):
        return self.__value

    def increase_value(self, i=1):
        self.__value += i

    def reduce_value(self, i=1):
        self.__value -= i


class Chest(object):
    __id = 12

    def __init__(self, locked=False):
        self.__all_things = []
        self.__is_locked = locked
        self.__key = []

        if self.__is_locked:
            for i in range(10):
                self.__key.append(random.randint(0, 10000))

    def is_locked(self):
        return self.__is_locked

    def show_things(self):
        if not self.__is_locked:
            if len(self.__all_things) is 0:
                print("Сундук пуст")
            else:
                for obj in self.__all_things:
                    try:
                        print(obj.info())
                    except:
                        print(obj)
                    print("-----------")
        else:
            print("Сундук закрыт")

    def take_a_key(self):
        if self.__is_locked:
            return self.__key
        else:
            return None

    def open(self, key):
        if self.__is_locked:
            if key == self.__key:
                self.__is_locked = False

    def _add_thing(self, thing):
        self.__all_things.append(thing)

    def remove_thing_by_name(self, name):
        for obj in self.__all_things:
            try:
                if obj.get_name() is name:
                    self.__all_things.remove(obj)
            except:
                pass

    def remove_thing_by_obj(self, obj):
        try:
            self.__all_things.remove(obj)
        except:
            pass

    def take_a_thing(self, name):
        for obj in self.__all_things:
            try:
                if obj.get_name() is name:
                    r = obj
                    self.__all_things.remove(obj)
                    return r
            except:
                pass


class RandomCutting(Cutting):
    """Random Cutting weapon"""

    __id = 13

    def get_class_id(self):
        return self.__id

    def __init__(self, lvl=1):
        if lvl < 1:
            lvl = 1
        elif lvl > 10:
            lvl = 10

        name = str
        weight = int
        damage = int
        type = int
        durability = int

        #TODO rewrite names and check values
        if lvl is 1:
            damage = 3
            weight = 1
            name = "Кинжал"
            type = 1
            durability = 10

        elif lvl is 2:
            rand_type = random.randint(1, 2)
            if rand_type is 1:
                damage = random.randint(4, 6)
                weight = damage - 2 - random.randint(0, 1)
                name = "Кинжал"
                type = 1
                durability = 10
            else:
                damage = random.randint(7, 8)
                weight = damage - 3 - random.randint(0, 1)
                name = "Меч"
                type = 2
                durability = 8

        elif lvl is 3:
            rand_type = random.randint(1, 2)
            if rand_type is 1:
                damage = random.randint(6, 8)
                weight = damage - 3 - random.randint(0, 2)
                name = "Кинжал"
                type = 1
                durability = 10
            else:
                damage = random.randint(8, 10)
                weight = damage - 1 - random.randint(0, 1)
                name = "Меч"
                type = 2
                durability = 8

        elif lvl is 4:
            rand_type = random.randint(1, 3)
            if rand_type is 1:
                damage = random.randint(8, 10)
                weight = damage - 4 - random.randint(0, 2)
                name = "Кинжал"
                type = 1
                durability = 10
            elif rand_type is 2:
                damage = random.randint(10, 13)
                weight = damage - 2 - random.randint(0, 2)
                name = "Меч"
                type = 2
                durability = 8
            else:
                damage = random.randint(12, 14)
                weight = damage - 1 - random.randint(0, 2)
                name = "Топор"
                type = 3
                durability = 6

        elif lvl is 5:
            rand_type = random.randint(1, 2)
            if rand_type is 1:
                damage = random.randint(14, 17)
                weight = damage - 2 - random.randint(0, 1)
                name = "Меч"
                type = 2
                durability = 8
            else:
                damage = random.randint(15, 19)
                weight = damage - 1 - random.randint(0, 2)
                name = "Топор"
                type = 3
                durability = 6

        elif lvl is 6:
            rand_type = random.randint(1, 2)
            if rand_type is 1:
                damage = random.randint(18, 22)
                weight = damage - 2 - random.randint(0, 1)
                name = "Меч"
                type = 2
                durability = 8
            else:
                damage = random.randint(20, 23)
                weight = damage - random.randint(0, 1)
                name = "Топор"
                type = 3
                durability = 6

        elif lvl is 7:
            rand_type = random.randint(1, 2)
            if rand_type is 1:
                damage = 25
                weight = damage - 3 - random.randint(0, 2)
                name = "Меч"
                type = 2
                durability = 8
            else:
                damage = random.randint(25, 30)
                weight = damage - 3 + random.randint(0, 6)
                name = "Топор"
                type = 3
                durability = 6

        elif lvl is 8:
            rand_type = random.randint(1, 2)
            if rand_type is 1:
                damage = random.randint(30, 34)
                weight = damage - 5 + random.randint(0, 9)
                name = "Молот"
                type = 4
                durability = 4
            else:
                damage = random.randint(31, 35)
                weight = damage - 4 + random.randint(0, 8)
                name = "Топор"
                type = 6

        elif lvl is 9:
            rand_type = random.randint(1, 2)
            if rand_type is 1:
                damage = random.randint(34, 37)
                weight = damage - 3 + random.randint(0, 10)
                name = "Молот"
                type = 4
                durability = 4
            else:
                damage = random.randint(31, 35)
                weight = damage - 4 + random.randint(0, 8)
                name = "Топор"
                type = 6

        elif lvl is 10:
            rand_type = random.randint(1, 4)
            if rand_type is 1:
                damage = random.randint(30, 32)
                weight = damage - 12 + random.randint(0, 12)
                name = "Кинжал"
                type = 10
                durability = 10
            elif rand_type is 2:
                damage = random.randint(33, 36)
                weight = damage - 5 + random.randint(0, 7)
                name = "Меч"
                type = 8
                durability = 4
            elif rand_type is 3:
                damage = random.randint(36, 39)
                weight = damage - 4 + random.randint(0, 9)
                name = "Топор"
                type = 6
                durability = 4
            elif rand_type is 4:
                damage = random.randint(38, 42)
                weight = damage - 3 + random.randint(0, 12)
                name = "Молот"
                type = 4
                durability = 4

        Cutting.__init__(self, name, weight, damage, type, durability, lvl)
