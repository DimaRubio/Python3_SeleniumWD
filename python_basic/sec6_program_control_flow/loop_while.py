from python_basic.sec5_boolean_operation.comparators import Age

def calculate_age():
    answer="yes"
    answer_list = ("yes", "y")
    while answer in answer_list:
        x = float(input("your age?: "))
        obj = Age()
        obj.calculate_age(x)
        answer = str(input("Would you like to Continue ? ")).lower()
    else:
        print("=(")

if __name__ == "__main__":
    calculate_age()