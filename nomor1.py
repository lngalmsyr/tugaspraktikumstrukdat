class pecahan :
  def __init__(self, atas, bawah):
    self.num = atas
    self.den = bawah

  def __str__(self):
    return "pembilang is "+str(self.num)+", penyebut is "+(self.den)

x = input("pembilang =")
y = input("penyebut =")
z = pecahan(x,y)
print (z)