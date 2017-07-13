empty_list = []
print(empty_list)               #[]

int_list = [1, 2 , 3 , 4]
print(int_list)                 #[1, 2, 3, 4]

list_from_range = list(range(5))
print(list_from_range)              #[0, 1, 2, 3, 4]

list_from_string = list("a list")
print(list_from_string)             #['a', ' ', 'l', 'i', 's', 't']

exampleString = "Example string 1"
if "str2" in exampleString:
    print(True)
else: print(False)                  #False

for char in exampleString:
    print(char, end=", ")           #E, x, a, m, p, l, e,  , s, t, r, i, n, g,  , 1,

print("_________")
int_list.append("abc")
for char in int_list:
    print(char, end=", ")           #1, 2, 3, 4, abc,
del int_list[4]
for char in int_list:
    print(char, end=", ")           #1, 2, 3, 4,