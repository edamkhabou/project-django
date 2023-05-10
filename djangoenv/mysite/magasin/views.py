from django.shortcuts import loader, redirect
from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Produit
from .forms import ProduitForm
from .forms import CommandeForm
from .models import Commande
from .models import Fournisseur
from .forms import ProduitForm,FournisseurForm,UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
"""def index(request):
    products=Produit.objects.all()
    context={'products':products}
    return render(request,'magasin/mesProduits.html',context)
    """
"""def index(request):
    if request.method == "POST" :
        form =FrsForm(request.POST)
        if form.is_valid():
            nom =form.cleaned_data ['nom']
            adr= form.cleaned_data['adr']
            frs=Fournisseur()
            frs.nom=nom
            frs.adr=adr
            form.save()
    else:
        form=FrsForm()
    return render(request,'magasin/testForm.html',{'form':form})
def Four(request):
    Fournis= Fournisseur.objects.all()
    context={'fournisseur':Fournis}
    return render(request,'magasin/mesFournisseur.html',context)
    """
"""def index(request):
    if request.method=="POST":
        form=ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else:
        list=Produit.objects.all()
        return render(request,'magasin/vitrine.html',{'list':list})
"""

@login_required
def listProd(request):
    list=Produit.objects.all() 
    return render(request,'magasin/produits/vitrine.html',{'list':list})
@login_required
def listFor(request):
    list=Fournisseur.objects.all()
    return render(request,'magasin/fournisseur/mesFournisseur.html',{'list':list})
def nouveauFournisseur(request):
    Fournis= Fournisseur.objects.all()
    context={'fournisseur':Fournis}
    return render(request,'magasin/fournisseur/mesFournisseur.html',context)
    # Create your views here.   """
def index(request): 
    return render(request,'magasin/base.html')
def AddProd(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('listProduits')
    else:
        form = ProduitForm()
    produits = Produit.objects.all()
    return render(request, 'magasin/produits/majProduits.html', {'produits': produits, 'form': form})
def AddFour(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('listFounisseur')
    else:
        form = FournisseurForm()
    fournisseur = Fournisseur.objects.all()
    return render(request, 'magasin/fournisseur/majFournisseur.html', {'fournisseur': fournisseur, 'form': form})
def register(request):
    if request.method == 'POST' :  
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('login')
    else :
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form' : form})
def EditProd(request, id):
    post = get_object_or_404(Produit, id=id)
    if request.method == 'GET':
        context = {'form': ProduitForm(instance=post), 'id': id}
        return render(request,'magasin/produits/editProduits.html',context)
    elif request.method == 'POST':
        form = ProduitForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('Produit')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'magasin/produits/editProduits.html',{'form':form})
def EditFour(request, id):
    post = get_object_or_404(Fournisseur, id=id)
    if request.method == 'GET':
        context = {'form': FournisseurForm(instance=post), 'id': id}
        return render(request,'magasin/fournisseur/editFournisseur.html',context)
    elif request.method == 'POST':
        form = FournisseurForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('Founisseur')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'magasin/fournisseur/editFournisseur.html',{'form':form})        
def DeleteProd(request, id):
    article = get_object_or_404(Produit, pk=id)
    context = {'article': article}    
    if request.method == 'GET':
        return render(request, 'magasin/produits/deleteProduits.html',context)
    elif request.method == 'POST':
        article.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('Produit')
def DeleteFour(request, id):
    article = get_object_or_404(Fournisseur, pk=id)
    context = {'article': article}    
    if request.method == 'GET':
        return render(request, 'magasin/fournisseur/deleteFournisseur.html',context)
    elif request.method == 'POST':
        article.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('Fournisseur')
class TaskDetail(DetailView):
    model = Produit
    context_object_name = 'produit'

@login_required
def add_commande(request):
    # Create an empty form for adding a new commande
    form = CommandeForm()

    if request.method == 'POST':
        # Fill the form with the submitted data
        form = CommandeForm(request.POST)

        if form.is_valid():
            # Save the commande instance to the database
            commande = form.save()

            # Add the selected products to the commande instance
            for produit_id in request.POST.getlist('produits'):
                produit = Produit.objects.get(id=produit_id)
                commande.produits.add(produit)

            # Update the totalCde field based on the selected products' prices
            total = sum([produit.prix for produit in commande.produits.all()])
            commande.totalCde = total
            commande.save()

            # Redirect to the detail view of the newly created commande
            return redirect('commande_detail', pk=commande.pk)

    context = {
        'form': form,
        'produits': Produit.objects.all(),
    }

    return render(request, 'magasin/cart.html', context)

def commande_detail(request,id):
    commande = get_object_or_404(Commande, pk=id)
    context = {
        'commande': commande
    }
    return render(request, 'magasin/commande/commande_detail.html', context)