import random
import sys


class LiveCreature(object):
    """Living creature, can be anyone, has it`s own health, mana and etc."""
    __id = 1

    def get_class_id(self):
        return self.__id

    def __init__(self, name="creature", m_health=10, m_mana=0, m_stamina=5, d_attack=5, defense=0):
        self.__name = name
        self.__max_health = m_health
        self.__health = self.__max_health
        self.__max_mana = m_mana
        self.__mana = self.__max_mana
        self.__max_stamina =  m_stamina
        self.__stamina = self.__max_stamina
        self.__default_attack = d_attack
        self.__attack = self.__default_attack
        self.__defense = defense

    def info(self):
        ret = str(self.__name) + "\nHealth: " + str(self.__health) + "/" + \
              str(self.__max_health) + "\nMana: " + str(self.__mana) + "/" + str(self.__max_mana) + \
              "\nStamina:" + str(self.get_current_stamina()) + "/" + str(self.get_max_stamina()) + \
              "\nAttack: " + str(self.__attack) + "\nDefense: " + str(self.__defense)
        print(ret)

    def die(self):
        self.__max_health = 0
        self.__health = 0
        self.__max_mana = 0
        self.__mana = 0
        self.__max_stamina = 0
        self.__stamina = 0
        self.__default_attack = 0
        self.__attack = 0
        self.__defense = 0

    def get_name(self):
        return self.__name

    def get_current_attack(self):
        return self.__attack

    def get_current_health(self):
        return self.__health

    def get_current_mana(self):
        return self.__mana

    def get_current_stamina(self):
        return self.__stamina

    def get_default_attack(self):
        return self.__default_attack

    def get_max_health(self):
        return self.__max_health

    def get_max_mana(self):
        return self.__max_mana

    def get_max_stamina(self):
        return self.__max_stamina

    def health_add(self, h_add=1):
        if self.__health + h_add > self.__max_health:
            self.__health = self.__max_health
        else:
            self.__health += h_add

    def max_health_add(self, mh_add):
        self.__max_health += mh_add

    def max_stamina_add(self, st=1):
        self.__max_stamina += st

    def stamina_add(self, st=1):
        if st + self.__stamina > self.__max_stamina:
            self.__stamina = self.__max_stamina
        else:
            self.__stamina += st

    def stamina_reduce(self, r=1):
        if r > self.__stamina:
            self.__stamina = 0
        else:
            self.__stamina -= r

    def health_reduce(self, damage=1):
        if self.get_class_id() is 2:
            if damage < self.get_defense():
                return
            else:
                damage -= self.get_defense()
        else:
            if damage < self.__defense:
                return
            else:
                damage -= self.__defense
        if damage >= self.__health:
            if self.get_class_id() is 2:
                self.__del__()
            else:
                self.die()
        else:
            self.__health -= damage

    def mana_add(self, m_add=1):
        if self.__mana + m_add > self.__max_mana:
            self.__mana = self.__max_mana
        else:
            self.__mana += m_add

    def max_mana_add(self, mm_add=1):
        self.__max_mana += mm_add

    def mana_reduce(self, damage=1):
        if damage > self.__mana:
            self.__mana = 0
        else:
            self.__mana -= damage

    def use_potion(self, potion):
        if potion.get_is_used() is True:
            return

        if potion.get_type() is 1:            # Add health
            self.health_add(potion.get_value())
        elif potion.get_type() is 2:          # Add mana
            self.mana_add(potion.get_value())
        elif potion.get_type() is 3:          # Reduce health
            self.__health -= potion.get_value()
        elif potion.get_type() is 4:          # Reduce mana
            self.mana_reduce(potion.get_value())

    def reset_attack(self):
        self.__attack = self.__default_attack


