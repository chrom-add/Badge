#Vous disposez d'une classe "Animal" décrite ci-dessous : Créer les classes "Chien", "Chat", et "Poulpe" comme suit

  #constructor(nom, age, pattes, espece, status) {
    #this.nom = nom;
    #this.age = age;
    #this.pattes = pattes;
    #this.espece = espece;
    #this.status = status;
  #}
  #sePresenter() {
    #return `Bonjour, mon nom est ${this.nom} et j'ai  ${this.age} ans.`;
  #}
#}
#Définir une classe Poulpe grâce à la classe animal : un poulpe a toujours 8 "pattes", son espèce est égale à "poulpe"

#Définir une classe Chat grâce à la classe animal : un chat a toujours 4 "pattes", son espèce est égale à "chat". La fonction "se présenter" du chat devrait par contre donner la même phrase que les autres animaux, mais avec "miaou miaou" ajouté à la fin

#Définir une classe Chien grâce à la classe animal : un chien a toujours 4 "pattes", son espèce est égale à "chien". Le chien possède en plus une méthode "accueillirSonMaitre" qui ne prend pas d'argument et qui renvoie "Bonjour" ${this.maitre}

#---------------------------------------------------------------------------#

class Animal :
    def __init__(self,nom,age,pattes,espece,status):
        self.nom = nom,
        self.age = age, 
        self.pattates = pattes,
        self.espece = espece,
        self.status = status
    
    def sePresenter(self):
        print("Bonjour je m'appel", self.nom,"et j'ai",self.age," ans")

#class Fille 
class Poulpe(Animal):
    def __init__(self,nom,pattes,espece):
        self.nom = nom,
        self.pattes = pattes,
        self.espece = espece
    
    def sePresenterPoulpe(self):
        print("Bonjour moi je suis un ",self.espece, "mon nom est : ",self.nom," j'ai ",self.pattes," pattes")

class Chat(Animal):
    def __init__(self,nom,espece,pattes,miaou):
        self.nom = nom,
        self.espece = espece,
        self.pattes = pattes,
        self.miaou = miaou
    def sePresenterCat(self):
         print("Bonjour je m'appel", self.nom,"je suis un ",self.espece,self.miaou)


class Chien(Animal):
    def __init__(self,nom,espece,pattes,maitre):
        self.nom = nom,
        self.espece = espece,
        self.pattes = pattes,
        self.maitre = maitre
    def accuueilllirMaitre(self):
        print("OUAFF OUAFF bonjour ",self.maitre)
        

    
    



    

#Instanciation Poule

InstancPoulpe = Poulpe("POULPI",8,"Poulpe")

#Instance Chat 

InstanceChat = Chat("Felix","chat",4,"Miaouu")

#Instanciation de chien

dog = Chien("Max","Chien",4,"Maitre")


InstancPoulpe.sePresenterPoulpe()
InstanceChat.sePresenterCat()
dog.accuueilllirMaitre()