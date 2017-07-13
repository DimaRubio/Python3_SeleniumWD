class DictionaryWrapper:

    def add_value_to_dic(self, dic, key, value):
        dic[key] = value
        return dic

    def print_dic_keys(self, dic):
        for k in dic:
            print(k)
        print("*" * 10)

    def print_dic_pairs(self, dic):
        for k,v in dic.items():
            print(k,v)
        print("*" * 10)

    def get_value_from_dic(self, dic, key):
        return dic[key]

    def get_value_from_nested_dic(self, dic, key1, key2):
        return dic[key1][key2]

if  __name__ ==  "__main__" :

    car = {"label": "bmv", 'model':'720i'}
    dw = DictionaryWrapper()
    car = dw.add_value_to_dic(car,"year", 2011)
    car = dw.add_value_to_dic(car,"milage", 100000)
    print(car)
    print(dw.get_value_from_dic(car, "model"))
    dw.print_dic_keys(car)
    dw.print_dic_pairs(car)

    #Work with nested dictionarys
    users = {'user1' : {'email' : 'user1@test.qa', 'password': 123456},
             'user2' : {'email' : 'user2@test.qa', 'password': 222222},}
    users = dw.add_value_to_dic(users,'user3',{'email' : 'user2@test.qa', 'password': 333333})
    dw.print_dic_keys(users)
    dw.print_dic_pairs(users)
    print("Your email is: {0}".format(dw.get_value_from_nested_dic(users,"user3","email")))
