from django.urls import path
from . import views
from .views import TaskDetail
from django.urls import path
from .views import CategoryAPIView,ProduitAPIView

from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns =[
    path('',views.index,name='index'),
    path('listProduits',views.listProd,name='Produit'),
    path('listFounisseur',views.listFor,name='Founisseur'),
    path('ajouterProd',views.AddProd,name='AddProd'),
    path('ajouterFour',views.AddFour,name='AddFour'),
    path('produit/edit/<int:id>/', views.EditProd, name='EditProd'),
    path('founisseur/edit/<int:id>/', views.EditFour, name='EditFour'),
    path('produit/delete/<int:id>/', views.DeleteProd, name='DeleteProd'),
    path('founisseur/delete/<int:id>/', views.DeleteFour, name='DeleteFour'),
    path('detail/<int:pk>/',TaskDetail.as_view(),name='detail'),
    path('nouvFourbisseur/',views.nouveauFournisseur,name='nouveauFour'),
    path('register/',views.register, name = 'register'),
    path('password-reset/', PasswordResetView.as_view(template_name='magasin/password_reset.html',html_email_template_name='magasin/password_reset_email.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='magasin/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='magasin/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='magasin/password_reset_complete.html'),name='password_reset_complete'),
    path("add_commande",views.add_commande,name="Commande"),
    path('detail_commande/<int:id>/',views.commande_detail,name="detailcomm"),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/',ProduitAPIView.as_view())
]