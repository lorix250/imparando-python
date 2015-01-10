# impostare
import random
import time
random.seed(time.time())

while True:
    print "Indovina il numero! (e tra 0 e 10)"
    numero_indovinato = input()
    numero_randomizzato = random.randint(0, 10)

    if numero_indovinato == numero_randomizzato:
        print "Che figo! L'hai indovinato!"
    else:
        print "Hmm...non e quello..."