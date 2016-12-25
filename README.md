# sncf_lcd
affichage LCD du temps nécessaire pour se préparer et partir

Affichage LCD du temps disponible le matin avant de devoir partir 


projet :

1. récupérer l'horaire du cours
1. récupérer l'horaire du train 
1. calculer le temps nécessaire : se préparer, partir, metro, train, marcher, salle  
    pour 8H : debout 5H30, partir 6h15, metro etc. 25, gare 6h40, train 6h45  
    la couleur LCD reflete :  
    * vert good > 15'
    * orange se préparer < 15'
    * rouge + clignoter = partir
    * ensuite s'eteint 15' après
    
todo :

tout lol

non c'est pas vrai ! y'a déjà des trucs qui marchent !

Que sais-je faire ?

1. récupérer les horaires sncf en json et mettre en forme vaguement
1. afficher du texte avec une couleur, faire clignotter


Qu'est ce qui galere ?

1. calendar api. marche qd elle veut... ça soule. 

ordre :

1. récupérer les données sncf en python. jsais le faire en ajax mais c'est mort ! P Y T H O N
2. créer les affichages en texte
3. créer les affichages lcd (tester bcp avant sinon des surprises...)
4. ajouter google calendar


