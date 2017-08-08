class Fruit:
    __weight = None
    def __init__(self):
        print("Base constructor ")

    def nutrition(self):
        print("Base: rational nutrition")

    def fruit_shape(self):
        print("Circle")

    def setWeight(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight


class Cherry(Fruit):
    def __init__(self, weight):
        super(Cherry, self).__init__()
        self.__weight = weight
        print("Child constructor ")

    def nutrition(self):
        print("Child method")

    def fruit_color(self):
        print("RED", )

    def getCherryWeight(self):
        return self.__weight

fruit = Fruit()
fruit.nutrition()
fruit.fruit_shape()
fruit.setWeight(1)
# print(fruit.__weight) #AttributeError: 'Fruit' object has no attribute '__weight'
print(fruit.getWeight())

print("*"*5)
cherry = Cherry(3)                  #Base constructor -> Child constructor
cherry.nutrition()                  #Child method
cherry.fruit_shape()                #Circle
cherry.fruit_color()                #RED
print(cherry.getCherryWeight())     #3




