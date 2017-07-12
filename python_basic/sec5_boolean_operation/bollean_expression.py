class BoolExpresiion:
    def expression_1(self, a, b, c):
        return a and not b or c or (a and (b or c))

    def expression_2(self, a, b, c):
        return a or not b and c

a = True
b = False
c = True
print("a = {0}; b = {1}, c = {2}".format(a,b,c))
obj= BoolExpresiion()
f = a and not b or c or (a and (b or c))
print("expression result  \"a and not b or c or (a and (b or c)\" = {0}".format(obj.expression_1(a,b,c)))

print("expression result  \"a or not b and c\" = {0}".format(obj.expression_2(a,b,c)))

