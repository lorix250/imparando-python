import random
import time

random.seed(time.time())

scelte = {
    "sasso" : 1,
    "carta" : 2,
    "forbice" :3
}

while True:
    print "sasso, carta, forbice!"
    scelta_del_utente = raw_input()
    try:
        scelte[scelta_del_utente]
    except:
        print "error"
        continue


    scelta_del_computer = 0

    if scelte[scelta_del_utente] == 1:
        scelta_del_computer = 2
        print "vince il computer con la carta"

    if scelte[scelta_del_utente] == 2:
        scelta_del_computer = 3
        print "vince il computer con la forbice"

    if scelte[scelta_del_utente] == 3:
        scelta_del_computer = 1
        print "vince il computer con il sasso"

    






