# Gestione delle Eccezioni
# ========================
# Parole chiavi
try
except
else
finally
raise

# Quando viene un errore, viene creata un eccezione. 
# Le eccezioni non 'gestite' terminano l'esecuzione del programma.

# Guarda la struttura di una gestione di eccezioni

try:
    # Dentro al blocco try viene messo il codice che puo dare un eccezione, dove noi la vogliamo gestire.
except Exception, e:
    # Il blocco except prende il tipo di eccezione, e poi un nome (in questo caso 'e') che viene usato per riferire all'eccezione.
    # Il codice dentro a questo blocco si esecuta solo se un eccezione e creata.
    # Se non specifici niente dopo except, vale per tutte le eccezioni.
else:
    # Il blocco else non e obbligatorio, ed e per istruzioni che avvengono solo se non vengono create eccezioni.
    # Nota che questo else e diverso da quello usato con if. 
    # Questo avviene se non vengono eccezioni, l'else di if avviene se la condizione e falsa - ricordati!
finally:
    # E, finalmente, il blocco finally sono delle istruzioni da fare in tutti i casi, se viene un eccezione o no


# Creare le Eccezioni
# ===================
# Quando diventerai piu esperto, vorrai creare codice che crea le eccezioni se c'e un errore.
# Per fare questo, e necessario utilizzare la parola chiave
raise
# ( In inglese, creare un eccezione si dice "Raise an Exception" )

# Le eccezioni sono comunque classi, quindi puoi difinire anche nuove eccezioni!
# Basta derivare la classe dalla classe
Exception

class MiaEccezione(Exception):
    def __init__(self, messaggio):
        self.messagio = messaggio

# ...
raise MiaEccezione("C'e un errore!")
# ...