import time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

device = 0

words = {}
found = {}
grid = []

visited = []
pathX = []
pathY = []
curword = ''

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
				print pathX
				print pathY
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
	input_words()

	grid_line = 'elelotispaenpprn'

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

	# device = MonkeyRunner.waitForConnection()
	# print "Device connected\n"

	global curword
	curword = ''
	for i in reversed(range(1, 9)):
		print "Words of length : ", i
		for x in range(0, 4):
			for y in range(0, 4):
				find_words(x, y, i)

main()