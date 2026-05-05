from connexion import connexion
from datetime import date

cnx = None

def ajouter_equipement(typE, marque, modele, num_serie, emplacement, responsable, date_achat):
    insert = (
        "INSERT INTO equipements (type, marque, modele, num_serie, emplacement, responsable, date_achat) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    )
    data = (typE, marque, modele, num_serie, emplacement, responsable, date_achat)
    cursor = cnx.cursor()
    cursor.execute(insert, data)
    cnx.commit()

def lire_equipement():
    read = (
        "SELECT * FROM equipements"
    )
    cursor = cnx.cursor()
    cursor.execute(read)
    return cursor

def maj_equipement(id_equipement, typE, marque, modele, num_serie, emplacement, responsable, date_achat):
    update = (
         "UPDATE equipements SET type = %s, marque = %s, modele = %s, num_serie = %s, emplacement = %s, responsable = %s, date_achat = %s WHERE id = %s"
    )
    data = (typE, marque, modele, num_serie, emplacement, responsable, date_achat, id_equipement)
    cursor = cnx.cursor()
    cursor.execute(update, data)
    cnx.commit()

def delete_equipement(id_equipement):
    delete = (
         "DELETE FROM equipements WHERE id = %s"
    )
    data = (id_equipement,)
    cursor = cnx.cursor()
    cursor.execute(delete, data)
    cnx.commit()

cnx = connexion()

#ajouter_equipement('clavier', 'auchan', 'clavier20', 1235  , 'ici', 'moa', date(2026, 6, 1))
#maj_equipement(2, 'clavier', 'auchan', 'clavier20', '1235', 'ici', 'toa', date(2026, 6, 1))
#delete_equipement(3)

cursor =  lire_equipement()
for line in cursor:
        print(line)