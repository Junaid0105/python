# def fun1(*argv):

#     for arg in argv:
#         print(arg)
# fun1('hello','welocm',1,'python')

# keyword Argument (**kwargs)

# def fun2(**kwargs):
#     for k, val in kwargs.items():
#         print(k, "=", val)

# fun2(Junaid='CS',Jitu='Full Stack',Kaushik='Cyber Security')

def introduce(**kwargs):
    details = []
    for k, val in kwargs.items():
        details.append(k + ": " + str(val))
    return ", ".join(details)

print(introduce(Name = "Junaid", age = 25, place = "Amroha"))
