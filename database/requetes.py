from database.connexion import connexion
from datetime import date
import mysql.connector as cpy
from mysql.connector.errors import Error
from tkinter import messagebox
cnx = None
str(Error())


def ajouter_equipement(typE, marque, modele, num_serie, emplacement, responsable, date_achat):

    try:
        insert = (
            "INSERT INTO equipements (type, marque, modele, num_serie, emplacement, responsable, date_achat) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )
        data = (typE, marque, modele, num_serie, emplacement, responsable, date_achat)
        cursor = cnx.cursor()
        cursor.execute(insert, data)
        cnx.commit()

    except cpy.Error as err:
            messagebox.showerror("Error", str(err))


def lire_equipement():

    try:
        read = (
            "SELECT * FROM equipements"
        )
        cursor = cnx.cursor()
        cursor.execute(read)
        # for line in cursor:
        #         print(line)    
        return cursor.fetchall() #routourne sous forme de tuple plutôt que sous forme de curseur
    
    except cpy.Error as err:
            print("La lecture a échoué: {}".format(err))


def maj_equipement(id_equipement, typE, marque, modele, num_serie, emplacement, responsable, date_achat):

    try:
        update = (
            "UPDATE equipements SET type = %s, marque = %s, modele = %s, num_serie = %s, emplacement = %s, responsable = %s, date_achat = %s WHERE id = %s"
        )
        data = (typE, marque, modele, num_serie, emplacement, responsable, date_achat, id_equipement)
        cursor = cnx.cursor()
        cursor.execute(update, data)
        cnx.commit()

    except cpy.Error as err:
        print("La mise à jour a échoué: {}".format(err))

def delete_equipement(id_equipement):

    try:
        delete = (
            "DELETE FROM equipements WHERE id = %s"
        )
        data = (id_equipement,)
        cursor = cnx.cursor()
        cursor.execute(delete, data)
        cnx.commit()

    except cpy.Error as err:
            print("La suppression a échoué: {}".format(err))

def error_name(err):
    if err.errno == 1062:
        message = "Ce numéro de série existe déjà."
    elif err.errno == 1048:
        message = "Merci de remplir tous les champs."
    elif err.errno == 2003:
        message = "Impossible de se connecter au serveur."
    elif err.errno == 1452:
        message = "Erreur avec la clé étrangère."
    else:
        message = ("La mise à jour a échoué: {}".format(err))
    return message

cnx = connexion()

#ajouter_equipement('clavier', 'auchan', 'clavier20', 1235  , 'ici', 'moa', date(2026, 6, 1))
#maj_equipement(2, 'clavier', 'auchan', 'clavier20', '1235', 'ici', 'toa', date(2026, 6, 1))
#delete_equipement(3)
#cursor =  lire_equipement()
#print(str(Error(errno=2006)))
