import random


class Location(object):
    """Main class of location"""
    __id = 11

    def get_class_id(self):
        return self.__id

    def __init__(self, name="small room", size=1, locked=False, special_type=0):
        self.__all_creatures = []
        self.__all_things = []
        self.__name = name
        self.__max_number_of_creatures = 0
        self.__current_number_of_creatures = 0
        self.__size = size
        self.__is_locked = locked
        self.__key = []

        if self.__is_locked:
            if self.__is_locked:
                for i in range(10):
                    self.__key.append(random.randint(0, 10000))

        if self.__size is 1:
            self.__max_number_of_creatures = 2
        elif self.__size is 2:
            self.__max_number_of_creatures = 4
        elif self.__size is 3:
            self.__max_number_of_creatures = 8
        elif self.__size is 4:
            self.__max_number_of_creatures = 100

    def open(self, key):
        if self.__is_locked:
            if key == self.__key:
                self.__is_locked = False

    def take_a_key(self):
        if self.__is_locked:
            return self.__key
        else:
            return None

    def get_type(self):
        return self.__size

    def get_max_number_of_creatures(self):
        return self.__max_number_of_creatures

    def get_current_number_of_creatures(self):
        return self.__current_number_of_creatures

    def get_all_things(self):
        return self.__all_things

    def add_thing(self, thing):
        self.__all_things.append(thing)

    def remove_thing_by_obj(self, thing):
        try:
            self.__all_things.remove(thing)
            return True
        except:
            return False

    def remove_thing_by_name(self, name):
        for _ in self.__all_things:
            try:
                if _.get_name() is name:
                    self.__all_things.remove(_)
            except:
                pass

    def add_creature(self, creature):
        if self.__current_number_of_creatures + 1 <= self.__max_number_of_creatures:
            self.__all_creatures.append(creature)
            return True
        else:
            return False

    def remove_creature_by_obj(self, creature):
        try:
            self.__all_creatures.remove(creature)
            return True
        except:
            return False

    def remove_creature_by_name(self, name):
        for obj in self.__all_creatures:
            try:
                if obj.get_name() is name:
                    self.__all_creatures.remove(obj)
                    return True
            except:
                pass
        return False

    def show_all_creatures(self):
        if not self.__is_locked:
            for obj in self.__all_creatures:
                try:
                    obj.info()
                except:
                    print(obj)

        else:
            print("room is closed")
