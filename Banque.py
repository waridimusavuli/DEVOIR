class Account:
    def __init__(self,soldInitial=0):
        self.SoldeInitial =soldInitial
        self.soldeActuel =self.SoldeInitial
    def getBalance(self):
        return self.soldeActuel
    def deposer(self,montant):
        self.soldeActuel=self.soldeActuel+montant
    def retirer(self,montant):
        self.soldeActuel=self.soldeActuel-montant
    def AjouterInteret(self,taux):
        self.soldeActuel =self.soldeActuel*(1+taux)

nouveauCompte=Account()
nouveauCompte.deposer(60)
nouveauCompte.retirer(20)
nouveauCompte.AjouterInteret(2)
print(nouveauCompte.getBalance())