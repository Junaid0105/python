def info():
    temp = 23
    def info1():
        print("main function variable used by inner function : ",temp)
        # temp = 46
        print("updated value: ",temp)
    info1()
    print("Original value",temp)
info()

# def f1():
#     s = "Hello"
#     def f2():
#         print(s)
#     f2()
# f1()