class MainHero(LiveCreature):
    """Creates a player hero. Only one object.  Example: *obj_name* = MainHero.create()"""
    __instance = None
    __count = 0

    __id = 2

    def get_class_id(self):
        return self.__id

    @staticmethod
    def create():
        if MainHero.__instance is None:
            MainHero.__instance = True
            return MainHero()
        else:
            raise Exception

    def __init__(self, name="Dima"):
        LiveCreature.__init__(self, name, 30, 20, 10, 10)
        self.__level = 1
        self.__weapon = None
        self.__equiped_weapon = False
        self.__wear_armor = False
        self.__wear_helmet = False
        self.__wear_shield = False
        self.__armor = None
        self.__helmet = None
        self.__shield = None
        self.__inventory = []
        self.__current_weight = 0
        self.__max_weight = 100


    def __del__(self):
        MainHero.__instance = None
        MainHero.__count = 0
        self.__game_over()

    def __game_over(self):
        self.die()
        print("You are dead! Game is over")
        #sys.exit("gg")
        #TODO go to begin

    def uplevel(self, lv=1):
        self.__level += lv
        self.max_health_add(5)
        self.health_add(5)
        self.max_mana_add(5)
        self.mana_add(5)
        self.max_stamina_add(5)

    def get_level(self):
        return self.__level

    def info(self):
        print("\n   ", self.get_name())
        print("Health:", self.get_current_health(), "/", self.get_max_health())
        print("Mana:", self.get_current_mana(), "/", self.get_max_mana())
        print("Stamina:", self.get_current_stamina(), "/", self.get_max_stamina())

        if not self.__equiped_weapon:
            print("Attack:", self.get_current_attack())
        else:
            print("Weapon attack", self.get_current_attack())
        if self.__wear_armor:
            print("Armor:", self.__armor.get_value())
        if self.__wear_helmet:
            print("Helmet:", self.__helmet.get_value())
        if self.__wear_shield:
            print("Shield:", self.__shield.get_value())

    def attack(self):
        attack = None
        if self.__equiped_weapon:
            if self.__weapon.get_class_id() is 6:
                self.__weapon.reduce_durability()
                attack = self.__weapon.get_damage()
                self.stamina_reduce(1)
            elif self.__weapon.get_class_id() is 7:
                arrow = None
                for obj in self.__inventory:
                    if obj.get_class_id() is 8:
                        arrow = obj
                        break
                if arrow:
                    attack = self.__weapon + arrow.get_damage()
                    self.remove_from_inventory_by_obj(arrow)
                    self.stamina_reduce(1)
                else:
                    attack = self.__weapon.get_damage()
            elif self.__weapon.get_class_id() is 9:
                try:
                    if self.__weapon.get_type() is 1:
                        attack = self.__weapon.get_damage()
                        self.mana_reduce(1)
                except:
                    pass
        else:
            attack = self.get_default_attack()
        return attack

    def add_to_inventory(self, obj):
        if obj.get_weight() <= self.__max_weight - self.__current_weight:
            self.__current_weight += obj.get_weight()
            self.__inventory.append(obj)
            print(obj.get_name(), "added to inventory!")
        else:
            print("No more space in inventory!")

    def show_inventory(self):
        if len(self.__inventory) is 0:
            print("Your INVENTORY is empty!")
        else:
            print("\nINVENTORY")
            print("Weight: ", self.__current_weight, "/", self.__max_weight)
            print("-------------\n")
            for obj in self.__inventory:
                obj.info()
                print("-------------")

    def get_inventory(self):
        return self.__inventory

    def remove_from_inventory_by_obj(self, obj):
        if obj in self.__inventory:
            self.__inventory.remove(obj)
            self.__current_weight -= obj.get_weight()
            return True
        else:
            return False

    def remove_from_inventory_by_name(self, name):
        for i in range(len(self.__inventory)):
            if name is self.__inventory[i].get_name():
                self.__current_weight -= self.__inventory[i].get_weight()
                self.__inventory.remove(self.__inventory[i])
                return True
        return False

    def take_off_armor(self):
        if self.__wear_armor:
            self.__wear_armor = False
            self.add_to_inventory(self.__armor)
            self.__armor = None

    def take_off_helmet(self):
        if self.__wear_helmet:
            self.__wear_helmet = False
            self.add_to_inventory(self.__helmet)
            self.__helmet = None

    def put_on_armor(self, armor):
        if self.__wear_armor:
            print("Take off your armor to wear a new one")
            return
        else:
            try:
                self.remove_from_inventory_by_obj(armor)
            except:
                pass
            self.__wear_armor = True
            self.__armor = armor

    def put_on_helmet(self, helmet):
        if self.__wear_helmet:
            print("Take off your helmet to wear a new one")
            return
        else:
            try:
                self.remove_from_inventory_by_obj(helmet)
            except:
                pass
            self.__wear_helmet = True
            self.__helmet = helmet

    def equip_a_shield(self, shield):
        if self.__wear_shield:
            print("Put off your current shield to take a new one")
        else:
            try:
                self.remove_from_inventory_by_obj(shield)
            except:
                pass
            self.__wear_shield = True
            self.__shield = shield

    def put_a_shield(self):
        if self.__wear_shield:
            self.__wear_shield = False
            self.__shield = None

    def equip_a_weapon(self, weapon):
        if self.__equiped_weapon:
            print("Put off your current weapon to take a new one")
            return
        else:
            try:
                self.remove_from_inventory_by_obj(weapon)
            except:
                pass
            self.__equiped_weapon = True
            self.__weapon = weapon
            self.__attack = self.__weapon

    def put_a_weapon(self):
        if self.__equiped_weapon:
            self.__equiped_weapon = False
            self.add_to_inventory(self.__weapon)
            self.__weapon = None
            self.reset_attack()

    def get_defense(self):
        defense = 0
        if self.is_equiped_armor():
            defense += self.__armor.get_value()
        if self.is_equiped_helmet():
            defense += self.__helmet.get_value()
        if self.is_equiped_shield():
            defense += self.__shield.get_value()

        if defense is 0:
            defense = self._LiveCreature__defense

        return defense

    def get_current_attack(self):
        if not self.__equiped_weapon:
            return self._LiveCreature__attack
        else:
            return self.__weapon.get_damage()

    def get_weapon(self):
        return self.__weapon

    def is_equiped_weapon(self):
        return self.__equiped_weapon

    def is_equiped_armor(self):
        return self.__wear_armor

    def is_equiped_helmet(self):
        return self.__wear_helmet

    def is_equiped_shield(self):
        return self.__wear_shield


class RandomСreature(LiveCreature):
    """Creates a random level creature """
    __id = 3

    def get_class_id(self):
        return self.__id

    def __init__(self, level=1):
        if level is 0:
            level = 1
        all = []
        f = open("database/creatures.txt", "r")
        for line in f:
            all.append(line)
        x = random.randint(0, len(all)-1)
        max_hp = random.randint(5+level, 15+level*2)
        d_attack = random.randint(1+level, 8+level*2)
        m_stamina = random.randint(1+level, 8+level*2)
        defense = random.randint(level, 5+level)
        LiveCreature.__init__(self, all[x], max_hp, 0, m_stamina, d_attack, defense)

