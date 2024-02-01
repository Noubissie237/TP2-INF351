-- CREATION DES TABLES POUR L'ENTREPOT DE DONNÉES

-- CREATION DE LA TABLE PAYS
CREATE TABLE Pays(
    idPays INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nom VARCHAR(100)
);

-- CREATION DE LA TABLE AUTEUR
CREATE TABLE Auteur(
    idAuteur INT PRIMARY KEY AUTO_INCREMENT, 
    nom VARCHAR(50)
);

-- CREATION DE LA TABLE ARTICLE
CREATE TABLE Article (
    idArticle INT PRIMARY KEY AUTO_INCREMENT,
    titre VARCHAR(250),
    annee INTEGER
);

-- CREATION DE LA TABLE INSTITUTION
CREATE TABLE Institution(
    idInstitution INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(250)
);

-- CREATION DE LA TABLE AFFILIATION
CREATE TABLE Affiliation(
    idAfiliation INT PRIMARY KEY AUTO_INCREMENT,
    etablissement INTEGER,
    pays INTEGER,
    FOREIGN KEY (etablissement) REFERENCES Institution(idInstitution),
    FOREIGN KEY (pays) REFERENCES Pays(idPays)
);

-- CREATION DE LA TABLE AUTEUR FILIATION
CREATE TABLE AuteurFiliation(
    idAuteur INT,
    idAfiliation INT,
    FOREIGN KEY (idAuteur) REFERENCES Auteur(idAuteur),
    FOREIGN KEY (idAfiliation) REFERENCES Affiliation(idAfiliation),
    PRIMARY KEY(idAuteur, idAfiliation)
);

-- CREATION DE LA TABLE AUTEUR ARTICLE
CREATE TABLE AuteurArticle(
    idAuteur INT,
    idArticle INT,
    FOREIGN KEY (idAuteur) REFERENCES Auteur(idAuteur),
    FOREIGN KEY (idArticle) REFERENCES Article(idArticle),
    PRIMARY KEY(idAuteur, idArticle)
);