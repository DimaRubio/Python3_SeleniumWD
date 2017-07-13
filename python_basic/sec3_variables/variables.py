class Variables:
    s = "result = {0}"

    def compare_values(self, a, b):
        print("*"*10)
        print("a is: " + a)
        print("b is: " + b)
        return  self.s.format(a == b)

    def compare_ref(self, a, b):
        print("*"*10)
        print("a is: " + a)
        print("b is: " + b)
        return  self.s.format(a is b)

    def add(self, a, b):
        print("*"*10)
        return  self.s.format(a + b)

a="python"
b=a
c="selenium"

obj = Variables()
print(obj.compare_values(a, b))
print(obj.compare_ref(a, b))
print(obj.add(a, c))
print(obj.add("a", "c"))

a = " java"
print(obj.compare_values(a, b))
print("b is still: " + b)