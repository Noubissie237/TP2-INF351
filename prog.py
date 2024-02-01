import os, mysql.connector
import matplotlib.pyplot as plt

def getNumber(message : str, min : int, max : int) -> int :
    
    try:
        number = int(input(message))
        if number < min or number > max:
            return getNumber(f"\nErreur, veuillez entrer une valeur comprise entre {min} et {max} selon ce que vous souhaitez faire : ", min, max)
        else:
            return number
    except:
        return getNumber("\nErreur : Veuillez entrer un entier : ", min, max)

T_pays = []
abscisse = []
ordonnee = [-1]

#Connexion a la bd 
connexion = mysql.connector.connect(user="root", password="", host="localhost", database="Entrepot")

# Creation du curseur
cursor = connexion.cursor(buffered=True)

# Definition des requetes
def requete1() -> None:
    print("!"*100)
    #Connexion a la bd 
    connexion = mysql.connector.connect(user="root", password="", host="localhost", database="Entrepot")
    # Creation du curseur
    cursor = connexion.cursor(buffered=True)

    # Requête SQL pour afficher le nombre de publications par institution
    query = """
    SELECT Institution.nom AS institution, COUNT(*) AS nombre_publications
    FROM Affiliation
    JOIN Institution ON Affiliation.etablissement = Institution.idInstitution
    JOIN AuteurFiliation ON Affiliation.idAfiliation = AuteurFiliation.idAfiliation
    JOIN AuteurArticle ON AuteurFiliation.idAuteur = AuteurArticle.idAuteur
    GROUP BY Institution.nom;
    """

    # Exécuter la requête
    cursor.execute(query)

    # Récupérer tous les résultats
    results = cursor.fetchall()

    # Vérifier si des résultats ont été retournés
    if results:
        print("Nombre de publications par institution :")
        for result in results:
            institution, nombre_publications = result
            print(f"{institution}: {nombre_publications} publications")
    else:
        print("Aucun résultat trouvé.")
    print("!"*100)
    cursor.close()

def requete2() -> None:
    print("!"*100)
    #Connexion a la bd 
    connexion = mysql.connector.connect(user="root", password="", host="localhost", database="Entrepot")
    # Creation du curseur
    cursor = connexion.cursor(buffered=True)

    # Requête SQL pour afficher le nombre de publications par auteur
    query = """
    SELECT Auteur.nom AS auteur, COUNT(*) AS nombre_publications
    FROM Auteur
    JOIN AuteurFiliation ON Auteur.idAuteur = AuteurFiliation.idAuteur
    JOIN AuteurArticle ON AuteurFiliation.idAuteur = AuteurArticle.idAuteur
    GROUP BY Auteur.nom;
    """

    # Exécuter la requête
    cursor.execute(query)

    # Récupérer tous les résultats
    results = cursor.fetchall()

    # Vérifier si des résultats ont été retournés
    if results:
        print("Nombre de publications par auteur :")
        for result in results:
            auteur, nombre_publications = result
            print(f"{auteur}: {nombre_publications} publications")
    else:
        print("Aucun résultat trouvé.")
    print("!"*100)
    cursor.close()

def requete3() -> None:
    print("!"*100)
    #Connexion a la bd 
    connexion = mysql.connector.connect(user="root", password="", host="localhost", database="Entrepot")
    # Creation du curseur
    cursor = connexion.cursor(buffered=True)

    # Requête SQL pour afficher le nombre d'auteurs par affiliation
    query = """
    SELECT Institution.nom AS etablissement, Pays.nom AS pays, COUNT(AuteurFiliation.idAuteur) AS nombre_auteurs
    FROM AuteurFiliation
    JOIN Affiliation ON AuteurFiliation.idAfiliation = Affiliation.idAfiliation
    JOIN Institution ON Affiliation.etablissement = Institution.idInstitution
    JOIN Pays ON Affiliation.pays = Pays.idPays
    GROUP BY Institution.nom, Pays.nom;
    """

    # Exécuter la requête
    cursor.execute(query)

    # Récupérer tous les résultats
    results = cursor.fetchall()

    # Vérifier si des résultats ont été retournés
    if results:
        print("Nombre d'auteurs par affiliation :")
        for result in results:
            etablissement, pays, nombre_auteurs = result
            print(f"Établissement : {etablissement} | Pays : {pays} | Nombre d'auteurs : {nombre_auteurs}")
    else:
        print("Aucun résultat trouvé.")
    print("!"*100)
    cursor.close()

