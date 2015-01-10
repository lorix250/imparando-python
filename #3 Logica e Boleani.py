# Operazioni Logiche
# ==================
# Se avete gia fatto i numeri binari, forse questo lo saprai gia.
# Le operazioni logiche sono:
and # e (questo e questo)
or # o (questo o questo)
not # non (non questo == quell'altro)

# Quindi, come esempio, guardiamo questao codice:
miaVariabile = 5
miaVariabile < 6 and miaVariabile > 4 
# verra vero, perche? Perche miaVariabile e meno di 6  e anche  miaVariabile e piu di 4

# Adesso cambiamo qualcosa:
miaVariabile > 6 and miaVariabile > 4
# Questo ritornera falso. Perche?
# Perche miaVariabile non e piu di 6, e si come con 'and' tutte due condizioni devono essere vere,
# questo sara falso.

# Adesso pero, utilizziamo or
miaVariabile > 6 or miaVariabile > 4
# Questo ritornera VERO, perche con or, solo una delle due condizioni deve essere vera.
# Qui  miaVariabile > 6 e falsa, ma  miaVariabile > 4 e vera, quindi l'espressione viene valutata a vero

# Non esiste in Python, ma e buono notare che esiste anche 'Exclusive Or' (o esclusivo) [ che viene chiamato anche XOR ]
# Con or, se tutte due condizioni sono vere, e lo stesso vero. Ma con XOR, se tutte due sono vere, l'esspressione
# diventa falsa! Quindi con XOR o uno o l'altro, non tutti e due. Pero non esiste in Python - e solo una cosa interessante
# che ti aiutera nel futuro (e nel C++)...


# Finalmente, guardiamo not
# Not server per invertire un valore boleano
# Se hai un espressione che ritorna vero e la precedi con not, diventa falsa
not True  # == False