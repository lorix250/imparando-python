# Risassunto delle Variabili
# ==========================

# Per ricapitolare: I valori esistono anche non essendo assegnati ad una variabile
5 + 6
True

# quindi questo codice:
numero = 5 + 6
function(numero)
# e questo:
function(5 + 6)
# hanno lo stesso effetto


# Allora perche usare una variabile? Be l'indizio e nel nome - quando hai qualcosa che varia
# Poi, le variabili si usano per sostituire un valore (che chambia) al posto di una costante

while True:
    numero = input("Inserisci un numero: ")
    print "Il tuo numero e " + str(numero)
# In questo esempio, ogni volta che l'utente viene chiesto di inserire un nuovo numero, 
# il valore della variabile 'numero' cambia. E poi usata per scrivere il numero all'utente



# Scopo
# Ricordati che le variabili hanno scopo!

variabile_globale = "io sono definito nello scopo globale"

if (qualche condizione):
    variabile_locale = "io sono definito nelllo scopo locale, e saro distrutto quando si esce dal blocco"

# Quindi questa linea di codice da un errore:
print variabile_locale
# Perche? Perche quando e definita una variabile con scopo locale, non si puo utilizzarla da fuori di
# questo scopo, e alla fine del blocco, quel pezzo di memoria viene liberato.