def requete4() -> None:
    print("!"*100)
    #Connexion a la bd 
    connexion = mysql.connector.connect(user="root", password="", host="localhost", database="Entrepot")
    # Creation du curseur
    cursor = connexion.cursor(buffered=True)

    # Requête SQL pour afficher l'auteur ayant publié le plus grand nombre d'articles aux États-Unis
    query = """
    SELECT Auteur.nom AS auteur, COUNT(AuteurArticle.idArticle) AS nombre_articles
    FROM Auteur
    JOIN AuteurFiliation ON Auteur.idAuteur = AuteurFiliation.idAuteur
    JOIN Affiliation ON AuteurFiliation.idAfiliation = Affiliation.idAfiliation
    JOIN Pays ON Affiliation.pays = Pays.idPays
    JOIN AuteurArticle ON Auteur.idAuteur = AuteurArticle.idAuteur
    WHERE Pays.nom = ' USA'
    GROUP BY Auteur.idAuteur
    ORDER BY nombre_articles DESC
    LIMIT 1;
    """

    # Exécuter la requête
    cursor.execute(query)

    # Récupérer le premier résultat
    result = cursor.fetchone()

    # Vérifier si un résultat a été retourné
    if result:
        auteur, nombre_articles = result
        print(f"L'auteur ayant publié le plus grand nombre d'articles aux États-Unis est {auteur} avec {nombre_articles} articles.")
    else:
        print("Aucun résultat trouvé.")
    print("!"*100)
    cursor.close()

def requete5() -> None:
    print("!"*100)
    #Connexion a la bd 
    connexion = mysql.connector.connect(user="root", password="", host="localhost", database="Entrepot")
    # Creation du curseur
    cursor = connexion.cursor(buffered=True)

    # Requête SQL pour afficher l'établissement ayant le plus d'articles publiés
    query = """
    SELECT Institution.nom AS etablissement, COUNT(AuteurArticle.idArticle) AS nombre_articles
    FROM Institution
    JOIN Affiliation ON Institution.idInstitution = Affiliation.etablissement
    JOIN AuteurFiliation ON Affiliation.idAfiliation = AuteurFiliation.idAfiliation
    JOIN AuteurArticle ON AuteurFiliation.idAuteur = AuteurArticle.idAuteur
    GROUP BY Institution.idInstitution
    ORDER BY nombre_articles DESC
    LIMIT 1;
    """

    # Exécuter la requête
    cursor.execute(query)

    # Récupérer le premier résultat
    result = cursor.fetchone()

    # Vérifier si un résultat a été retourné
    if result:
        etablissement, nombre_articles = result
        print(f"L'établissement ayant le plus d'articles publiés est {etablissement} avec {nombre_articles} articles.")
    else:
        print("Aucun résultat trouvé.")
    print("!"*100)
    cursor.close()

def requete6() -> None:
    print("!"*100)
    # Requête SQL pour afficher le nombre d'articles publiés par année
    #Connexion a la bd 
    connexion = mysql.connector.connect(user="root", password="", host="localhost", database="Entrepot")
    # Creation du curseur
    cursor = connexion.cursor(buffered=True)

    query = """
    SELECT annee, COUNT(idArticle) AS nombre_articles
    FROM Article
    GROUP BY annee
    ORDER BY annee;
    """

    # Exécuter la requête
    cursor.execute(query)

    # Récupérer tous les résultats
    results = cursor.fetchall()

    # Vérifier si des résultats ont été retournés
    if results:
        print("Nombre d'articles publiés par année :")
        for result in results:
            annee, nombre_articles = result
            print(f"Année {annee}: {nombre_articles} articles")
    else:
        print("Aucun résultat trouvé.")
    print("!"*100)
    cursor.close()

def requete7() -> None:
    print("!"*100)

    #Connexion a la bd 
    connexion = mysql.connector.connect(user="root", password="", host="localhost", database="Entrepot")
    # Creation du curseur
    cursor = connexion.cursor(buffered=True)

    # Requête SQL pour trouver l'article avec le plus grand nombre d'auteurs
    query = """
    SELECT Article.titre AS titre_article, COUNT(Auteur.idAuteur) AS nombre_auteurs
    FROM Article
    JOIN AuteurArticle ON Article.idArticle = AuteurArticle.idArticle
    JOIN Auteur ON AuteurArticle.idAuteur = Auteur.idAuteur
    GROUP BY Article.idArticle
    ORDER BY nombre_auteurs DESC
    LIMIT 1;
    """

    # Exécuter la requête
    cursor.execute(query)

    # Récupérer le résultat
    result = cursor.fetchone()

    # Vérifier si un résultat a été retourné
    if result is not None:
        titre_article, nombre_auteurs = result
        print(f"L'article avec le plus grand nombre d'auteurs est '{titre_article}' avec {nombre_auteurs} auteurs.")
    else:
        print("Aucun article trouvé.")
    print("!"*100)
    cursor.close()

