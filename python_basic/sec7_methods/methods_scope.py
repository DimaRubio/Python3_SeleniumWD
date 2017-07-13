var = "global variable"

def getLocalVAriable():
    var = "somestring Local"
    print(var)

def getGlobalVAriable():
    print(var)

def changeGlobalVAriable():
    global var
    var = "change "+ var
    print(var)

class Class_A:
    def getLocalVAriable(self):
        var = "somestring Local"
        print(var)

    def getGlobalVAriable(self):
        print(var)

    def changeGlobalVAriable(self):
        global var
        var = "change " + var
        print(var)

if __name__ == "__main__":
    getLocalVAriable()
    getGlobalVAriable()
    print(var)
    changeGlobalVAriable()
    getGlobalVAriable()

    print("*"*20)
    var = "global variable"
    obj = Class_A()

obj.getLocalVAriable()
obj.getGlobalVAriable()
print(var)
obj.changeGlobalVAriable()
obj.getGlobalVAriable()