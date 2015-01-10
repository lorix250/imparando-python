class Agenda:
	def __init__(self, piatto, ricetta):
		self.piatto = piatto
		self.ricetta = ricetta

entrate = {
}

def inserisci(data, piatto, ricetta):
	entrate[data] = Agenda(piatto, ricetta)


def visualizza():
	for data in entrate:
		print"Data"+ data
		print"Piatto" + str(entrate[data].piatto)
		print"Ricetta" + str(entrate[data].ricetta)
		print"\n"


def elimina(data):
	del entrate[data]



print "cosa hai cucinato Elisabetta oggi."
while True:
	operazione = input("1 per aggiungere il piatto, 2 per rivedere il piatto, 3 per eliminare il piatto")
	if operazione < 1 or operazione > 3:
		print "Errore, riprova."
		continue

	if operazione == 2:
		try:
			visualizza()
		except:
			print "Eccezione"		
			continue


	if operazione == 1:
		data = raw_input("Inserire la data: ")
		piatto = raw_input("Inserire il piatto: ")
		ricetta = raw_input("Inserire la ricetta: ")


	if operazione == 3:
		data = raw_input("Inserire la data da eliminare: ")
		elimina(data)


