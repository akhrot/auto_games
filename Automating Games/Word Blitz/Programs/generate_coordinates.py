import time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

withBar = 'n'

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

posX = []
posY = []

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

print(posX)
print(posY)

for i in range(0, 4):
	for j in range(0, 4):
		print(posX[i][j], ",", posY[i][j])
	print("")

x1 = 1
y1 = 2
x2 = 2
y2 = 3
x3 = 2
y3 = 2
x4 = 1
y4 = 3
x5 = 0
y5 = 3

device = MonkeyRunner.waitForConnection()
print("Device connected")

device.touch(posX[x1][y1], posY[x1][y1], MonkeyDevice.DOWN)
time.sleep(0.05)
device.touch(posX[x2][y2], posY[x2][y2], MonkeyDevice.MOVE)
time.sleep(0.05)
device.touch(posX[x3][y3], posY[x3][y3], MonkeyDevice.MOVE)
time.sleep(0.05)
device.touch(posX[x4][y4], posY[x4][y4], MonkeyDevice.MOVE)
time.sleep(0.05)
device.touch(posX[x5][y5], posY[x5][y5], MonkeyDevice.MOVE)
time.sleep(0.05)
device.touch(posX[x5][y5], posY[x5][y5], MonkeyDevice.UP)

time.sleep(0.05)

device.touch(posX[x1][y1], posY[x1][y1], MonkeyDevice.DOWN)
time.sleep(0.05)
device.touch(posX[x2][y2], posY[x2][y2], MonkeyDevice.MOVE)
time.sleep(0.05)
device.touch(posX[x3][y3], posY[x3][y3], MonkeyDevice.MOVE)
time.sleep(0.05)
device.touch(posX[x4][y4], posY[x4][y4], MonkeyDevice.MOVE)
time.sleep(0.05)
device.touch(posX[x5][y5], posY[x5][y5], MonkeyDevice.MOVE)
time.sleep(0.05)
device.touch(posX[x5][y5], posY[x5][y5], MonkeyDevice.UP)