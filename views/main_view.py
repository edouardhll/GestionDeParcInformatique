import tkinter
from tkinter import *
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


    #----------Création du cadre----------#
    frame= Frame(root, bg=bgc, bd=1, relief=SUNKEN)
    frame.pack(expand=YES)


    #----------Définition du titre----------#
    label_title = Label(frame, text='Gestionnaire de parc informatique', font=(h1p, 30), bg=bgc, fg=h1c)
    label_title.pack(expand=YES)


    #----------Définition du texte----------#
    # label_texte = Label(frame, text="titi toto tata", font=(h2p, 20), bg=bgc, fg = h2c)
    # label_texte.pack(side=BOTTOM)


    #----------Création du bouton github----------#
    boutongithub = Button(frame, text="Consulter mon github", font=(h2p, 15), bg=bgc, fg=h2c, command=github)
    boutongithub.pack(fill=X, pady=25,)

    #----------Création du bouton lire----------#
    lire = Button(frame, text="Lire la bdd", font=(h2p, 15), bg=bgc, fg=h2c, command=lire_equipement)
    lire.pack(fill=X, pady=25,)

    #----------Exécution de la fenêtre----------#
    root.mainloop() #afficher la fenêtre