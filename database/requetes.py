from connexion import connexion

def ajouter_equipement(typE, marque, modele, num_serie, emplacement, responsable, date_achat):
    insert = (
        "INSERT INTO equipements (type, marque, modele, num_serie, emplacement, responsable, date_achat) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    )
    data = (typE, marque, modele, num_serie, emplacement, responsable, date_achat)
    cursor = connexion.cursor()
    cursor.execute(insert, data)
    connexion.commit()