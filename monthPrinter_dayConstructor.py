#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
---------------------------------------------------------------------------------------------------
Filename:           JPG_monthPrinter_dayConstructor.py
Author:             Martin Walch
Release Date:       2016-09-22
Description:        day Constructor for DTLA exhibition prints
                    
            ****    No gaps between thumbnails  *****

                    Iterates through a directory tree of JPG's renamed by JPG_reNamer.py.

                    TARONGA_2014_09_29-11_56_58.jpg

            ****    Filters the list to select
                    four images from each day

                    6am
                    12noon
                    6pm
                    12 midnight
            

Required Modules:  
                    











                    
---------------------------------------------------------------------------------------------------
"""
import glob
from PIL import Image
from PIL import ImageStat
from PIL import ImageChops
from PIL.ExifTags import TAGS, GPSTAGS
import string, sys, traceback, datetime, time, calendar
import os, shutil
from PIL import *
import math
from multiprocessing import Pool
from proofSheet_Multi import *
from dayMaker import *
from dayBlock import *



inputDir = '/Volumes/3TB_DP/KINGWIL/2015'   #root directory that will be parsed (includes subdirectories)
#outputDir = '/Users/pyDev/Documents/JPG_dayProofer_Multi/JPG_proof_Outputs' #output directory (must be created before script is run)
fileExt = '.jpg'
#cameraInterval = 300 #this is the number of seconds between each capture:   5mins = 300 secs

nameList = []
namePathList = []
namePathList_Filtered = []
dateList = []
cellInfo = []

DateChangeList =[]

DAYS = []
count = 0



def secsSincemidnight(name):

    location =  str(name[0:7])
    date =      str(name[8:18])

    year =      int(name[8:12])
    month =     int(name[13:15])
    day =       int(name[16:18])

    hour =      int(name[19:21])
    minute =    int(name[22:24])
    second =    int(name[25:27])
    

    secs_since_midnight = (int(second) + int(minute*60) + int(hour*3600))

    return secs_since_midnight



def Timer(start, end):
    """
    Calculates the time it takes to run a process, based on start and finish times
    ---------------------------------------------------------------------------------------------
    Inputs:       in seconds 
    start:        Start time of process
    end:          End time of process
    ---------------------------------------------------------------------------------------------
    """
    elapsed = end - start
    # Convert process time, if needed
    if elapsed <= 59:
        time = str(round(elapsed,2)) + " seconds\n"
    if elapsed >= 60 and elapsed <= 3590:
        min = elapsed / 60
        time = str(round(min,2)) + " minutes\n"
    if elapsed >= 3600:
        hour = elapsed / 3600
        time = str(round(hour,2)) + " hours\n"
    return time


##### RUN #####

if __name__ == '__main__':
    #start = time.clock()
    start = time.time()

    print '   '
    print 'JPG_monthPrinter_dayConstructor.py   '
    print '   '

    # loop to create list of names and paths
    for root, dirs, files in os.walk(inputDir):
        for name in files:
            
            if name.endswith(fileExt):

                nameList.append(name)           #list of filenames - basename only
                namePathList.append(os.path.join(root,name))    #list of names with directory paths

                count = count + 1

    #---------------------------------------------------------------
    #print namePathList - debug

    #set date of first name as today and appends it to the start of 'dateList'
    todaysdate = nameList[0][8:18]
    dateList.append(todaysdate)
    #print dateList - debug

    #   loop to create list of days by checking if the date changes
    #   and adding the date to the list of dates it does.
    for name in nameList:

        if name[8:18] != todaysdate:
            #create new day and append name
            dateList.append(name[8:18])
            #make the new date = 'today'
            todaysdate = name[8:18]


    numberofDays = len(dateList)
    print 'Number of Days = ', numberofDays


    #---------------------------------------------------------------
    print "________________________________________________________"

    for name in namePathList:
        print name

    print "________________________________________________________"
    print "________________________________________________________"
    #---------------------------------------------------------------


    for name in namePathList:
        item = name[-31:]
 
        x = secsSincemidnight(item)

        if   x >=21300 and x <= 21600:  # 5 mins before 6am
            namePathList_Filtered.append(name)
        elif x >= 42900 and x <= 43200: # 5 mins before noon
            namePathList_Filtered.append(name)
        elif x >= 64500 and x <= 64800: # 5 mins before 6pm
            namePathList_Filtered.append(name)
        elif x >= 86100 and x <= 86400: # 5 mins before midnight
            namePathList_Filtered.append(name)


    #---------------------------------------------------------------




    namePathList = namePathList_Filtered







    #---------------------------------------------------------------

    today = 0

    for i in range(0,len(namePathList)):
        date = os.path.basename(namePathList[i])
        date = date[8:18]
        

        if date != today:
            today = date
            DateChangeList.append(i)
        
        print ' ', i, '   ', date

    DateChangeList.append(len(namePathList))
    print 'Date Change List  ', DateChangeList


    #---------------------------------------------------------------

    d = 0

    for x in range(len(DateChangeList)-1):
        #print x,' ', len(namePathList)
        v = DateChangeList[d]
        
        v1 =DateChangeList[(d+1)]
        print 'v ',v,'v1 ',v1
        proofPath = namePathList[v:v1]
        DAYS.append(proofPath)

        d+=1

    #---------------------------------------------------------------




    pool = Pool()
    pool.map(dayBlock, DAYS)
    pool.close()
    pool.join()

    print ' '
    print ' '
    print ' '

   




    finish = time.time()



    print 'List of dates in data', dateList
    print 'Total Number of dates = ', len(dateList)
    print 'Total Number of Images processed: ', str(count)
    print 'Processing done in ', Timer(start, finish), '\n'






