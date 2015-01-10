import random
import time

random.seed(time.time())
print "Sasso, Carta e Forbici \n"

scelte = {
    "sasso" : 1, "carta" : 2, "forbici" : 3
}

while True:
    print "Scegli un optzione"
    scelta_del_utente = raw_input()
    
    try:
        scelte[scelta_del_utente]
    except:
        print "Non e un valore valido"
        continue

    scelta_del_computer = random.randint(1, 3)

    if scelte[scelta_del_utente] == 1:
        if scelta_del_computer == 2:
            print "Utente: Sasso, Computer: Carta, vince il computer"
        else:
            print "Utente: Sasso, Computer: Forbici, vince l'utente"

    if scelte[scelta_del_utente] == 2:
        if scelta_del_computer == 3:
            print "Utente: Carta,  Computer: Forbici, vince il computer"
        else:
            print "Utente: Carta,  Computer: Sassom, vince l'utente"

    if scelte[scelta_del_utente] == 3:
        if scelta_del_computer == 1:
            print "Utente: Forbici,  Computer: Sasso, vince il computerq"
        else:
            print "Utente: Forbici,  Computer: Carta, vince l'utente"

