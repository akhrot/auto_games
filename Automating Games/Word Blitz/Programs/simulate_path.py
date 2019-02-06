import time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

posX = []
posY = []
global device

def generate_coordinates():
	withBar = 'y'

	if withBar=='y' or withBar=='Y':
		startX = 168
		startY = 924
		endX = 914
		endY = 1670
	else:
		startX = 168
		startY = 865
		endX = 914
		endY = 1611

	diffX = endX-startX
	diffY = endY-startY

	for j in range(0, 4):
		curY = startY + (diffY*j)//3
		horposX = []
		horposY = []
		for i in range(0, 4):
			curX = startX + (diffX*i)//3
			horposX.append(curX)
			horposY.append(curY)
		posX.append(horposX)
		posY.append(horposY)

def simulate_path(x, y):
	delay = 0.1
	global device
	device.touch(posX[x[0]][y[0]], posY[x[0]][y[0]], MonkeyDevice.DOWN)
	time.sleep(delay)
	for i in range(1, len(x)):
		device.touch(posX[x[i]][y[i]], posY[x[i]][y[i]], MonkeyDevice.MOVE)
		time.sleep(delay)
	i = len(x)-1
	device.touch(posX[x[i]][y[i]], posY[x[i]][y[i]], MonkeyDevice.UP)
	time.sleep(delay)

def main():
	generate_coordinates()
	x = [2, 1, 1, 0, 1, 2, 2, 1]
	y = [0, 0, 1, 1, 2, 3, 2, 3]

	global device
	print "Connecting to device"
	device = MonkeyRunner.waitForConnection()
	print "Device connected"

	simulate_path(x, y)

main()