# Nonogram-Solver
<p float="center" align="center">
  <img src="https://github.com/Kugge/Nonogram-Solver/blob/master/imgs/preview.png?raw=true" width="250" height="250"/>
  <img src="https://github.com/Kugge/Nonogram-Solver/blob/master/imgs/preview2.png?raw=true" width="250" height="250"/>
</p>

Projet Nonogram  
Par Sofiane DJERBI &amp; Salem HAFTARI
## Lancer le programme
Programme non compatible avec python2.  
Installation des dépendances avec pip: `pip install -r requirements.txt`  
Lancement du programme: `python main.py` (+ `cd src/`)  
Pour utiliser le scrapper: `pip install requests-html`  
(il est parfois nécéssaire de lancer le programme deux fois afin d'installer le chrome driver)

## Conventions
- Les commentaires sont en Français, le code en Anglais.
- Paradigme de la programmation orientée objet.
- Toute fonction doit être documentée.
- Les conventions plus précises (par exemple, les conventions grapiques) sont dans le code source, au début de chaque fichier, en commentaire si besoin.
## Resources
- Librairie graphique `pygame`.
- Librairie de serialisation `pickle`.
- Librairie de requêtes html `requests-html`, facultative (1).
## TODO
- ~~Faire une librairie graphique~~ Fait
- ~~Faire un outil permettant de convertir un nonogramme en données exploitables~~ Fait
- ~~Modéliser un nonogramme en FNC~~ Fait
- ~~Implémenter un solveur SAT~~ Fait
- ~~Implémenter NOTRE solveur SAT~~ Fait
## Infos supplémentaires
(1) : On ne va pas obliger le correcteur à installer cette librairie trop lourde pour une fonctionnalité qui n'est pas censée être dans le projet. C'est pourquoi on proposera des nonogrammes déjà "téléchargés" sous forme de fichiers. Cependant, soyez libre d'installer requests-html et le driver chromium pour utiliser notre scraper.
