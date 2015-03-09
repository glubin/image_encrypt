from PIL import Image
import random

# eventually convert to rbg so that it has a hex code

im = Image.open("sloth.jpg") # loads image
pixels = im.load()
rgb_im = im.convert('RGB') # create the pixel map
fileExt = "sloth" + str(random.randint(8000,10000) * 3 - random.randint(1,2999)) + ".png"

alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
xlimit = 270
prevSavedPts = [131, 166, 61, 71, 173, 56, 81, 72, 223, 41, 201, 132, 19, 220, 144, 51, 243, 245, 127, 142, 225, 267, 51, 249, 14, 249, 82, 14, 227, 104, 63, 98, 157, 140, 267, 37, 178, 250, 38, 61, 241, 37, 14, 235, 105, 104, 180, 237, 222, 56, 76, 251, 4, 159, 10, 262, 220, 101, 2, 29, 112, 72, 99, 268, 254, 117, 108, 243, 9, 180, 248, 26, 61, 201, 77, 13, 152, 123, 83, 190, 192, 109, 151, 221, 105, 11, 184, 104, 214, 191, 176, 218, 227, 147, 60, 68, 173, 46, 10, 61, 241, 5, 36, 191, 257, 264, 9, 232, 173, 252, 110, 50, 88, 113, 70, 205, 171, 235, 82, 235, 70, 106, 69, 220, 55, 38, 146, 239, 152, 98, 136, 71, 258, 190, 29, 208, 2, 268, 29, 27, 149, 62, 94, 102, 248, 212, 208, 152, 54, 190, 89, 204, 43, 53, 74, 37, 101, 128, 198, 160, 106, 206, 53, 134, 0, 112, 69, 142, 180, 164, 38, 20, 232, 4, 226, 16, 115, 132, 164, 92, 203, 243, 85, 6, 48, 80, 217, 27, 195, 80, 181, 80, 247, 177, 42, 22, 30, 62, 28, 186, 212, 78, 2, 99, 194, 29, 150, 5, 87, 26, 21, 184, 247, 249, 231, 165, 86, 22, 95, 82, 70, 217, 266, 112, 114, 23, 243, 122, 12, 165, 229, 199, 47, 124, 194, 84, 238, 218, 233, 188, 218, 195, 65, 173, 46, 78, 251, 20, 89, 100, 25, 173, 29, 98, 203, 84, 104, 231, 13, 41, 129, 76, 167, 170, 247, 29, 196, 195, 261, 148, 55, 188, 75, 139, 130, 32, 69, 12, 52, 45, 254, 24, 157, 39, 238, 69, 144, 87, 110, 83, 72, 51, 56, 152, 255, 124, 244, 77, 70, 79, 133, 6, 80, 181, 253, 130, 208, 81, 132, 160, 264, 209, 145, 78, 228, 177, 150, 261, 131, 9, 238, 263, 111, 239, 196, 179, 13, 119, 144, 131, 115, 254, 6, 197, 9, 125, 169, 97, 141, 64, 220, 45, 197, 43, 0, 38, 26, 53, 50, 92, 26, 40, 131, 220, 179, 214, 235, 57, 0, 156, 32, 54, 67, 257, 29, 243, 217, 195, 131, 101, 25, 257, 150, 16, 197, 144, 118, 51, 225, 8, 222, 269, 213, 77, 47, 234, 140, 28, 258, 254, 158, 149, 24, 138, 10, 204, 148, 10, 14, 10, 129, 52, 64, 242, 212, 222, 70, 264, 27, 26, 186, 236, 86, 201, 205, 9, 56, 82, 251, 63, 74, 182, 9, 54, 21, 9, 4, 1, 175, 74, 180, 194, 16, 242, 178, 149, 188, 29, 237, 35, 99, 156, 17, 117, 104, 151, 17, 120, 60, 19, 171, 60, 257, 32, 239, 169, 24, 262, 166, 240]

def userInput():
	print "Enter message to encrypt:"
	message = raw_input("")
	convertToRBG(message)


def convertToRBG(message):
	print "Your message is: " + message
	arrayOut = []
	passLen = len(message)
	i = 0
	while i <passLen:
		for i in range(passLen): #sorts through password
			
			for j in range(len(alphabet)): #sorts through alphabet
				if message[i] == alphabet[j]:
					arrayOut.append(numbers[j])

			i = i + 1

	arrayOut.append(255)
	print arrayOut
	encrypt(arrayOut)



def encrypt(toEncrypt): 
	prevSavedCounter = 0;
	enPointer = 0;
	encryptLen = len(toEncrypt)
	print "Password Length: " + str(encryptLen)

	for i in range(im.size[0]):   
	 	for j in range(im.size[1]):
	 		
	 		if j == prevSavedPts[prevSavedCounter]:
	 			if enPointer < encryptLen:
		 			r, g, b = rgb_im.getpixel((i, j))

		 			# print "Old: " + red + ", " + green + ", " + blue
		 			pixels[i,j+1] = (10,11,12)
		 			pixels[i,j] = (toEncrypt[enPointer], 255, 255) 
		 			enPointer = enPointer + 1
			
				r, g, b = rgb_im.getpixel((i, j))
	 			# print "Old: " + red + ", " + green + ", " + blue
	 			pixels[i,j+1] = (10,11,12)
	 			pixels[i,j] = (255, 255, 255) 
zA
	 	prevSavedCounter = prevSavedCounter + 1
 
	im.show()
	im.save(fileExt, 'png')
	print "File: " + str(fileExt)
	im.close()









userInput()

