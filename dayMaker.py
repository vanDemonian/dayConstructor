#!/usr/bin/python

def dayMaker(name):
	"""
	creates an individual array representation of the
	four jpegs for am, noon, pm and midnight

	                Format 1: 1 x 4

                    Format 2: 4 x 1

                    Format 3: 2 x 2


	"""
	xstep = 1920
	ystep = 1278


	shape = 1  # 1 = 1 x 4, 2 = 4 x 1, 3 = 2 x 2


	location = 	str(name[0:7])
	date = 		str(name[8:18])

	year = 		int(name[8:12])
	month = 	int(name[13:15])
	day = 		int(name[16:18])

	hour = 		int(name[19:21])
	minute = 	int(name[22:24])
	second = 	int(name[25:27])
	

	secs_since_midnight = (int(second) + int(minute*60) + int(hour*3600))

	#	for debugging puposes
	#	print location,'_',year,'_',month,'_',day,'_',hour,'_',minute,'_',second
	#	print 'seconds_since_midnight =', secs_since_midnight 

	if   secs_since_midnight <  21600:
		gridNum = 0
	elif secs_since_midnight <  43200:
		gridNum = 1
	elif secs_since_midnight <  64800:
		gridNum = 2
	elif secs_since_midnight <= 86400:
		gridNum = 3


		# 1 column of four rows	
	if gridNum == 0:
		cellCoordinates = (0*xstep, 0*ystep)
	if gridNum == 1:
		cellCoordinates = (0*xstep, 1*ystep)
	if gridNum == 2:
		cellCoordinates = (0*xstep, 2*ystep)
	if gridNum == 3:
		cellCoordinates = (0*xstep, 3*ystep)









	return  gridNum, secs_since_midnight, location, year, month, day, hour, minute, second, date, xstep , ystep, cellCoordinates






"""
		# 4 columns on one row	
	if gridNum == 0:
		cellCoordinates = (0*xstep, 0*ystep)
	if gridNum == 1:
		cellCoordinates = (1*xstep, 0*ystep)
	if gridNum == 2:
		cellCoordinates = (2*xstep, 0*ystep)
	if gridNum == 3:
		cellCoordinates = (3*xstep, 0*ystep)



"""



"""

	# 2 columns by two rows	
	if gridNum == 0:
		cellCoordinates = (0*xstep, 0*ystep)
	if gridNum == 1:
		cellCoordinates = (1*xstep, 0*ystep)
	if gridNum == 2:
		cellCoordinates = (0*xstep, 1*ystep)
	if gridNum == 3:
		cellCoordinates = (1*xstep, 1*ystep)



"""











