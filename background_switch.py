#!/usr/bin/env python
import os
import sys
import time
from random import randint
from PIL import Image

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

# Picks a new background randomly and then displays it
def changeBackground():
	try:
		files = os.listdir(IMG_FOLDER)
	except IOError:
		print "Folder path is bad. Please recheck that folder path is correct."
		sys.exit(-1)

	directory_size = len(files)

	# TODO: Throw an error if Img folder is empty
	img_number = randint(0, directory_size-1)

	# TODO: Need to check if file is actually a file and not a folder

	path = os.path.abspath(IMG_FOLDER + "/" + files[img_number])
	final_path = fixSpaces(path)
	print final_path;
	os.system("gsettings set org.gnome.desktop.background picture-uri file://" + final_path)

# Check if File is a PNG file
def isPNG(fileName):
	fileName = fileName.lower()

	fileLen = len(fileName)
	if fileName[fileLen - 4] != '.':
		return False
	if fileName[fileLen - 3] != 'p':
		return False
	if fileName[fileLen - 2] != 'n':
		return False
	if fileName[fileLen - 1] != 'g':
		return False

	return True

# Check if File is a JPG file
def isJPG(fileName):
	fileName = fileName.lower()

	fileLen = len(fileName)
	if fileName[fileLen - 4] != '.':
		return False
	if fileName[fileLen - 3] != 'j':
		return False
	if fileName[fileLen - 2] != 'p':
		return False
	if fileName[fileLen - 1] != 'g':
		return False

	return True

# Verify that the director given by the user is valid directory
# and that the directory has at least 1 picture
def verifyDirectory():
	try:
		files = os.listdir(IMG_FOLDER)
	except IOError:
		print "Folder path is bad. Please recheck that folder path is correct."
		sys.exit(-1)

	hasPicture = False

	if len(files) == 0:
		raise "Directory size is 0"

	for f in files:
		if isJPG(f) or isPNG(f):
			return True

	return hasPicture

# Runner of the program
def run():
	# Verify that Img folder is not empty and does not contain all folders
	if verifyDirectory() == False:
		raise NameError('Directory failed verification')
	# Get total number of seconds
	totalSeconds = HOURS * 60 * 60 + MINUTES * 60 + SECONDS
	while(True):
		changeBackground()
		time.sleep(totalSeconds)

############################### Run the Program #############################################
run()