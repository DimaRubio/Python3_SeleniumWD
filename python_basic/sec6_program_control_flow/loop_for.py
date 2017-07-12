from python_basic.sec4_list_tuple_dictionary.work_with_list import ListWrapper
from python_basic.sec4_list_tuple_dictionary.work_with_dictionary import DictionaryWrapper

class Users:
    lw = ListWrapper()
    dw = DictionaryWrapper()
    def generate_users_dic(self, n):
        list_email = []
        list_password = []
        dic = {}
        count = 1
        for number in range(1,n+1):
            list_email = self.lw.add_value_to_list(list_email,"user{0}@test.qa".format(number))
            list_password = self.lw.add_value_to_list(list_password, "password{0}".format(number))
        for a,b in zip(list_email,list_password):
            dic = self.dw.add_value_to_dic(dic,"user{0}".format(count),{"email" : a ,"login" : b})
            count += 1
        return dic

users = Users()
dic_users = users.generate_users_dic(5) # generate 5 users
dw = DictionaryWrapper()
dw.print_dic_pairs(dic_users)   #displayed all users data
print("Get email for user3 from dictionary = {0}".format(dw.get_value_from_nested_dic(dic_users,"user3","email")))  #Get email for user3 from dictionary
