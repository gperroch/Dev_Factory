# Main de lancement de l'usine de developpement
# Mettre a part les Classes
# Ajouter des parametres pour controler les differents processus de l'usine
# Ajouter le nettoyage des dossiers de sources et du rapport d'analyse

# OPTIONS d'EXECUTION
#			--mail: specifie une nouvelle adresse mail a laquelle envoyer les resultats. Override la default dans le fichier de config de l'usine (a definir)
#		RECUPERATION DES SOURCES
#			-d: ne pas telecharger les sources. Elles se trouvent deja dans l'usine
#			--path: specifie un chemin local a utiliser pour les sources. Override le ${PROJECT_NAME}_SOURCES. Utilise automatiquement le -d
#		ANALYSE
#			-A: skip l'analyse complete
#			-N: skip la norme
#			--norme_file: specifie le fichier dans lequel enregistrer les resultats de la norminette
#		TESTS UNITAIRES
#			--tu: skip les tu
#			-T: skip tous les tests, compile seulement
#		TESTS D'INTEGRATION
#			--ti: skip les ti
#			-T: skip tous les tests, compile seulement
#		COMPILATION
#			--compiler: specifie le compilateur a utiliser
#		TESTS FONCTIONNELS
#			--tf: skip les tests fonctionnels
#			-T: skip tous les tests, compile seulement

import os
import sys
import errno
import shutil
import traceback


def				main():
	number_args = len(sys.argv)
	if number_args < 2:
		print_usage()
	args = sys.argv[1:]

def				print_usage():
	options_short = ('N', )
	options_long = ('mail', 'path', 'norme_file', 'tu', 'ti', 'tf', 'compiler')
