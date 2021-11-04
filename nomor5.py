#jawaban nomer lima
def gcd(m,n): 
    while m%n != 0: 
        oldm = m 
        oldn = n 
 
        m = oldn 
        n = oldm%oldn 
    return n 

class Fraction: 
    def __init__(self,top,bottom): 
        self.num = int(top)
        self.den = int(bottom) 
        if int(self.den) < 0:
            self.den = abs(self.den)
            self.num=-self.num
        
    
    def __str__ (self): 
        return str(self.num)+"/"+str(self.den)
 
    
x = input("masukkan angka")
y = input("maskkan angka")
z= Fraction(x,y)


print(z)
