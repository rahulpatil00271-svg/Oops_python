class Fraction:

    def __init__(self,n,d):
        self.num = n
        self.den = d

x = Fraction(4,5)

print(x.num)
print(x.den)

    def __str__(self):
        return "{}/{}".format(sel.num,self.den)