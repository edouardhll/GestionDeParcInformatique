import tkinter as tk
from tkinter import *
from tkinter import ttk
from views.fonction_view import github
from database.requetes import ajouter_equipement, lire_equipement, delete_equipement, maj_equipement
from datetime import datetime
from tkinter import messagebox





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
    root.minsize(1280, 720) #donne une taille minimal à la fenêtre ne pouvant pas être réduite
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



#----------Fonction de la fenêtre de lecture----------#
def entry(home, root):
    home.pack_forget() #on ferme la fenêtre d'accueil

    bdd_page = Frame(root, bg=(bgc))

    bdd = lire_equipement()

    #----------Création du tableau----------#
    #on nomme les valeurs que l'ont va traiter
    table = ttk.Treeview(bdd_page, columns = ('ID', 'type', 'marque', 'modele', 'num_serie', 'emplacement', 'responsable', 'date_achat'), show= 'headings')

    #on rajoute le texte qui s'affiche pour chaque colonne
    table.heading('ID', text='ID')
    table.heading('type', text='type')
    table.heading('marque', text='marque')
    table.heading('modele', text='modèle')
    table.heading('num_serie', text='numéro de série')
    table.heading('emplacement', text='emplacement')
    table.heading('responsable', text='responsable')
    table.heading('date_achat', text='date d achat')

    #attribution de la largeur des colonnes
    table.column('ID', width=50)
    table.column('type', width=150)
    table.column('marque', width=150)
    table.column('modele', width=150)
    table.column('num_serie', width=150)
    table.column('emplacement', width=150)
    table.column('responsable', width=150)
    table.column('date_achat', width=150)

    #pour chaque ligne on vient l'ajouter au tableau
    for i in bdd:
        table.insert(parent='', index = END, values = i)# parent vide = ligne racine, on ne veut pas de branches ici ; end précise qu'on ajoute la ligne à la fin de notre tableau
    table.pack(expand=YES, padx=20)

    #----------Création d'un cadre pour les boutons----------#
    button_frame = Frame(bdd_page, bg=(bgc))
    button_frame.pack(side=BOTTOM)

    #----------Création du bouton AJOUTER----------#
    add_button = Button(button_frame, text="Ajouter un nouvel équipement", font=(h2p, 15), bg=bgc, fg=h2c, activebackground=bgc, command=lambda: add_tk(bdd_page, root, home,))#appelle la fonction pour la nouvelle fenêtre, on importe home et root pour pouvoir les reconnaitre
    add_button.pack(side = LEFT, pady=25, padx=25)
    #----------Création du bouton MODIFIER----------#
    edit_button = Button(button_frame, text="Modifier un équipement", font=(h2p, 15), bg=bgc, fg=h2c, activebackground=bgc, command=lambda: edit_tk(bdd_page, root, home, table))#appelle la fonction pour la nouvelle fenêtre, on importe home et root pour pouvoir les reconnaitre
    edit_button.pack(side=LEFT, pady=25, padx=25)
    #----------Création du bouton EFFACER----------#
    delete_button = Button(button_frame, text="Supprimer un équipement", font=(h2p, 15), bg=bgc, fg=h2c, activebackground=bgc, command=lambda: delete_tk(home))#appelle la fonction pour la nouvelle fenêtre, on importe home et root pour pouvoir les reconnaitre
    delete_button.pack(side = RIGHT, pady=25, padx=25)
    #----------Création de la fonction pour EFFACER----------#
    def delete_tk(home):
        try:
            ligne = table.selection()
            value = table.item(ligne, 'values')
            id = value[0]
            delete_equipement(id)
            bdd_page.pack_forget()
            entry(home, root)
        except Exception as err:
            messagebox.showerror("Error", str(err))

    #on a fini on pack le tout
    bdd_page.pack(expand=YES)

#----------Fonction de la fenêtre pour AJOUTER----------#

