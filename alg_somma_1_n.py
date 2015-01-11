# Algoritmo per la somma dei numeri da 1 a n

# Questa sara un po matematicosa e noiosa ( uffa :/) - ma ti insegnera a programmare un Algoritmo

# Se vuoi fare la somma di una serie di numeri da 1 a n, come puoi fare?
# 1, 2, 3, 4, 5, 6, 7
# 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28

# Quindi usando questo metodo, viene da usare un ciclo for
somma = 0
for numero in range(1, 7):
    somma += numero

print somma

# Prova a replicarlo tu, ma usando una function che prende n come parametro, chiamata somma_1aN(n)
# Non oltrepassare la linea di ====  fino a che non l'hai fatto!













# =======================================================================================




# In realta, un genio matematico chiamato Gauss ha sviluppato un metodo mollto migliore,
# e quando aveva solo 12 anni!! (Oh dio Patrick, esiste un genio piu genio di te hahahaha)


# Lui ha avuto l'idea di accoppiare i numeri in questo metodo:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
(1+8) + (2+7) + (3+6) + (5+4)
9 + 9 + 9 + 9
9 * 4
36

# Oppure:
(n + 1) * (n / 2)

( n * (n+1) ) / 2

# Questa e la formula di Gauss.
# Adesso, crea un'altra function, chiamata somma_gauss(n) che prende n come parametro,
# e utilizza la formula di Gauss
