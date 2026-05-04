from connexion import connexion

insert = (
    "INSERT INTO equipements (type, marque, modele, num_serie, emplacement, responsable, date_achat)"
    "VALUES (%s, %s, %s, %s, %s, %s, %s)"
)
data = ()
cursor.execute(insert, data)