class Spam:
    numinstances = 0
    def count(cls):
        cls.numinstances +=1
    def __init__(self):
        self.count()
    count=classmethod(count)
class Sub(Spam):
    numinstances = 0
class Other(Spam):
    numinstances = 0
S = Spam()
y1,y2 = Sub(),Sub()
z1,z2,z3= Other(),Other(),Other()

print(S.numinstances, y1.numinstances,z1.numinstances)
print(Spam.numinstances, Sub.numinstances,Other.numinstances)
