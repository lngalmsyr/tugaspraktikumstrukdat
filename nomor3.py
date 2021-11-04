#jawaban nomer tiga
def gcd(m,n): 
    while m%n != 0: 
        oldm = m 
        oldn = n 
 
        m = oldn 
        n = oldm%oldn 
        return n 

class Fraction: 
    def __init__(self,top,bottom): 
        self.num = top 
        self.den = bottom 
 
    def __str__ (self): 
        return str(self.num)+"/"+str(self.den) 
 
    def show(self): 
        print(self.num,"/",self.den) 
    
    def __eq__ (self, other): 
        firstnum = self.num * other.den 
        secondnum = other.num * self.den 
        return firstnum == secondnum 
    
    def __gt__ (self, other): 
        firstnum = self.num * other.den 
        secondnum = other.num * self.den 
        return firstnum > secondnum 

    def __ge__ (self, other): 
        firstnum = self.num * other.den 
        secondnum = other.num * self.den 
        return firstnum >= secondnum 

    def __lt__ (self, other): 
        firstnum = self.num * other.den 
        secondnum = other.num * self.den 
        return firstnum < secondnum 

    def __le__ (self, other): 
        firstnum = self.num * other.den 
        secondnum = other.num * self.den 
        return firstnum  <= secondnum 

    def __ne__ (self, other): 
        firstnum = self.num * other.den 
        secondnum = other.num * self.den 
        return firstnum != secondnum 

x = Fraction(2,3) 
y = Fraction(3,8) 
print(x,y)
print(x == y)
print(x > y)
print(x >= y)
print(x <=y)
print(x < y)