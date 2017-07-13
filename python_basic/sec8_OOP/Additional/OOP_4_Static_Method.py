class MyObject:
    class_attribute = 8

    def __init__(self):
        self.class_attribute = 42

    def siple_method(self):
        print(self.class_attribute)

    @staticmethod
    def static_method():
        print(MyObject.class_attribute)

if __name__ == "__main__":
    obj1 = MyObject()

    obj1.siple_method()
    obj1.static_method()

    MyObject.siple_method(obj1)
    MyObject.static_method()