def requete8() -> None:
    print("!"*100)
    #Connexion a la bd 
    connexion = mysql.connector.connect(user="root", password="", host="localhost", database="Entrepot")
    # Creation du curseur
    cursor = connexion.cursor(buffered=True)

    # Requête SQL pour afficher l'auteur, son établissement, son pays ayant publié le plus grand nombre d'articles
    query = """
    SELECT Auteur.nom AS auteur, Institution.nom AS etablissement, Pays.nom AS pays, COUNT(AuteurArticle.idArticle) AS nombre_articles
    FROM Auteur
    JOIN AuteurFiliation ON Auteur.idAuteur = AuteurFiliation.idAuteur
    JOIN Affiliation ON AuteurFiliation.idAfiliation = Affiliation.idAfiliation
    JOIN Institution ON Affiliation.etablissement = Institution.idInstitution
    JOIN Pays ON Affiliation.pays = Pays.idPays
    JOIN AuteurArticle ON Auteur.idAuteur = AuteurArticle.idAuteur
    GROUP BY Auteur.idAuteur, Institution.idInstitution, Pays.idPays
    ORDER BY nombre_articles DESC
    LIMIT 1;
    """

    # Exécuter la requête
    cursor.execute(query)

    # Récupérer le premier résultat
    result = cursor.fetchone()

    # Vérifier si un résultat a été retourné
    if result:
        auteur, etablissement , pays, nombre_articles = result
        print("Auteur ayant publié le plus grand nombre d'articles :")
        print(f"Auteur : {auteur}")
        print(f"Établissement : {etablissement}")
        print(f"Pays : {pays}")
        print(f"Nombre d'articles publiés : {nombre_articles}")
    else:
        print("Aucun résultat trouvé.")
    print("!"*100)
    cursor.close()


#   ----------- Supprimons D'abord les tables afin d'eviter les potentielles erreurs ----------- #
breakForeignKey = "SET FOREIGN_KEY_CHECKS = 0"
AuteurCheck = "SELECT * FROM Auteur"
ArticleCheck = "SELECT * FROM Article"
AffiliationCheck = "SELECT * FROM Affiliation"
AuteurFiliationCheck = "SELECT * FROM AuteurFiliation"
AuteurArticleCheck = "SELECT * FROM AuteurArticle"

try:
    cursor.execute(breakForeignKey)
    cursor.execute(AuteurCheck)
    cursor.execute(ArticleCheck)
    cursor.execute(AffiliationCheck)
    cursor.execute(AuteurFiliationCheck)
    cursor.execute(AuteurArticleCheck)
    connexion.commit()

except:
#   ----------- Creation des tables ----------- #
    
    print("Chargement de l'entrepot ...\n")
    create_pays_table = """
    CREATE TABLE Pays(
    idPays INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nom VARCHAR(100)
    );
    """
    create_auteur_table = """
    CREATE TABLE Auteur(
    idAuteur INT PRIMARY KEY AUTO_INCREMENT, 
    nom VARCHAR(50)
    )
    """
    create_article_table = """
    CREATE TABLE Article (
    idArticle INT PRIMARY KEY AUTO_INCREMENT,
    titre VARCHAR(250),
    annee INTEGER
    )
    """
    create_institution_table = """
    CREATE TABLE Institution(
    idInstitution INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(250)
    );
    """

    create_affiliation_table = """
    CREATE TABLE Affiliation(
    idAfiliation INT PRIMARY KEY AUTO_INCREMENT,
    etablissement INTEGER,
    pays INTEGER,
    FOREIGN KEY (etablissement) REFERENCES Institution(idInstitution),
    FOREIGN KEY (pays) REFERENCES Pays(idPays)
    )
    """

    create_auteurFiliation_table = """
    CREATE TABLE AuteurFiliation(
    idAuteur INT,
    idAfiliation INT,
    FOREIGN KEY (idAuteur) REFERENCES Auteur(idAuteur),
    FOREIGN KEY (idAfiliation) REFERENCES Affiliation(idAfiliation),
    PRIMARY KEY(idAuteur, idAfiliation)
    )
    """

    create_auteurArticle_table = """
    CREATE TABLE AuteurArticle(
    idAuteur INT,
    idArticle INT,
    FOREIGN KEY (idAuteur) REFERENCES Auteur(idAuteur),
    FOREIGN KEY (idArticle) REFERENCES Article(idArticle),
    PRIMARY KEY(idAuteur, idArticle)
    )
    """

    cursor.execute(create_pays_table)
    cursor.execute(create_auteur_table)
    cursor.execute(create_article_table)
    cursor.execute(create_institution_table)
    cursor.execute(create_affiliation_table)
    cursor.execute(create_auteurFiliation_table)
    cursor.execute(create_auteurArticle_table)
    connexion.commit()


