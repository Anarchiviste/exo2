import datetime

class Personne():

    def __init__(self, data):

        self.data = data

    

    def etat_civil(self): 

        return self.data["prenom"]  + " " + self.data["nom"]



    def age(self):

        aujourdhui = int(datetime.date.today().year)

        return int(aujourdhui - int(self.data["annee_naissance"]))



data = {

    "annee_naissance": "1966",

    "nom" : "Dupont",

    "prenom": "Jean"

}



# instanciation de la classe Personne: personne est une instance de Personne()

personne = Personne(data)



# on accède ensuite aux différents attributs et méthodes de la classe Personne() pour notre instance personne

# cas 1

print("Cas 1 : Personne(data).data ")

print(personne.data)



# cas2

print("Cas 2 : Personne(data).etat_civil()")

print(personne.etat_civil())



# cas3

print("Cas 3 : Personne(data).age()")

print(personne.age())