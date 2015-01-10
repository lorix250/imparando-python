class Cane:
    spece = 'canino'

    def __init__(self, nome):
        self.bisogno_di_cagare = False
        self.lunghezza = 66
        self.nome = nome
        self.eta = 3

    def mangiare(self):
        self.bisogno_di_cagare = True

    def caga(self):
        self.bisogno_di_cagare = False

    def compie_gli_anni(self):
        self.eta += 1

billy = Cane("Billy")
fufi = Cane("Fufi")

print billy.bisogno_di_cagare
print "Billy adesso mangia..."
billy.mangiare()
print billy.bisogno_di_cagare
print "Billy adesso va al gabinetto..."
billy.caga()
print billy.bisogno_di_cagare

print "Fufi adesso mangia..."
fufi.mangiare()
print "Fufi ha mangiato, e ha bisognio di cagare? " + str(fufi.bisogno_di_cagare)
fufi.caga()
print "Fufi ha cagato... si sente svuotato adesso..."
print fufi.bisogno_di_cagare


print Cane.spece

input()
