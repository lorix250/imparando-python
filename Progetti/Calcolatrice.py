print "Benvenuti nella nostra Calcolatrice!\n"

while True:
    modo_di_operazione = input("Scegliere 1 per addizione, 2 per sottrazione, 3 per multiplicazione e 4 per divisione")
    if(modo_di_operazione not in range(1, 5)):
        print "Errore! Non hai scelto un operazione valida!"
        continue

    primo_numero = input("Inserire il primo numero: ")
    secondo_numero = input("Inserire il secondo numero: ")

    if(modo_di_operazione == 1):
        print primo_numero + secondo_numero

    if(modo_di_operazione == 2):
        print primo_numero - secondo_numero

    if(modo_di_operazione == 3):
        print primo_numero * secondo_numero

    if(modo_di_operazione == 4):
        print primo_numero / secondo_numero