def add_tk(bdd_page, root, home):

    bdd_page.pack_forget() #on ferme la fenêtre précédente

    #----------Création du cadre principal----------#
    frame = Frame(root, bg=(bgc))

    #----------Création du cadre bottom----------#
    bottom = Frame(frame, bg = (bgc))
    bottom.pack(side=BOTTOM)
    #----------Création du cadre left----------#
    left = Frame(frame, bg = (bgc))
    left.pack(side=LEFT)
    #----------Création du cadre right----------#
    right = Frame(frame, bg = (bgc))
    right.pack(side=RIGHT)


    #Tous les noms à gauche
    label_title = Label(left, text='Matériel :', font=(h2p, 15), bg=bgc, fg=h2c)
    label_title.pack(pady=5, padx=5,)

    label_title = Label(left, text='Marque :', font=(h2p, 15), bg=bgc, fg=h2c)
    label_title.pack(pady=5, padx=5)

    label_title = Label(left, text='Modèle :', font=(h2p, 15), bg=bgc, fg=h2c)
    label_title.pack(pady=5, padx=5)

    label_title = Label(left, text='Numéro de série :', font=(h2p, 15), bg=bgc, fg=h2c)
    label_title.pack(pady=5, padx=5)

    label_title = Label(left, text='Emplacement :', font=(h2p, 15), bg=bgc, fg=h2c)
    label_title.pack(pady=5, padx=5)

    label_title = Label(left, text='Responsable :', font=(h2p, 15), bg=bgc, fg=h2c)
    label_title.pack(pady=5, padx=5)

    label_title = Label(left, text='Date achat :', font=(h2p, 15), bg=bgc, fg=h2c)
    label_title.pack(pady=5, padx=5)


    #Tous les inputs à droite
    input_type = Entry(right, font=(h2p, 15), bg=bgc, fg=h2c, width=20)
    input_type.pack(pady=5, padx=5)

    input_marque = Entry(right, font=(h2p, 15), bg=bgc, fg=h2c, width=20)
    input_marque.pack(pady=5, padx=5)

    input_modele = Entry(right, font=(h2p, 15), bg=bgc, fg=h2c, width=20)
    input_modele.pack(pady=5, padx=5)

    input_num_serie = Entry(right, font=(h2p, 15), bg=bgc, fg=h2c, width=20)
    input_num_serie.pack(pady=5, padx=5)

    input_emplacement = Entry(right, font=(h2p, 15), bg=bgc, fg=h2c, width=20)
    input_emplacement.pack(pady=5, padx=5)

    input_responsable = Entry(right, font=(h2p, 15), bg=bgc, fg=h2c, width=20)
    input_responsable.pack(pady=5, padx=5)

    input_date_achat = Entry(right, font=(h2p, 15), bg=bgc, fg=h2c, width=20)
    input_date_achat.pack(pady=5, padx=5)

    def input_data():

        try:
            data = input_type.get(), input_marque.get(), input_modele.get(), input_num_serie.get(), input_emplacement.get(), input_responsable.get(), datetime.strptime(input_date_achat.get(), "%d/%m/%Y")
            ajouter_equipement(*data) #ajouter_equipement() attend 7 entrées, mettre une étoile permet de lui renvoyer la liste en séparant les éléments qui la contiennent.
            frame.pack_forget()
            entry(home, root)
        except Exception as err:
            messagebox.showerror("Error", str(err))


    validation_button = Button(bottom, text="Valider le nouvel équipement", font=(h2p, 15), bg=bgc, fg=h2c, activebackground=bgc, command=input_data)
    validation_button.pack(side=BOTTOM, pady=25, padx=25)

    frame.pack(expand=YES)




#----------Fonction de la fenêtre pour MODIFIER----------#



