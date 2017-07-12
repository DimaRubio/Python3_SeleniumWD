class ListWrapper:

    def compose_list_from_string(self, s, sep=" "):
        return list(s.split())

    def compose_list_from_range(self, n):
        return list(range(n))

    def add_value_to_list(self, l, value):
        l.append(value)
        return l

    def insert_value_to_list(self, l, position, value):
        l.insert(position,value)
        return l

    def del_item_by_numder(self, l, number):
        l.pop(number)
        return l

    def del_item_by_valye(self, l, value):
        l.remove(value)
        return l

    def get_sub_list(self, l, start, end):
        l = l[start : end]
        return l

    def get_index_first_entry(self, l, value):
        return l.index(value)

if  __name__ ==  "__main__" :

    lw = ListWrapper()
    print(lw.compose_list_from_range(6))

    str_example = "test@test.qa 123456 Alex"
    cred = lw.compose_list_from_string(str_example)
    print(cred)
    cred = lw.add_value_to_list(cred, "Oreshkin")
    print(cred)
    cred = lw.insert_value_to_list(cred, 0, "testLogin")
    print(cred)
    cred = lw.del_item_by_numder(cred, 0)
    print(cred)
    cred = lw.del_item_by_valye(cred, "Oreshkin")
    print(cred)
    print(lw.get_index_first_entry(cred, "Alex"))
    cred = lw.get_sub_list(cred, 1, 3)
    print(cred)