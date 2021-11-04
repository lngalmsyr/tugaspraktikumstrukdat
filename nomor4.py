#jawaban nomer empat
def gcd(m,n): 
    while m%n != 0: 
        oldm = m 
        oldn = n 
 
        m = oldn 
        n = oldm%oldn 
    return n 

class Fraction: 
    def __init__(self,top,bottom): 
        try:
            self.num = int(top) 
            self.den = int(bottom) 
        except ValueError:
            print("wrong data type")
            exit()
    
    def __str__ (self): 
        return str(self.num)+"/"+str(self.den)
 
    
x = input("masukkan angka =")
y = input("maskkan angka =")
z= Fraction(x,y)


print(z)
