#!/usr/bin/python
import glob
from PIL import Image
from PIL import ImageStat
from PIL import ImageChops
from PIL import ImageFont
from PIL import ImageDraw
from PIL.ExifTags import TAGS, GPSTAGS
import string, sys, traceback, datetime, time, calendar
import os, shutil
from PIL import *
import math
from dayMaker import *


outputDir = 'Outputs'

#def dayBlock(DAY, blockSize):

def dayBlock(DAY):

	'Creates a dayBlock from a list of JPGs'

	backGround = (255,255,255)

	imageWidth  = imW = 1920
	imageHeight = imH = 1278

	thumbSize   = (imW, imH)

	# 			 	width, height
	blockSize1 = (    imW, 4 * imH)  # one column of four images
	blockSize2 = (4 * imW,     imH)  # four columns of one image
	blockSize3 = (2 * imW, 2 * imH)  # two columns of two images

	blockSize = blockSize1 # which blockSize to use? 1, 2 or 3


	quality = 100


	if os.path.isdir(outputDir) != 1:
            os.mkdir(outputDir)

	cellInfo = []
	today = os.path.basename(DAY[0])
	
	location = today[0:7]
	today = today[8:18]
	
	print '\ntoday ', today
	print ' '


	#create new Proof.tiff file
	Proofimg = Image.new('RGB', blockSize, backGround)

	
	fnt = ImageFont.truetype('TrueTypeFonts/arial.ttf', 30)

	#process all thumbs from day
	for name in DAY:

	
		#resize
		img = Image.open(name).resize(thumbSize)
		name = os.path.basename(name)
		#parse cellInfo
		nameInfo = dayMaker(name) # call to cellNUmbers function that delivers info for each image in proof set 
		cellInfo.append(nameInfo) #list of cellInfo for each cell

   		Proofimg.paste(img,(nameInfo[12][0],nameInfo[12][1]))


   	#Proofimg.save(outputDir+'/'+nameInfo[2] +'_'+ today +'_'+'PROOF_'+'.tif','tiff', quality=quality)#tiff
   	#Proofimg.save(outputDir+'/'+nameInfo[2] +'_'+ today +'_'+'PROOF_'+'.jpg','jpeg', quality =100) #jpeg

   	Proofimg.save(outputDir+'/'+ location +'_'+ today +'_'+'.tif','tiff', quality = quality )
	

	print 'cellInfo ',cellInfo