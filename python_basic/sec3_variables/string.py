class StringWrapper:

    def convert_case(self, s, case ="lower"):
        res = s.lower() if case=="lower" else s.upper()
        print("*"*10,
              "\nPrevious value is: {0}\n"
              "Current value is: {1}".format(s,res))

    def get_word(self, s, n = 0):
        wordList = s.split()
        return wordList[n-1] if wordList.__len__() >= n and n is not 0 else "out off range"

    def get_char_from_word(self, s, n = 0):
        return s[n-1] if s.__len__() >= n and n is not 0 else "out off range"

    def count_words_in_string(self, s):
        return s.split().__len__()

    def change_sub_string(self, s, old, new, count=0):
        return s.replace(old, new, count) if count is not 0 else s.replace(old, new)

    def get_sub_string(self, s, start, end):
        return s[start : end]


str_example = "SCRUM is a subset of Agile."

sw = StringWrapper()
sw.convert_case(str_example)
sw.convert_case(str_example, "upper")

print("Second char in sixth word of string \"{0}\" is = \"{1}\"".format(str_example, sw.get_char_from_word(sw.get_word(str_example, 6), 2)))
print("String contains of {0} words".format(sw.count_words_in_string(str_example)))
print(sw.change_sub_string(str_example, "is", "$"))
print(sw.get_sub_string(str_example, 0, 5))