from django.contrib import admin
from .models import Produit,Categorie,Fournisseur,ProduitNC,ProduitC,Commande
# Register your models here.
admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Fournisseur)
admin.site.register(ProduitNC)
admin.site.register(ProduitC)
admin.site.register(Commande)