class fraction_number:

    # value of numerator and denominator
    def __init__(self, num, den):
        self.num = num
        self.den = den


    def __str__(self):
        return "{}/{}".format(self.num,self.den)


    def show_result(self):
        return self.num, self.den

obj = fraction_number(3,4)
print(obj.show_result())

    