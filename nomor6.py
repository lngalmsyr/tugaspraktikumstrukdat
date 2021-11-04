#jawaban nomer 6
"""
perbedaan antara fungsi __add dan fungsi __radd__ adalah jika pada fungsi radd akan menuar posisi dari nilai y
"""

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
    
    def  __add__ (self,otherfraction): 
        newnum = self.num*otherfraction.den + self.den*otherfraction.num 
        newden = self.den*otherfraction.den 
        common = gcd(newnum,newden) 
        return Fraction(newnum//common,newden//common)

    def  __radd__ (self, otherfraction): 
        if otherfraction == 0:
            return self
        else :
            otherfraction = Fraction(otherfraction, 1)
            return self.__add__(otherfraction)
 
    def __str__ (self): 
        return str(self.num)+"/"+str(self.den) 
 
    def show(self): 
        print(self.num,"/",self.den) 
 

    
    
    
x = Fraction(1,2) 
y = Fraction(2,3) 

print(x,y)
print("add=", x+y)
print("radd=", x+y)  
