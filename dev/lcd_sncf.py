#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
0.0 25/12/2016 :
	todo : tout
	* import du char_lcd_rgb.py d'adafruit
	* github
	* une date quelconque, affiche les infos
0.1 26/12/2016 :
	todo : etablir un calendrier hebodmadaire
	lun : no
	mardi : 8h00
	mercredi : 8h00
	jeudi : 11h00
	vendredi : 8h00
	Chaque fois soustraire 35 minutes

	tester avec un objectif random
"""

	def affichage():
	# Example using an RGB character LCD wired directly to Raspberry Pi or BeagleBone Black.
	import time
	import Adafruit_CharLCD as LCD
	import json_sncf as sncf


	# Raspberry Pi configuration:
	lcd_rs = 27  # Change this to pin 21 on older revision Raspberry Pi's
	lcd_en = 22
	lcd_d4 = 25
	lcd_d5 = 24
	lcd_d6 = 23
	lcd_d7 = 18
	lcd_red   = 4
	lcd_green = 17
	lcd_blue  = 7  # Pin 7 is CE1

	# Define LCD column and row size for 16x2 LCD.
	lcd_columns = 16
	lcd_rows    = 2

	# Initialize the LCD using the pins above.
	lcd = LCD.Adafruit_RGBCharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
	                              lcd_columns, lcd_rows, lcd_red, lcd_green, lcd_blue)

	# affiche les horaires du train
	# exemple d'horaire : '20161229T080000'

	'''
	version 0.0 :
	'''

	donnees = sncf.train('20161229T080000') # donnees = [u'07:15', u'07:46', '31']

	# affiche l'heure de départ
	lcd.set_color(1.0, 0.0, 0.0)
	lcd.clear()
	lcd.message(donnees[0])
	time.sleep(3.0)

	# affiche l'heure d'arrivee
	lcd.set_color(0.0, 1.0, 0.0)
	lcd.clear()
	lcd.message(donnees[1])
	time.sleep(3.0)

	# affiche la duree du trajet
	lcd.set_color(0.0, 0.0, 1.0)
	lcd.clear()
	lcd.message(donnees[2])
	time.sleep(3.0)

	# eteint l'eclairage et vide l'écran
	lcd.set_color(0.0, 0.0, 0.0)
	lcd.clear()

if __name__ == '__main__':
	affichage()
