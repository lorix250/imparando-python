# Ho trovato questo sulla documentazione in inglese di Python e l'ho tradutto in italiano.
# L'ho visto e o detto: questo codice insegnera qualcosa a tutti!
# E di una function 
# Guarda se capisci cosa intendeva il programmatore.

# =====
# Nota che per vedere se una lista, dizionario o un tuple contiene un valore o dei valori, puoi fare:
miaLista = [ 1, 6, "zeta"]
if valore in miaLista:
    pass # (pass non fa niente...)
# 'in' in questo senso sarebbe 'nel/nella', quindi:
# if valore in miaLista
# se valore nella miaLista
# =====

def chiedi_ok(domanda_al_utente, numero_di_riprove=4, lamento='Si or no, per favore!'):
    while True:
        ok = input(domanda_al_utente)

        if ok in ('y', 'ye', 'yes', 'si', 'ok'):
            return True

        if ok in ('n', 'no'):
            return False

        numero_di_riprove = numero_di_riprove - 1

        if retries < 0:
            raise OSError('uncooperative user')

        print(lamento)

# Pensa a questo:  in un codice tuo, come useresti questa function? che funzione ha?
# Dovrebbe essere facile dal nome, pero guarda specialmente il blocco if dove viene 'raise'...
# Cosa si dovrebbe fare, per evitare al programma di terminare nel caso che quel blocco arriva 
# ad essere eseguito...  

# c'e un indizio piu in giu se sei un po confuso



















# Indizio: Eccezioni