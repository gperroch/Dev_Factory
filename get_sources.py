# Read xxx.conf given in parameters and download the sources

import os
import sys
import errno
import shutil
import traceback
import analyse


class	Configuration:
	def	__init__(self, **kwargs):
		self.sources_directory = kwargs.get("sources_directory")
		self.conf = kwargs.get("conf")
		self.project_name = kwargs.get("project_name")

	@property
	def	sources_directory(self):
		return self.__sources_directory
	@property
	def	conf(self):
		return self.__conf
	@property
	def	project_name(self):
		return self.__project_name

	@sources_directory.setter
	def	sources_directory(self, sources_directory):
		self.__sources_directory = sources_directory	# Verifier que le path est valide
	@conf.setter
	def	conf(self, conf):
		self.__conf = conf								# Verifier que le path est valide
	@project_name.setter
	def	project_name(self, project_name):
		self.__project_name = project_name


def		get_sources():
	filename = sys.argv[1]
	script_location = os.path.dirname(os.path.abspath(__file__))

	try:
		fd = open(filename, 'r')
	except:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		print("Couldn't open file:%s" % filename)
		traceback.print_tb(exc_traceback)
		sys.exit(1)

	#	Get the configuration
	for line in fd:
		if line.startswith("sources_location:"):
			sources_location = line[len("sources_location:"):].rstrip()
		if line.startswith("sources_url:"):
			sources_url = line[len("sources_url:"):].rstrip()
		if line.startswith("sources_path:"):
			sources_path = line[len("sources_path:"):].rstrip()
		if line.startswith("sources_type:"):
			source_type = line[len("sources_type:"):].rstrip()

	project_name = filename.split(".", 1)[0]
	sources_download_directory_local = script_location + "/" + project_name.upper() + "_DOWNLOAD"
	sources_directory_local = script_location + "/" + project_name.upper() + "_SOURCES"
	config = Configuration(sources_directory=sources_directory_local, conf=script_location + "/" + filename, project_name=project_name)

	#	Get the files
	try:
		if sources_location.startswith("local"):
			shutil.copytree(sources_path, sources_directory_local, symlinks=True)
		elif sources_location.startswith("remote"):
			cmd = "git clone " + sources_url + " " + sources_download_directory_local
			os.system(cmd)
			if len(sources_path) > 0:
				shutil.copytree(sources_download_directory_local + "/" + sources_path, sources_directory_local, symlinks=True)
			else:
				os.rename(sources_download_directory_local, sources_directory_local)
		else:
			print("sources_location not supported:%s" % sources_location)
	except:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		print("Error in parsing %s: %s" % filename, exc_type)
		traceback.print_tb(exc_traceback)
		sys.exit(2)

	fd.close()
	return (config)

conf = get_sources()
analyse.analyse(conf)
