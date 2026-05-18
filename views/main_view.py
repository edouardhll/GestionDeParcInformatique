import tkinter as tk
from tkinter import *
from tkinter import ttk
from views.fonction_view import github
from database.requetes import ajouter_equipement, lire_equipement, delete_equipement, maj_equipement


#----------Définition des polices----------#
h1p = "Manrope"
h2p = "Inter"


#----------Définition des couleurs----------#
bgc = "#F2F3FF"
h1c = "#131B2E"
h2c = "#434655"


#----------Création de l'app dans une fonction'----------#
def lancer_app():

    #----------Création de la fenêtre----------#
    root = Tk() #création de la première fenêtre
    root.title("Gestionnaire de parc informatique") #le nom affiché de la fenêtre
    root.geometry("1280x720") #donne une taille à la fenêtre quand elle s'ouvre
    root.minsize(720, 480) #donne une taille minimal à la fenêtre ne pouvant pas être réduite
    root.iconbitmap("./assets/logo.ico") #donne un logo à l'app
    root.config(background=bgc) #couleur de l'arrière plan de la fenêtre


    #----------Création du cadre ACCUEIL ----------#
    home= Frame(root, bg=bgc, bd=1, relief=SUNKEN)
    home.pack(expand=YES)

    #----------Définition du titre----------#
    label_title = Label(home, text='Gestionnaire de parc informatique', font=(h1p, 30), bg=bgc, fg=h1c)
    label_title.pack(expand=YES)

    #----------Création du bouton github----------#
    boutongithub = Button(home, text="Consulter mon github", font=(h2p, 15), bg=bgc, fg=h2c, activebackground=bgc, command=github)
    boutongithub.pack(fill=X, pady=25,)

    #----------Création du bouton lire----------#
    open = Button(home, text="Lire la bdd", font=(h2p, 15), bg=bgc, fg=h2c, activebackground=bgc, command=lambda: entry(home, root))#appelle la fonction pour la nouvelle fenêtre, on importe home et root pour pouvoir les reconnaitre
    open.pack(fill=X, pady=25,)

    #----------Exécution de la fenêtre----------#
    root.mainloop() #afficher la fenêtre

def entry(home, root):
    home.pack_forget() #on ferme la fenêtre d'accueil

    bdd_page = Frame(root, bg=(bgc))

    bdd = dict(lire_equipement())
    print(type(bdd))
    print(bdd)

    table = ttk.Treeview(root, columns = ('ID', 'type', 'marque', 'modele', 'num_serie', 'emplacement', 'responsable', 'date_achat'), show= 'headings')
    table.heading('ID', text='ID')
    table.heading('type', text='type')
    table.heading('marque', text='marque')
    table.heading('modele', text='modèle')
    table.heading('num_serie', text='numéro de série')
    table.heading('emplacement', text='emplacement')
    table.heading('responsable', text='responsable')
    table.heading('date_achat', text='date d achat')

    table.column('ID', width=50)
    table.column('type', width=150)
    table.column('marque', width=150)
    table.column('modele', width=150)
    table.column('num_serie', width=150)
    table.column('emplacement', width=150)
    table.column('responsable', width=150)
    table.column('date_achat', width=150)

    table.pack(expand=YES, padx=20)

    bdd_page.pack(expand=YES)

