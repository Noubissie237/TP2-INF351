-- CHARGEMENT DES INSTITUTIONS
INSERT INTO Entrepot.Institution (nom)
SELECT DISTINCT etablissement
FROM TPINF351.Affiliation
WHERE 1;

-- CHARGEMENT DES PAYS
INSERT INTO Entrepot.Pays (nom)
SELECT DISTINCT pays
FROM TPINF351.Affiliation
WHERE 1;


-- CHARGEMENTS DES ARTICLES
INSERT INTO Entrepot.Article (titre, annee)
SELECT titre_article, annee
FROM TPINF351.Article
WHERE 1;

-- CHARGEMENTS DES AUTEURS
INSERT INTO Entrepot.Auteur (nom)
SELECT nom_encode
FROM TPINF351.Auteur
WHERE 1;

-- CHARGEMENTS DE AUTEUR_ARTICLE
INSERT INTO Entrepot.AuteurArticle (idAuteur, idArticle)
SELECT DISTINCT idAuteur, idArticle
FROM TPINF351.AuteurArticle
WHERE 1;

-- CHARGEMENT DES AFFILIATIONS
INSERT INTO Entrepot.Affiliation (etablissement, pays)
SELECT Entrepot.Institution.idInstitution, Entrepot.Pays.idPays
FROM TPINF351.Affiliation
INNER JOIN Entrepot.Institution ON Entrepot.Institution.nom = TPINF351.Affiliation.etablissement
INNER JOIN Entrepot.Pays ON Entrepot.Pays.nom = TPINF351.Affiliation.pays;

-- CHARGEMENTS DE AUTEUR_FILIATION
INSERT INTO Entrepot.AuteurFiliation (idAuteur, idAfiliation)
SELECT DISTINCT Auteur.idAuteur, Affiliation.idAfiliation
FROM TPINF351.AuteurFiliation
INNER JOIN TPINF351.Auteur ON TPINF351.AuteurFiliation.idAuteur = TPINF351.Auteur.idAuteur
INNER JOIN TPINF351.Affiliation ON TPINF351.AuteurFiliation.idAfiliation = TPINF351.Affiliation.idAfiliation;
