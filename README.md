# lcd_sncf


[see it in action ! !](https://imgur.com/a/ukOrs)

## Hardware
* Raspberry Pi 2 ou 3 (peut-être le 1B ?)  
* LCD RGB (grove ou adafruit)  
* quelques fils pour le grove, beaucoup pour celui d'adafruit.  
* voltage shifter (5v <-> 3.3v) pour le grove

Deux écrans LCD sont supportés : Adafruit LCD RGB et Grove LCD RGB

### Adafruit LCD RGB
18 pins, montage classique, RAS. Potentiomètre de contraste.

### Grove LCD RGB
I2C 5v logic. Nécessite un voltage shifter avec un montage particulier. L'alimentation directement sur celle du RPI 5V ! Les trois autres pins à travers le voltage shifter.

## Principe

Récupère chaque jour une info sur google calendar : à quelle heure ai-je cours ?

En fct de cet horaire, choisi un train à prendre pour arriver à l'heure (35' plus tôt à Hz)

Affiche sur l'écran LCD :
* le temps pour déjeuner (en vert)
* qu'il est l'heure de me préparer (en cyan)
* qu'il est l'heure de partir (en rouge)  

Ensuite éteint l'écran.

## crontab - lancement automatique
Les logs seront enregistrés dans `~/lcd_sncf/calendrier.log`  
Taper : `$ mkdir ~/lcd_sncf/` puis `$ touch ~/lcd_sncf/calendrier.log`  
Taper : `$ sudo crontab -e` et ajouter à la fin :

    # lancer calendrer au boot
    @reboot sleep 300; /usr/bin/python /home/pi/lcd_sncf/grove_lcd/grove-lcd-master/calendrier.py >> /home/pi/lcd_sncf_log/calendrier.log 2>&1
    # lancer calendrier a minuit  
    05 00 * * * /usr/bin/python /home/pi/lcd_sncf/grove_lcd/grove-lcd-master/calendrier.py >> /home/pi/lcd_sncf_log/calendrier.log 2>&1

Si nécessaire, éditer le crontab pour le lcd d'adafruit en dirigeant vers les bons fichiers.
## troubleshooting

### L'écran Adfafruit lcd reste allumé, continue d'afficher du texte...
Taper : `$ python ~/lcd_sncf/adafruit_lcd/dev/lcd_display.py` pour lancer des tests d'affichage et éteindre l'écran.

### Le grove plante
Le débrancher / rebrancher (fail)

## Versions

### 0.3
Ajout du GROVE LCD RGB.  
**Python Library for Seeed Studio's Grove RGB LCD**  

This is a work-in-progress port of https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight


### 0.2
FONCTIONNE !
3 fichiers et qq dependences
* calendrier.py : main truc, lance tous les jours à 0h et au boot (si tourne pas deja...)
* json_sncf : récupère les infos sncf
* lcd_display : commande l'écran lcd
* token.py : contient la clé sncf_api


### 0.1
élements séparés en python
* json_sncf : librairie qui récupère les horaires et infos des trains en questions, 2 nlles fct pour 8h et 12h45 (mes horaires cette année)  
* lcd_display : affiche un msg à l'écran avec une couleur et vide l'écran
* lcd_event : brouillon de combinaison :  affiche des scheduled events sur l'écran lcd


fritzing :
* proto grand breadboard (actuel)
* proto mini breadboard

## brouillon :

1. récupérer l'horaire du cours
1. récupérer l'horaire du train
1. calculer le temps nécessaire : se préparer, partir, metro, train, marcher, salle  
    pour 8H : debout 5H30, partir 6h15, metro etc. 25, gare 6h40, train 6h45  
    la couleur LCD reflète :  
    * vert good > 15'
    * orange se préparer < 15'
    * rouge + clignoter = partir
    * ensuite s'éteint 15' après
