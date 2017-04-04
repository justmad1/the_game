class Thing(object):
    __id = 4

    def get_class_id(self):
        return self.__id

    def __init__(self, name="1", cost=1, weight=1):
        self.__name = name
        self.__cost = cost
        self.__weight = weight

    def info(self):
        print(self.__name, "\nCost: ", self.__cost, "\nWeight: ", self.__weight)

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

    def __init__(self, name="heal", type=1, value=1):
        """1 - Add health; 2 - Add mana; 3 - Reduce health; 4 - Reduce mana"""
        Thing.__init__(self, name, value**2, 1)
        self.__type = type
        self.__value = value
        self.__is_used = False

    def info(self):
            print(self.get_name(), "\nCost: ", self.get_cost(), "\nWeight: ", self.get_weight())
            if self.__type is 1:
                print("Add health: ", self.__value)
            if self.__type is 2:
                print("Add mana: ", self.__value)
            if self.__type is 3:
                print("Reduce health: ", self.__value)
            if self.__type is 4:
                print("Reduce mana: ", self.__value)

    def get_is_used(self):
        return self.__is_used

    def get_value(self):
        return self.__value

    def get_type(self):
        return self.__type

    def reduce_weight(self, r):
        print("Cannot reduce weight of a potion!")


class Weapon(Thing):                                        # !!   Do not use  !!
    """Class not for use, only for inheritance"""           # !!!!!!!!!!!!!!!!!!!
    def __init__(self, name, weight, damage):
        self.__damage = damage
        Thing.__init__(self, name, self.__damage, weight)

    def get_damage(self):
        return self.__damage

    def increase_damage(self, i):
        self.__damage += i

    def reduce_damage(self, r):
        if r > self.__damage:
            self.__damage = 0
        else:
            self.__damage -= r


class Сutting(Weapon):
    __id = 6
    __max_durability = 10

    def get_class_id(self):
        return self.__id

    def __init__(self, name="sword", weight=5, damage=10, type=1, durability=10):
        """1 - Sword; 2 - dagger; 3 - axe; 4 - hammer"""
        self.__type = type
        self.__durability = durability
        self.__is_magic = False
        Weapon.__init__(self, name, weight, damage)

    def info(self):
        print(self.get_name(), "\nDamage:", self.get_damage(), "\nWeight:", self.get_weight(),
              "\nDurability:", self.__durability)

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

    def __init__(self, name="bow", weight=3, damage=5, type=1):
        """1 - Bow; 2 - Crossbow;"""
        self.__type = type
        self.__is_magic = False
        Weapon.__init__(self, name, weight, damage)

    def info(self):
        print(self.get_name(), "\nDamage:", self.get_damage(), "\nWeight:", self.get_weight())

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
        Weapon.__init__(self, "arrow", self.__weight, damage)

    def info(self):
        print(self.get_name(), "\nDamage:", self.get_damage())


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
            self.__name = "Fireball"
            self.__damage = value
        elif type is 2:
            self.__name = "Frost arrow"
            self.__can_freeze = True
            self.__damage = 1
        elif type is 3:
            self.__name = "Heal"
            self.__heal = value
        elif type is 4:
            self.__name = "Summon a creature"
            self.__summon = True
            self.__summon_lvl = value
        self.__weight = 0
        Thing.__init__(self, self.__name, value**2, self.__weight)

    def info(self):
        print(self.get_name())
        if self.__type is 1:
            print("Damage:", self.__damage)
        elif self.__type is 2:
            print("Damage:", self.__damage, "\nFreeze an enemy")
            self.__damage = 1
        elif self.__type is 3:
            print("Heal:", self.__heal)
        elif self.__type is 4:
            print("Summons a random level creature")
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
        print("Cannot reduce weight of magic!")


class Armor(Thing):
    __id = 10

    def get_class_id(self):
        return self.__id

    def __init__(self, name="Simple Armor", type=1, value=3, weight=6):
        """1 - Armor; 2 - Helmet; 3 - Shield"""
        self.__name = name
        self.__type = type
        self.__value = value
        self.__is_magic = False
        Thing.__init__(self, self.__name, value ** 2, weight)

    def info(self):
        print(self.get_name(), "\nStrength:", self.__value, "\nWeight:", self.get_weight(),
              "\nCost:", self.get_cost())

    def get_type(self):
        return self.__type

    def get_value(self):
        return self.__value

    def increase_value(self, i):
        self.__value += i
