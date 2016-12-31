# lcd_sncf

## Principe

[see it in action](https://imgur.com/a/ukOrs)

Récupère chaque jour une info sur google calendar : à quelle heure ai-je cours ?

En fct de cet horaire, choisi un train à prendre pour arriver à l'heure (35' plus tôt à Hz)

Affiche sur l'ecran LCD :
* le temps pour déjeuner (en vert)
* qu'il est l'heure de me préparer (en cyan)
* qu'il est l'heure de partir (en rouge)
* ensuite s'éteint

## crontab - lancement automatique
Les logs seront enregristrés dans `~/lcd_sncf/calendrier.log`  
Taper : `$ mkdir ~/lcd_sncf/` puis `$ touch ~/lcd_sncf/calendrier.log`  
Taper : `$ sudo crontab -e` et ajouter à la fin :

    # lancer calndrier au boot
    @reboot sleep 300; /usr/bin/python /home/pi/lcd_sncf/dev/calendrier.py >> /home/pi/lcd_sncf_log/calendrier.log 2>&1
    # lancer calendrier a minuit  
    05 00 * * * /usr/bin/python /home/pi/lcd_sncf/dev/calendrier.py >> /home/pi/lcd_sncf_log/calendrier.log 2>&1

## Versions

### 0.2
FONCTIONNE !
3 fichiers et qq dependances
* calendrier.py : main truc, lance tous les jours à 0h et au boot (si tourne pas deja...)
* json_sncf : recupere les infos sncf
* lcd_display : commande l'ecran lcd
* token.py : contient la clé sncf_api


### 0.1
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
