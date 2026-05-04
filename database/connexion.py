import mysql.connector as cpy #importation de la librairie mysql.connector.python on lui donne le nom de cpy pour simplifier le code

def connexion():
    try:
        cnx = cpy.connect( #on créer la connexion avec toute les informations nécessaires afin de se connecter à la db
            user='root',
            password='root',
            database='gestiondeparcinformatique',
            host='127.0.0.1',
            port='3306'
            )
        print('Connexion réussie')
        return cnx
    except cpy.Error as err:
        print("Connexion échouée: {}".format(err))
        return None