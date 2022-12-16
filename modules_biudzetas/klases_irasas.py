class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.info = info

    def __str__(self):
        return f"Pajamos: {self.suma}, siuntėjas - {self.siuntejas}, info: {self.info}"

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga, info):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
        self.info = info

    def __str__(self):
        return f"Išlaidos: {self.suma}, atsiskaitymo būdas - {self.atsiskaitymo_budas}, įsigyta prekė/paslauga - {self.isigyta_preke_paslauga}, info: {self.info}"