def edit_tk(bdd_page, root, home, table):

    bdd_page.pack_forget() #on ferme la fenêtre précédente

    ligne = table.selection()
    value = table.item(ligne, 'values')
    id = value[0]





    #----------Création du cadre principal----------#
    frame = Frame(root, bg=(bgc))

    #----------Création du cadre bottom----------#
    bottom = Frame(frame, bg = (bgc))
    bottom.pack(side=BOTTOM)
    #----------Création du cadre left----------#
    left = Frame(frame, bg = (bgc))
    left.pack(side=LEFT)
    #----------Création du cadre right----------#
    right = Frame(frame, bg = (bgc))
    right.pack(side=RIGHT)


    #Tous les noms à gauche
    label_title = Label(left, text='Matériel :', font=(h2p, 15), bg=bgc, fg=h2c)
    label_title.pack(pady=5, padx=5,)

    label_title = Label(left, text='Marque :', font=(h2p, 15), bg=bgc, fg=h2c)
    label_title.pack(pady=5, padx=5)

    label_title = Label(left, text='Modèle :', font=(h2p, 15), bg=bgc, fg=h2c)
    label_title.pack(pady=5, padx=5)

    label_title = Label(left, text='Numéro de série :', font=(h2p, 15), bg=bgc, fg=h2c)
    label_title.pack(pady=5, padx=5)

    label_title = Label(left, text='Emplacement :', font=(h2p, 15), bg=bgc, fg=h2c)
    label_title.pack(pady=5, padx=5)

    label_title = Label(left, text='Responsable :', font=(h2p, 15), bg=bgc, fg=h2c)
    label_title.pack(pady=5, padx=5)

    label_title = Label(left, text='Date achat :', font=(h2p, 15), bg=bgc, fg=h2c)
    label_title.pack(pady=5, padx=5)


    #Tous les inputs à droite
    input_type = Entry(right, font=(h2p, 15), bg=bgc, fg=h2c, width=20)
    input_type.insert(0, value[1])
    input_type.pack(pady=5, padx=5)

    input_marque = Entry(right, font=(h2p, 15), bg=bgc, fg=h2c, width=20)
    input_marque.insert(0, value[2])
    input_marque.pack(pady=5, padx=5)

    input_modele = Entry(right, font=(h2p, 15), bg=bgc, fg=h2c, width=20)
    input_modele.insert(0, value[3])
    input_modele.pack(pady=5, padx=5)

    input_num_serie = Entry(right, font=(h2p, 15), bg=bgc, fg=h2c, width=20)
    input_num_serie.insert(0, value[4])
    input_num_serie.pack(pady=5, padx=5)

    input_emplacement = Entry(right, font=(h2p, 15), bg=bgc, fg=h2c, width=20)
    input_emplacement.insert(0, value[5])
    input_emplacement.pack(pady=5, padx=5)

    input_responsable = Entry(right, font=(h2p, 15), bg=bgc, fg=h2c, width=20)
    input_responsable.insert(0, value[6])
    input_responsable.pack(pady=5, padx=5)

    input_date_achat = Entry(right, font=(h2p, 15), bg=bgc, fg=h2c, width=20)
    input_date_achat.insert(0, value[7])
    input_date_achat.pack(pady=5, padx=5)

    def input_data():

        try:
            data = input_type.get(), input_marque.get(), input_modele.get(), input_num_serie.get(), input_emplacement.get(), input_responsable.get(), datetime.strptime(input_date_achat.get(), "%d/%m/%Y")
            maj_equipement(id, *data) #ajouter_equipement() attend 7 entrées, mettre une étoile permet de lui renvoyer la liste en séparant les éléments qui la contiennent.
            frame.pack_forget()
            entry(home, root)
        except Exception as err:
            messagebox.showerror("Error", str(err))

    validation_button = Button(bottom, text="Valider Les modifications", font=(h2p, 15), bg=bgc, fg=h2c, activebackground=bgc, command=input_data)
    validation_button.pack(side=BOTTOM, pady=25, padx=25)

    frame.pack(expand=YES)