class Personne():
    def __init__(self,nom,age,metier):

        self.nom = nom
        self.age = age
        self.metier = metier

    def presentation(self):

        print(f"je suis {self.nom}, je suis {self.metier} et j'ai "+ str(self.age))


p1 = Personne("Guy",26,"Etudiant")

p1.presentation()