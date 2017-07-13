class MyObject:
    pass

print(type(MyObject))
obj_1 = MyObject()
print(obj_1)
obj_2 = MyObject()
print(obj_2)
obj_1=obj_2
print(obj_1)
print(obj_2 is obj_1)