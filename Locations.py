class Location:
    """Main class of location"""
    __id = 11

    def get_class_id(self):
        return self.__id

    def __init__(self, name="small room", size=1, special_type=0):
        self.__all_creatures = []
        self.__name = name
        self.__max_number_of_creatures = 0
        self.__current_number_of_creatures = 0
        self.__size = size

        if self.__size is 1:
            self.__max_number_of_creatures = 2
        elif self.__size is 2:
            self.__max_number_of_creatures = 4
        elif self.__size is 3:
            self.__max_number_of_creatures = 8
        elif self.__size is 4:
            self.__max_number_of_creatures = 100

    def get_type(self):
        return self.__size

    def max_number_of_creatures(self):
        return self.__max_number_of_creatures

    def current_number_of_creatures(self):
        return self.__current_number_of_creatures

    def add_creature(self, creature):
        if self.__current_number_of_creatures + 1 <= self.__max_number_of_creatures:
            self.__all_creatures.append(creature)
            return True
        else:
            return False

    def remove_creature_by_obj(self, creature):
        for obj in self.__all_creatures:
            if obj is creature:
                self.__all_creatures.remove(obj)
                return True
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
        for obj in self.__all_creatures:
            try:
                obj.info()
            except:
                print(obj)
