"""program that changes input"""

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
storedPassword = []
ArandomAlphabet = ['w','n','h','s','t','f','d','b','z',' ','x','i','p','o','a','e','v','g','j','u','y','r','q','c','m','k','l']
BrandomAlphabet = ['e','f','a','b','c','d','g','h','i','j','k','l','m','q','r','s','t','u','v','w','x','y','z',' ','n','o','p',]
newPassword = []

def convert(password):
	length = int(len(password))
	start = 0
	while start < length:
		x = password[start]
		value = int(alphabet.index(x))
		storedPassword.append(value)
		start+=1 
	changeNumericValue()

def changeNumericValue():
	arrayLength = int(len(storedPassword))
	start = 0
	while start < arrayLength:
		x = storedPassword[start]
		recreateNumber(x)
		start+=1
	encrypted = ' '.join(newPassword)
	encrypted = encrypted.replace(" ","")
	
def recreateNumber(password):
	print "Select encryptor 'A' or 'B'"
	format = raw_input("")

def encrypt():
	print "Enter message to encrypt:"
	password = raw_input("")
	convert(password)

encrypt()