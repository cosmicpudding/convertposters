#!/usr/bin/python
# CONVERT POSTERS: Convert PDF posters in "input" folder to JPG posters in "output" folder
# V.A. Moss (vanessa.moss@csiro.au)
__author__ = "V.A. Moss"
__version__ = "0.1"

import os
import sys
import platform
import glob

downsize = False

# Check architecture
archit = platform.platform().lower()

files = glob.glob('input/*pdf')
print(files)

for fname in files:

	stem = fname.split('/')[-1].split('.pdf')[0]

	# Check if it is already in output, and if so, skip
	# Comment this out if not needed or want to regenerate
	output = glob.glob('output/%s*' % stem)
	if len(output) > 0:
		print('%s is done... continuing!' % stem)
		continue

	# Downsize possibility
	if downsize != True:
		os.system('cp %s small.pdf' % fname)
	else:
		# This may be useful if needing to downsize the poter size but significantly reduces quality (may need tweaking)
		os.system('gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/default -dNOPAUSE -dQUIET -dBATCH -sOutputFile=small.pdf %s' % fname)

	# Deal with different architectures (won't work on Windows though)
	if 'linux' in archit:
		retval = os.system('convert -resize 4096x4096 -density 200 -background white -flatten small.pdf output/%s.jpeg' % (stem))
	if 'darwin' in archit:
		retval = os.system('sips -Z 4096 -s format jpeg small.pdf --out output/%s.jpeg' % (stem))


