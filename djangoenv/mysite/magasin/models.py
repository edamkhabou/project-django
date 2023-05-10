
from datetime import date
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User

class Produit(models.Model):    
    TYPE_CHOICES=[('em','emballé'),('fr','Frais'),('cs','Conserve')]
    libellé=models.CharField(max_length =100)
    description=models.TextField(default='Non définie')
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True,upload_to='media/')
    categorie=models.ForeignKey('Categorie',on_delete=models.CASCADE,null=True)
    fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "la libellé: "+f"{self.libellé} description: {self.description} prix:  {str(self.prix)} type:  {self.type}"
class Categorie(models.Model):
    choix=[('Al','Alimentaire'),
           ('Mb','Meuble'),
           ('Sn','Sanitaire'),
           ('Vs','Vaisselle'),
           ('Vt','Vétement'),
           ('Jx','Jouets'),
           ('Lg','Linge de Maison'),
           ('Bj','Bijoux'),
           ('Dc','Décor')]
    name=models.CharField(default='Al',max_length=100,choices=choix)
    def __str__(self):
        return "name: "+self.name  
class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField(default= 'Non définie')
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return "Le Nom: "+f"{self.nom} adresse: {self.adresse} email: {self.email} telephone: {self.telephone}"
class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return "la libellé: "+f"{self.libellé} description: {self.description} prix:  {str(self.prix)} type:  {self.type} Duree_grantie: {self.Duree_garantie}"
class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')
    def __str__(self): 
        return "date du commande: "+f"{self.dateCde} total du commande: {self.totalCde}"   
    # Create your models here.
    def __str__(self):
        return str(self.id)
class Panier(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    produits = models.ManyToManyField('Produit')

    def __str__(self):
        return f"Panier de {self.utilisateur.username}"