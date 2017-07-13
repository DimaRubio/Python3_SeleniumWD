print("*"*10,"Calculate Tax","*"*10)

def calculateTax(state , income):
    #Calculate income after federal tax
    income -= income * 0.1
    taxOfState = {
         "ny" : 0.08,
         "washington" : 0.10,
         "alabama" : 0.12
         }
    if state in taxOfState.keys():
        return income * taxOfState[state]

income = float(input("What is your income?"))
state = input("What state do you live in?").lower()
tax = calculateTax(state, income)
if tax != None:
    print(tax)
else:
    print("Something go wrong, maybe state does not exist, try again")