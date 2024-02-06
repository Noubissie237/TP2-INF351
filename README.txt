##-----------------------EXPLICATION DETAILLÉE DE LA MISE EN MARCHE DE TOUT LE TP (Partant de la BD opérationnelle du TP1 vers l'entrepôt du TP2)



1) Se connecter à MySQL et créer Deux (02) Bases de données nommées respectivement (tout en respectant la cass):
   - TPINF351
   - Entrepot

2) Executer le programme python se trouvant dans le dossier "Backup_TP_1". Pour cela, proccedez comme suite:
   - Ouvrir le programme python (fichier prog.py), et verifier à la ligne neuf (09) les information de connexion à votre base de données (le user et password)
   - Telecharger (si vous n'avez pas ) les dependance necessaire en tapant sur le terminal les deux commandes ci-dessous:
         .  pip install matplotlib
         .  pip install mysql-connector-python
   - Une fois les 02 étapes ci-dessus effectuées, vous pouvez lancer l'execution du programme en tapant la commande:
         .  python3 prog.py

3) Créer l'Entrepot de données et charger les données venant de la premiere Base de données. Pour cela, pour avez deux possibilités:

   1ère possibilité : Via le programme python

      Pour ce faire, 
         . Ouvrir le fichier main.py et verifier à la ligne quatre (09) et cinq (05) les information de connexion à votre base de données (le gobalUserName et GlobalPassword)
         . lancer tout simplement l'execution du programme python en tapant la commande
            -  python3 main.py

         ceci va créer l'entrepot de données, et effectuées le chargement des données depuis la première Base de données et vous donnera même la possibilité d'exécuter des requêtes decisionnelles


   2ème possibilité : Via les Script SQL

      Pour ce faire,
         . Ouvrir votre phpMyAdmin ou MySQL Workbench et importez juste respectivement les fichiers 'createEntrepotTables.sql' et 'loadDataFromTP1'
         . Une fois ces deux fichiers importées, vous pouvez ouvrir le fichier 'requetesDecisionnelles.txt' et tester requête par requête