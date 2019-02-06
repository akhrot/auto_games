import time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

posX = []
posY = []
global device

words = {}
found = {}
grid = []

visited = []
pathX = []
pathY = []
curword = ''

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
	delay = 0.05
	global device
	device.touch(posX[x[0]][y[0]], posY[x[0]][y[0]], MonkeyDevice.DOWN)
	time.sleep(delay)
	for i in range(1, len(x)):
		device.touch(posX[x[i]][y[i]], posY[x[i]][y[i]], MonkeyDevice.MOVE)
		time.sleep(delay)
	i = len(x)-1
	device.touch(posX[x[i]][y[i]], posY[x[i]][y[i]], MonkeyDevice.UP)
	time.sleep(delay)

def isValid(x, y):
	if x<0 or x>=4:
		return False
	if y<0 or y>=4:
		return False
	return not visited[x][y]

def find_words(x, y, len):
	# print "x, y, l = ", x, y, len
	global curword
	visited[x][y] = True
	curword += grid[x][y]
	# print "Curword = ", curword
	pathX.append(x)
	pathY.append(y)

	if len==1:
		# print "Entered len==1, len = ", len
		if curword in words:
			if curword not in found:
				print(curword)
				simulate_path(pathX, pathY)
				found[curword] = 1
	else:
		nx = [x-1, x-1, x-1, x, x, x+1, x+1, x+1]
		ny = [y-1, y, y+1, y-1, y+1, y-1, y, y+1]
		for i in range(0, 8):
			if isValid(nx[i], ny[i]):
				find_words(nx[i], ny[i], len-1)
	visited[x][y] = False
	curword = curword[:-1]
	pathX.pop()
	pathY.pop()

def input_words():
	f = open("C:\\Users\\Jinish\\Desktop\\C++\\Games\\Word Blitz\\Programs\\words.txt", "r")
	lines = f.readlines()

	for line in lines:
		words[line[:-1]] = 1

	if 'model' in words:
		print("Word model is present")
	else:
		print("Word model is not present")

def main():
	generate_coordinates()
	input_words()

	grid_line = 'sduerrnariersiel'

	print grid_line

	for i in range(0, 4):
		line = []
		curvisit = []
		for j in range(0, 4):
			line.append(grid_line[(i*4)+j])
			curvisit.append(False)
		grid.append(line)
		visited.append(curvisit)

	for i in range(0, 4):
		for j in range(0, 4):
			print grid[i][j],
		print ""

	global device
	print "Connecting to device"
	device = MonkeyRunner.waitForConnection()
	print "Device connected"

	global curword
	curword = ''
	for i in reversed(range(2, 9)):
		print "Words of length : ", i
		for x in range(0, 4):
			for y in range(0, 4):
				find_words(x, y, i)

main()