#   ----------- Alimentation de l'entrepot ----------- #
    alimentation_institutions = """
    INSERT INTO Entrepot.Institution (nom)
    SELECT DISTINCT etablissement
    FROM TPINF351.Affiliation
    WHERE 1;
    """

    alimentation_pays = """
    INSERT INTO Entrepot.Pays (nom)
    SELECT DISTINCT pays
    FROM TPINF351.Affiliation
    WHERE 1;
    """

    alimentation_article = """
    INSERT INTO Entrepot.Article (titre, annee)
    SELECT titre_article, annee
    FROM TPINF351.Article
    WHERE 1;
    """

    alimentation_auteur = """
    INSERT INTO Entrepot.Auteur (nom)
    SELECT nom_encode
    FROM TPINF351.Auteur
    WHERE 1;
    """

    alimentation_auteur_article = """
    INSERT INTO Entrepot.AuteurArticle (idAuteur, idArticle)
    SELECT DISTINCT idAuteur, idArticle
    FROM TPINF351.AuteurArticle
    WHERE 1;
    """

    alimentation_affiliation = """
    INSERT INTO Entrepot.Affiliation (etablissement, pays)
    SELECT Entrepot.Institution.idInstitution, Entrepot.Pays.idPays
    FROM TPINF351.Affiliation
    INNER JOIN Entrepot.Institution ON Entrepot.Institution.nom = TPINF351.Affiliation.etablissement
    INNER JOIN Entrepot.Pays ON Entrepot.Pays.nom = TPINF351.Affiliation.pays;
    """

    alimentation_auteur_filiation = """
    INSERT INTO Entrepot.AuteurFiliation (idAuteur, idAfiliation)
    SELECT DISTINCT Auteur.idAuteur, Affiliation.idAfiliation
    FROM TPINF351.AuteurFiliation
    INNER JOIN TPINF351.Auteur ON TPINF351.AuteurFiliation.idAuteur = TPINF351.Auteur.idAuteur
    INNER JOIN TPINF351.Affiliation ON TPINF351.AuteurFiliation.idAfiliation = TPINF351.Affiliation.idAfiliation;
    """

    cursor.execute(alimentation_institutions)
    cursor.execute(alimentation_pays)
    cursor.execute(alimentation_article)
    cursor.execute(alimentation_auteur)
    cursor.execute(alimentation_auteur_article)
    cursor.execute(alimentation_affiliation)
    cursor.execute(alimentation_auteur_filiation)
    
    connexion.commit()

    #Fermeture du cursor et de la connexion à la bd
    cursor.close()
    connexion.close()

    print("Chargement effectué avec success !\n")

finally:

    choix = -1
    while choix != 0 :
        print("\n\nQue souhaitez vous afficher ?\n")
        print("\t0. Sortir du programme")
        print("\t1. Nombre de publication par institution")
        print("\t2. Nombre de publication par auteur")
        print("\t3. Nombre d'auteur par affiliation")
        print("\t4. L'auteur ayant publié le plus grand nombre d'article au USA")
        print("\t5. Etablissement ayant le plus d'article publié")
        print("\t6. Le nombre d'article publié par année")
        print("\t7. L'article ayant la plus grande collaboration d'acteurs")
        print("\t8. L'auteur, son établissement, sa ville son pays, ayant publié le plus grand nombre d'article, ainsi que son nombre d'article publié")
        
        choix = getNumber("\nChoix : ", 0, 8)

        if choix == 1:
            requete1()
        if choix == 2:
            requete2()
        if choix == 3:
            requete3()
        if choix == 4:
            requete4()
        if choix == 5:
            requete5()
        if choix == 6:
            requete6()
        if choix == 7:
            requete7()
        if choix == 8:
            requete8()
        if choix == 0:
            print("\n\nFin du programme ...")

