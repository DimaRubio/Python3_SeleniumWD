class Boolean:
    s = "result = {0}"

    def compare_values(self, a, b):
        print("*"*10)
        print("a is: " + str(a))
        print("b is: " + str(b))
        print(self.s.format(a == b))

    def add(self, a, b):
        print("*"*10)
        print("a is: " + str(a))
        print("b is: " + str(b))
        print(self.s.format(int(a) + int(b)))

a = True
b = False

obj = Boolean()

obj.compare_values(a, b)
obj.compare_values(a, 1)
obj.compare_values(b, 0)
obj.compare_values(b, bool(""))
obj.compare_values(a, bool("one char"))

obj.add(a,a)
obj.add(a,b)
obj.add(a,10)





