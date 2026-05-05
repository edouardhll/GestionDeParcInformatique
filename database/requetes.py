from connexion import connexion
from datetime import date

cnx = None

def ajouter_equipement(typE, marque, modele, num_serie, emplacement, responsable, date_achat):
    insert = (
        "INSERT INTO equipements (type, marque, modele, num_serie, emplacement, responsable, date_achat) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    )
    data = (typE, marque, modele, num_serie, emplacement, responsable, date_achat)
#    cnx = connexion()
    cursor = cnx.cursor()
    cursor.execute(insert, data)
    cnx.commit()

def lire_equipement():
    #créer un curseur
    read = (
        "SELECT * FROM equipements"
    )
    cursor = cnx.cursor()
    cursor.execute(read)
    #cursor.commit()
    return cursor

def maj_equipement():
    pass

def delete_equipement():
    pass



cnx = connexion()

ajouter_equipement('clavier', 'auchan', 'clavier20', 1235  , 'ici', 'moa', date(2026, 6, 1))

cursor =  lire_equipement()
for line in cursor:
        print(line)
