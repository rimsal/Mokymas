
import datetime

class Kursas:

    def __init__(self, pavadinimas, destytojas, trukme):
        self.pavadinimas = pavadinimas
        self.destytojas = destytojas
        self.trukme = datetime.datetime.strptime(trukme, "%Y-%m-%d")
        print(self.pavadinimas, self.destytojas, self.trukme)

    def destyti(self):
        print("Vyksta mokymas!")


