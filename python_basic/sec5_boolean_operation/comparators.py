class Age:

    def not_equal(self, a, b):
        return print(a != b)

    def calculate_age(self, a):
        if a < 0  or a == 0 or a > 130: return print("wrong value")
        elif 0.1<a<=14: print("child")
        elif 14<a<=20: print("teenager")
        elif 20<a<=35: print("young")
        elif 35<a<=60: print("adult")
        elif 60<a<=130: print("Retired")
        else: print("something go wrong")
if __name__ == "__main__":
    x = float(input("your age? "))
    obj = Age()
    obj.calculate_age(x)

    obj.not_equal(x,10)