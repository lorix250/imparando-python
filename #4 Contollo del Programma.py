# Controllo del Programma
# =======================

if
elif
else

while 
for 
range()

# Condizionali (if/elif/else)
# ===========================
# I condizionali esistono per potere eseguire del codice solo se una condizione e vera, o falsa.
# Si usa la parola inglese per 'se', che sarebbe if  e poi la condizione prima dei due punti (:)
if condizione:
    blocco di codice da eseguire

# se invece vogliamo eseguire un codice diverso se la condizione e falsa, uare else (se no)
else:
    blocco di codice da esegire se la condizione e falsa

# Nota pero che else non va bene da solo, e deve venire sempre dopo if. Se vuoi eseguire solo un codice se la
# condizione e falsa e niente se e vera, hai due opzioni:
if condizione:
    pass
else:
    il tuo codice
# OPPURE
if not condizione:
    il tuo codice
# Se guardi la lezione 'Logica e Boleani', l'operatore not e descritto li.


# A volte, torna utile gruppare degli if con gli elif, per esempio se hai diverse cose da controllare:
if condizione1:
    codice se condizione1 e vera
elif condizione2:
    codice se condizione2 e vera
elif condizione3:
    codice se condizione3 e vera
else:
    codice se nessuna condizione e vera

# ricorda pero che in questo metodo, se condizione 1 e vera, condizione2 e 3 non vengono mai controllate.
# Se vuoi controllarle tutte (che e a volte l'uso inteso), basta fare degli if separati

if condizione1:
    # blabla

if condizione2:
    # blabla

# Questo torna utile se 2 o piu condizioni possono essere vere




# Cicli
# =====
# I cicli servono per ripetere un codice diverse volte.
# Il ciclo piu semplice e while. While ripete il codice fino a che la condizione diventa falsa.
# (while e mentre in inglese, quindi pensaci come: mentre condizione e vera)
while condizione:
    ripeti questo
# per uscire dal ciclo senza la condizione essendo falsa, occorre la parola d'ordine
    break

# per saltare tutto il codice sotto ad una linea e avanzare alla possima ripetizione, occorre
    continue

# C'e un altro tipo di ciclo, ma che viene usato in un modo diverso. Il ciclo 'for', viene usato per:
# 1. ripetere un codice un numero fisso di volte ( usando la function range() )
# 2. eseguire un pezzo di codice per ogni elemento in una lista, un dizionario o un tuple

for elemento in lista:
    fai questo
# interessante da notare e che viene creata una variabile (elemento) con scopo locale per potere fare
# qualcosa con ogni elemento.
# 'in' vuol dire  'dentro a' o 'nel/nella'
# 'for' (in questo contesto) voil dire 'per ogni'
# Quindi ' per ogni elemento dentro alla lista: '

# Per l'uso numero 1, ripetere un codice un numero di volte (numero fisso), ci vuole la function
range()
# Range ritorna una lista con i numeri 0 fino a il numero specificato come parametro:
range(5) # ritorna una lista: [0, 1, 2, 3, 4, 5]

# se vuoi specificare l'inizio, puoi anche farlo prendere 2 parametri:
range(1, 5) # ritorna [1, 2, 3, 4, 5]

# Quindi utilizzando range si puo metterlo in for:
for numero in range(1, 5):
    # fai qualcosa 5 volte
# nota che lo stesso, la variabile numero e creata col'elemento della lista della ripetizione in questione
# quindi numero serve per vedere a quale ripetizione siamo, che puo tornare utile
# Nota anche che numero puo essere chiamato qualsiasi cosa, e un nome di una variabile!

# Anche, le istruzioni break e continue sono valide anche per cicli for.
# Procedendo uno dopo l'altro negli elementi di una lista viene chiamato 'Iterazione' (Iteration),
# quindi se mi senti parlarne poi capirai.