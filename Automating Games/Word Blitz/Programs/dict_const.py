f = open("C:\\Users\\Jinish\\Desktop\\C++\\Games\\Word Blitz\\Programs\\words.txt", "r")
lines = f.readlines()

words = {}

for line in lines:
	words[line[:-1]] = 1

if 'model' in words:
	print("Word model is present")
else:
	print("Word model is not present")