# Proceed to analyse the sources
# First step is the norme

import os
import sys
import errno
import shutil
import traceback

def		analyse(conf):
	try:
		cmd = "norminette " + conf.sources_directory + " > norme.txt"
		os.system(cmd)
		fd_norme = open("norme.txt", "r")
		fd_rapport = open("rapport.txt", "a")
		content = fd_norme.readlines()
		number_lines = len(content)
		index = 0
		while index < number_lines:
			if ((index < number_lines - 1
			and content[index].startswith("Norme")
			and content[index + 1].startswith("Error"))
			or (index > 0 and content[index].startswith("Error"))):
				fd_rapport.write(content[index])
			index += 1
	except:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		print("Error in analyse %s: %s" % conf.project_name, exc_type)
		traceback.print_tb(exc_traceback)
		sys.exit(3)
