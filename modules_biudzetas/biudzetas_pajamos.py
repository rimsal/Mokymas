from modules_biudzetas.klases_irasas import PajamuIrasas, IslaiduIrasas

class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma, siuntejas, info):
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)

    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga, info):
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga, info)
        self.zurnalas.append(irasas)

    def gauti_balansa(self):
        bendrasuma = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                bendrasuma += irasas.suma
            if type(irasas) is IslaiduIrasas:
                bendrasuma -= irasas.suma
        return bendrasuma

    def gauti_ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)
