class etudiant:
    def __init__(self,nom,note1,note2):
         self.nom = nom 
         self.note1 = note1
         self.note2 = note2
    
    def calcul_note_moyen(self,note1,note2):
         self.note1 = note1
         self.note2 = note2
         liste_note = [note1,note2]
         somme = sum(liste_note)
         moyenne = somme/2
         return moyenne
    def aff_nom_moyenne(self,nom,moyenne):
         self.nom = nom
         self.moyenne = moyenne
         aff_nom_moyenne = f"l'etudiant {nom} a eu comme moyenne"
         print(aff_nom_moyenne)

nom = input("entrer le nom de l'etudiant")
note1 = int(input("entrer la note 1"))
note2 = int(input("entrer la note 2"))

moyenne = etudiant(nom,note1,note2)
moyenne_calcul = moyenne.calcul_note_moyen(note1,note2)

affiche = etudiant(nom,note1,note2)
affiche.aff_nom_moyenne(nom,moyenne_calcul)