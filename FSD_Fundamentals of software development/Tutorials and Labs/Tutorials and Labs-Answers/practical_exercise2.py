def getDistanceTime():
    distanceTime = []
    
    distance = float(input("Enter distance in meters(m):\t"))
    while distance != -1:
        distanceTime.append(distance)
        time = float(input("Enter time in seconds(s):\t"))
        distanceTime.append(time)
        distance = float(input("Enter distane in meters(m):\t"))
    return distanceTime

def calculateSpeed(distanceTime):
    speedList = []
    for x in range(0,len(distanceTime),2):
        distance = distanceTime[x]
        time = distanceTime[x+1]
        speed = distance/time
        speedList.append(speed)
    return speedList

def trailRecord():
    dt = getDistanceTime()
    s = calculateSpeed(dt)
    filehandler = open('practical_exercise2.txt','w')
    filehandler.write("Distance(m)\t\tTime(s)\t\tSpeed(m/s)\n")
    for i in range(0,len(dt),2):
        filehandler.write(str(dt[i])+'\t\t' + str(dt+[i+1]) +'\t\t' + str(s[i/2]) + '\n')
    filehandler.close()

trailRecord()


