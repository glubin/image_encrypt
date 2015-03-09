from PIL import Image
import random
 
img = Image.open("sloth.jpg") # loads image
pixels = img.load() # create the pixel map

xlimit = 400
x = random.randint(0,xlimit)
 
for i in range(img.size[0]):   
 	for j in range(img.size[1]):
 		xcor = str(i)
 		ycor = str(j)
 		print str("X: " + xcor + " Y: " + ycor)

 		# check if random number x
 		if x == j:
 			pixels[i,j] = (255, 255, 255) 
 		
 	# change random number
 	x = random.randint(0,xlimit)
 		
 
img.show()
