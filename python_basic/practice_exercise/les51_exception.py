print("*"*10,"Calculate Tax using Exception","*"*10)

def calculateTax(state , income):
    #Calculate income after federal tax
    income -= income * 0.1
    res = 0
    taxOfState = {
         "ny" : 0.08,
         "washington" : 0.10,
         "alabama" : 0.12
         }
    try:
        res = income * taxOfState[state]
    except:
        res = "Something go wrong, maybe state does not exist, try again"
    finally:
        return res

def input_float_value(x):
    value = None
    try:
        value = float(x)
        print(value)
    except:
        print("The entered value is not a number.")
        value = input_float_value(input("What is your income?"))
    finally:
        return value

income = input_float_value(input("What is your income?"))
state = input("What state do you live in?").lower()
print("Your tax = {0} ".format(calculateTax(state, income)))