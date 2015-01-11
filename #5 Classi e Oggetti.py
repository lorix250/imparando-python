# Classi e Oggetti
# ================

# Le classi e gli oggetti sono il nostro metodo per descrivere i concetti del mondo ad un computer

# Un oggetto ha proprieta (variabili) e metodi (functions)
# Una classe e la definizione di come costruire un oggetto

# In principio, un oggetto non esiste senza una classe, e deve essere creato ed assegnato ad una variabile


# Definizione di una classe:
class Animale:  # nota che per destinguere tra le classi e le functions, le classi di solito vengono chiamate con la prima lettra maiuscola
    # Questo metodo si chiama il costruttore - e obbligatorio!
    def __init__(self, n_di_zampe, colore):
        # il costruttore va sempre chiamato __init__ e prende sempre come primo parametro self
        # self e una referenza a questa istanzea di un oggetto

        self.n_di_zampe = n_di_zampe
        self.colore = colore

    def mangia(self):
        # questo e un metodo della classe. Anche i metodi prendono sempre come primo parametro self
        # non e mai necessario specificarlo, perche e implicitamente passato con ogni oggetto
        print "mmmm che buono"

# Uso della classe - creazione di un oggetto
mioAnimale = Animale(4, "giallo")
# Come potete vedere, la creazione di un oggetto prende il nome di una classe, e poi sembra una function
# In fatti questo codice eseguisce il costruttore della classe, e per quello si passano i parametri.




# Eredita (classi basi e derivate)

# Una classe base e una classe che non deriva da nessuna classe
# Una classe derivata deriva alcuni dei suoi metodi e proprieta da un altra classe

# Per derivare una classe da un altra, mettere il nome di quella classe tra parentesi dopo il nome
# della classe nella definizione
class Cammello(Animale):
    def __init__(self, n_di_zampe, colore, n_di_gobbe):
        # Quando si deriva una classe, bisogna sempre eseguire il costruttore della classe base,
        # passando self e tutti gli altri parametri neccessari
        Animale.__init__(self, n_di_zampe, colore)

        self.n_di_gobbe = n_di_gobbe

    def camminare(self):
        print "uffa che lungo viaggio, meno male che sono un cammello"




# Proprieta e Metodi Statici

# A volte e utile gruppare functions e variabili ad una classe, ma non duplicarli per tutti gli oggetti
# creati da quella classe

# Per proprieta statiche, basta metterle fuori dal costruttore
class Esempio:
    proprieta_statica = "haha"

    def __init__(self):
        pass

# Invece per i metodi statici e un po piu complicato.
# Bisogna usare una decorazione
@staticmethod

class Esempio2:
    def __init__(self):
        pass

    @staticmethod
    def metodo_statico():
        pass


# (nel caso non lo sapevi, pass sarebbe come 'passa' - vuol dire che non fa niente)

