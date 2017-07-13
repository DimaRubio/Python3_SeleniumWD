class TupleWrapper:

    def compose_tuple_from_string(self, s, sep=" "):
        return tuple(s.split())

    def compose_tuple_from_range(self, n):
        return tuple(range(n))

    def get_sub_tuple(self, l, start, end):
        l = l[start : end]
        return l

    def get_index_first_entry(self, l, value):
        return l.index(value)

if __name__ == "__main__":

    lw = TupleWrapper()
    print(lw.compose_tuple_from_range(6))

    str_example = "test@test.qa 123456 Alex"
    cred = lw.compose_tuple_from_string(str_example)
    print(cred)
    print(lw.get_index_first_entry(cred, "123456"))
    cred = lw.get_sub_tuple(cred,1,3)
    print(cred)

    t =("asf","xcb","zzz")
    print(t.index("zzz"))