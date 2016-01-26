#!/usr/bin/env python
import os
import time
from random import randint

# Time Configuration
SECONDS=5
MINUTES=0
HOURS=0

# File Configuration
IMG_FOLDER="/home/jeremy/Downloads/Background_Imgs"

# Fixes anystring that has spaces to be a linux path
def fixSpaces(string):
	retString = ""

	for s in string:
		if s == ' ':
			retString += "\\ "
		else:
			retString += s
	return retString 

def changeBackground():
	backgrounds_path = IMG_FOLDER
	files = os.listdir(backgrounds_path)
	directory_size = len(files)
	img_number = randint(0, directory_size-1)

	# Need to check if file is actually a file and not a folder
	path = os.path.abspath(backgrounds_path + "/" + files[img_number])
	final_path = fixSpaces(path)
	print final_path;
	os.system("gsettings set org.gnome.desktop.background picture-uri file://" + final_path)


def run():
	# Get total number of seconds
	totalSeconds = HOURS * 60 * 60 + MINUTES * 60 + SECONDS

	while(True):
		changeBackground()
		time.sleep(totalSeconds)

############################### Run the Program #############################################
run()