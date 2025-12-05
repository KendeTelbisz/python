from datetime import date

class Ember:
    def __init__(self, nev, eletkor): #tulajdonságok, amiket megadhatok és dolgozhatok vele
        self.nev = nev #self az osztályon belüli műveletekhez 
        self.eletkor = eletkor

    def koszones(self):
        return f"Szia, {self.nev} vagyok, {self.eletkor} éves."
    
    def szuletesi_ev(self):
        aktualis_ev = date.today().year
        return aktualis_ev - self.eletkor
    
    def egy_ev_mulva(self):
        return self.eletkor + 1
    
    def noveli_eletkort(self, ev):
        self.eletkor += ev
    
ember1 = Ember("Anna", 30)
print(ember1.koszones())
print(ember1.szuletesi_ev())
ember2 = Ember("Béla", 35)
print(ember2.koszones())
print(ember2.szuletesi_ev())
ember3 = Ember("Sándor", 40)
print(ember3.koszones())
print(ember3.szuletesi_ev())