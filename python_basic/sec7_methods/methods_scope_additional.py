def out_func():

    global var
    print(var)
    var = var+str(" has been changed in function")
    var1 = "local var1"

    def inner_func():
        nonlocal var1
        var1 = var1 + " has been changed in inner function"
        var2 = "inner var"
        print(var2)

    inner_func()
    print(var)
    print(var1)

if __name__ == "__main__":

    var = "global variable"
    out_func()
    print(var)