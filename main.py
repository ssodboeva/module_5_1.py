class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to (self, new_floor):
        new_floor = int (new_floor)
        if new_floor > self.number_of_floors or new_floor < 1:
            print ('Такого этажа не существует')
        else:
            for floor in range (1,new_floor + 1):
                print (floor)

home = House ('ЖК "Эльбрус"', 30)
home.go_to (15)
home.go_to (31)
home.go_to (-1)