# Variabili e Tipi
# ================ 
# Variabili sono dei dati che risiedono in un indirizzo in memoria del computer.
# Le variabili si devono definire e possono essere usate.
# Per definire una variabile, usare l'operatore dell'assegnamento ( = )

miaVariabile = 0

# In Python, le variabili sono di tipo dinamico - cioe, il tipo della variabile cambia a seconda del tipo del valore
# che c'e sulla destra del =
# Se hai una variablile String, puoi cambiarla in un Numero Intero solo assegnandola ad un numero intero.
# Per esempio:

miaVariabileString = "questo string"
miaVariabileString = 5
# ^ perfettamente valido... ma ti sconsiglio di chiamarla cosi se e questo l'uso inteso della variablile.

# Per usare le variabili, basta scrivere il loro nome dove vuoi usarle.
print miaVariabile + 5

# Puoi anche assegnare il valore di una variablile ad un'altra:
miaVariabile = miaVariabileString
# Non cambia niente perche la parte destra del =  e sempre valutata prima ed il valore finale assegnato alla variabile sulla sinistra
miaVariabileString = miaVariabile + 66 * 3 - 5

# ATTENZIONE! L'opposto non e valido, non puoi fare:
miaVariabile + 5 = 10
# Non e matematica, e Python...!



# Numeri Interi
# =============
# Un numero intero e lo stesso come in matematica - un numero senza numeri dopo la virgola.
# Attenzione pero! Se fai per esempio:
mioNumeroIntero = int(3.68)
# viene assegnato 3, non 4 come si penserebbe. Il computer non arrotonda I numeri decimali - taglia il pezzo decimale e basta!
# Se guardi sulle documentazioni sul modulo 'math', vedrai una function che arrotonda i numeri se ti serve...



# Numeri Reali
# ============
# I numeri reali sono i numeri decimali, non interi. 
piGreco = 3.14
# In realta ci sono due tipi: float e double.
piGreco = float(3.1415927)
# Per la spiegazione del perche, fai una ricerca su google per 'rappresentazione dei numeri decimali binari' o
# qualcosa del genere, e troverai qualcosa - se no te lo spiego un altra volta...



# Strings
# =======
# Gli Strings sono serie di caratteri, o frasi. Gli string vengono definiti usando le virgolette
# (singole o doppie, non importa)
mioStringUno = 'string esemplare'
mioStringDue = "che figata"

# ****Pero ricordati che gli string sono lo stesso variabili, e quindi per usarli devi usare il loro nome,
# e senza virgolette!****



# Manipolazione degli String
# ==========================
# Per accedere ad un pezzo di uno string, sono necessarie le parentesi quadre [ ]
# Il primo carattere di uno string ha indice 0, e tutti i seguenti hanno un indice di uno in piu del primo.
# Per accedere ad uno 'substring', o pezzo dello string, scrivere il nome della variabile, poi le parentesi
# quadre, e tra le parentesi l'indice iniziale, due punti, e l'indice finale:
mioStringDaManipolare = "Questo e il mio string"
mioStringDaManipolare[0:5] # ritorna "Questo"

# Delle functions utili per manipolare gli strings si trovano qui:


# Liste
# =====
# Le liste vengono definite come serie di variabili (o elementi), di qualsiasi tipo.
# Le liste vengono definite usando le parentesi quadre [ ]
miaLista = [ 1, "Due", 3.14, "qualcosa"]
# Gli elementi della lista, come i caratteri dello string, cominciano da indice 0 e aumentano. Quindi, per
# ottenere una variabile dentro ad una lista, scrivere il nome della lista, le parentesi quadre, e dentro l'indice
# dell'elemento desiderato.
miaLista[1] # mi da "Due"

# I tipi di variabili possono essere diversi nella stessa lista, ma se c'e bisogno che tutti gli elementi siano di un tipo,
# specificarlo nel codice con un commento (# ...)



# Dizionari
# =========
# I dizionari sono collezioni di variabili, dove si accede agli elementi usando una chiave, che corrisponde ad un valore.
# Dizionari vengono definiti con le parentesi graffe { }, ed ogni elemento viene scritto come chiave:valore
mioDizionario = { "chiave" : "valore", "chiave2" : 3 }

# Per accedere agli elementi contenuti nel dizionario, scrivere la chiave tra parentesi quadre, dopo il nome del dizionario:
mioDizionario["chiave"] # ritorna "valore"
mioDizionario["chiave2"] # ritorna 3



# Tuples
# ======
# Tuples vengono usati per rappresentare dei dati dove coppie o tris tornano utili.
# I tuples vengono definiti usando le parentesi tonde ( ) - occhio a non confondere tuples con functions!
mioTuple = ("valore A", "valore B")

# per accedere ai contenuti del tuple, (...patrick deve controllare come si fa...:D)



# Nesting
# =======
# Importante: Liste, Dizionari e Tuples, pur essendo collezioni di variabili, sono loro stesse variabili.
# Quindi, come elemento du una Lista, puoi avere un Dizionario etc...
# Questo concetto si chiama 'Nesting' - che proviene da Nest (Nido)
lista = [ { "puttana":"vacca"  }, (22, "Jump Street") ]
# In questo esempio, il dizionario ed il tuple sono 'Nested' dentro alla lista.
