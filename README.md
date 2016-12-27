# lcd_sncf

## todo :
1. 0.2 : coordonner le truc complet : lancé auto, récupère l'info (dans un fichier), selon l'horaire va chercher le train et lance les affichages
1. ajouter google calendar


## Principe

Récupère chaque jour une info sur google calendar : à quelle heure ai-je cours ?

En fct de cet horaire, choisi un train à prendre pour arriver à l'heure (35' plus tôt à Hz)

Affiche sur l'ecran LCD :
* le temps pour déjeuner (en vert)
* qu'il est l'heure de me préparer (en cyan)
* qu'il est l'heure de partir (en rouge)
* ensuite s'éteint

## Versions

Version 0.1 :
élements séparés en python
* json_sncf : librairie qui récupere les horaires et infos des trains en questions, 2 nlles fct pour 8h et 12h45 (mes horaires cette année)  
* lcd_display : affiche un msg à l'ecran avec une couleur et vide l'ecran
* lcd_event : brouillon de combinaison :  affiche des scheduled events sur l'ecran lcd

fritzing :
* proto grand breadboard (actuel)
* proto mini breadboard

## brouillon :

1. récupérer l'horaire du cours
1. récupérer l'horaire du train
1. calculer le temps nécessaire : se préparer, partir, metro, train, marcher, salle  
    pour 8H : debout 5H30, partir 6h15, metro etc. 25, gare 6h40, train 6h45  
    la couleur LCD reflete :  
    * vert good > 15'
    * orange se préparer < 15'
    * rouge + clignoter = partir
    * ensuite s'eteint 15' après
