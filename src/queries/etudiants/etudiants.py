import psycopg2
from ...database.database import connect_to_database


class EtudiantQueryHandler:
    def __init__(self):
        self.conn = connect_to_database()
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def create_etudiants_table(self):
        try:
            # SQL pour créer la table des étudiants
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS etudiants (
                id SERIAL PRIMARY KEY,
                nom VARCHAR(255) NOT NULL,
                prenom VARCHAR(255) NOT NULL,
                age INT
            );
            """

            # Exécution de la requête SQL pour créer la table
            self.cursor.execute(create_table_sql)

            # Validation de la transaction
            self.conn.commit()
            print("Table 'etudiants' créée avec succès.")

        except (Exception, psycopg2.DatabaseError) as error:
            # Gestion des erreurs
            print("Erreur lors de la création de la table 'etudiants' :", error)

    def get_etudiants(self):
        try:
            # SQL pour sélectionner tous les étudiants
            select_all_sql = "SELECT * FROM etudiants"

            # Exécution de la requête SQL pour sélectionner tous les étudiants
            self.cursor.execute(select_all_sql)

            # Affichage des données
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)

        except (Exception, psycopg2.DatabaseError) as error:
            # Gestion des erreurs
            print("Erreur lors de la sélection des données :", error)

    def insert_etudiant(self, nom, prenom, age):
        try:
            # SQL pour ajouter un nouvel etudiant
            insert_sql = "INSERT INTO etudiants (nom, prenom, age) VALUES (%s, %s, %s)"

            # Exécution de la requête SQL pour ajouter un nouvel etudiant
            self.cursor.execute(insert_sql, (nom, prenom, age))

            # Validation de la transaction
            self.conn.commit()
            print("Nouvel etudiant ajouté avec succès.")

        except (Exception, psycopg2.DatabaseError) as error:
            # Gestion des erreurs
            print("Erreur lors de l'ajout du nouvel etudiant :", error)

    def __exit__(self, exc_type, exc_value, traceback):
        # Fermer le curseur et la connexion à la base de données
        self.cursor.close()
        self.conn.close()


etudiant_query_handler = EtudiantQueryHandler()
# etudiant_query_handler.create_etudiants_table()
# etudiant_query_handler.insert_etudiant("Doe", "John", 25)
etudiant_query_handler.get_etudiants()
