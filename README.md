# Financial_review

# Installation
Installation tester avec Python 3.10.12
Pour les rapports pdf, ce programme nécessite l’installation de pdflatex.

Sur windows : installer [MikTex](https://miktex.org/)

Sur linux :
```
sudo apt install texlive-latex-base
sudo apt install texlive-fonts-recommended
sudo apt install texlive-fonts-extra
sudo apt install texlive-latex-extra
pdflatex --version
```
Assurer vous de mettre pdflatex dans vos variables Path du système, pour pouvoir le lancer depuis le dépôt local git de Financial_review

Puis pour installer l’environnement Python,
Dans le répertoire git cloné :
```
$python venv .venv
$source .venv/bin/activate
$pip install -r requirements.txt
# Puis lancer le programme avec
python main.py
```
Pour créer la base de données, dans main.py exécuter create_db
Pour mettre à jour la base de données, dans main.py exécuter maj_db
Pour un rapport texte, exécuter text_report()
Pour un rapport excel, exécuter excel_report()
Pour un rapport pdf, exécuter pdf_report()
Pour utiliser une api, exécuter api_report(), nécissite un abonnement.

Régler le portefeuille dans le fichier selection.txt, ou laisser tout le fichier commenter pour exécuter l’ensemble du dictionnaire des actions.

## Description
Élément d’analyse financière par automatisation de plusieurs rapports. Partie nécessitant le driver chrome de [Selenium](https://selenium-python.readthedocs.io/) commentée.

## Détails
L’objectif du logiciel est de fournir un tableau synoptique,
et un rapport plus complet, moyennant plus de temps de calcul, mais incluant notamment la volatilité à 30 jours et une simulation Monte-Carlo pour chaque valeur.

Tableau synoptique :

![](img/sample_01.png)

Rapport complet :

![](img/sample_02.png)

Exemples présents dans les dossiers de sorties :

* [rapport textuel](reports_txt/performance_du_jour.txt)

* [rapport excel](reports_excel/2024-08-30_synoptique.xlsx)

* [rapport pdf](reports_pdf/2024-08-30.pdf) (1 seule action dans l’exemple)
