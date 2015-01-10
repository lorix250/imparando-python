

class Animale:
    def __init__(self, n_di_zampe, colore, habitat):
        self.numero_di_zampe = n_di_zampe
        self.colore = colore
        self.habitat = habitat
        self.bisogno_di_cagare = False



class Dinosauro(Animale):
    def __init__(self, n_di_zampe, colore, habitat, spine):
        Animale.__init__(self, n_di_zampe, colore, habitat)
        self.spine = spine
        self.prehistorico = True

    def ruggire(self):
        print "ROOOOAAAAAARRRR"

    def mangiare(self):
        print "Mmm che buon T-REX"


class Ghepardo(Animale):
    def __init__(self, n_di_zampe, colore, habitat, occhi):
        Animale.__init__(self, n_di_zampe, colore, habitat)
        self.occhi = occhi

    def mangiare(self):
        print "Buona Gazella"


class Scatola:
    def __init__(self, cose):
        self.__n_di_cose = cose

    def aggiungi(self):
        self.__n_di_cose += 1

    def rimuovi(self):
        self.__n_di_cose -= 1

