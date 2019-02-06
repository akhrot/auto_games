word = 'Hello there'

def foo():
	global word
	word += '345'

def main():
	foo()

main()
print word