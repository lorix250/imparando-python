# Lezione su Functions

# Questa e la definizione di una function. Comincia sempre con def, e poi uno spazio, 
# poi il nome della function. Subito attacato, vengono messe due parentesi tonde, con dentro i nomi dei
# parametri. I parametri sono cose che cambiano ogni volta che la function e chiamata (o usata)
def multiplicaPerDue(numero):
    return numero * 2
    # La parola chiave return e usata per 'ritornare' un valore quando la function e chiamata.
    # Functions senza valore di return vengono chiamate 'Procedures' (procedure) o 'Void Functions' (sara piu chiaro quando farai C++)

# In ogni caso qua sotto, la function viene 'chiamata', con un parametro diverso, che cambia l'output della function
print multiplicaPerDue(6)
print multiplicaPerDue(234)
print multiplicaPerDue(67890748682)



# Nota bene:
# Le functions eliminano la repetizione di codice. Se tu devi sempre fare una serie di operazioni due o tre volte,
# e meglio creare una function per generalizzare il codice - cosi il codice sembra piu 'pulito'.

# Nella definizione di una function, il parametro viene chiamato il parametro formale - perche viene sustituito con
# i valori passati alla function quando e chiamata. Questi valori si chiamano gli 'Actual Parameters' (credo si dicano parametri veri in Italiano)

# Adesso prova a creare diverse functions e utilizzarle!










input()