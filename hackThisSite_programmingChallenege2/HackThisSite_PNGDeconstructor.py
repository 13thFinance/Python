#converts a black and white png image from hackthissite.org programming challenge 2
#into morse which then is translated to english

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from morseCode import *
import string
import os

filename = 'PNG'

img = Image.open( filename + '.png' )
data = np.array( img, dtype='uint8' )

#print all data
print("Data is of type: ", type(data))
temp = True
for array in data:
	if temp == True:
		print("Array is of type: ", type(array))
		print("Array elements are of type: ", type(array[0]))
		temp = False
	#print (array)

xMax = data.shape[1] #30
yMax = data.shape[0] #100
print("Image size: x: ", xMax, " y: ", yMax)

i = 0
j = 0

ascii_list = []

counter = 0
countTilNextDot = []


while i < 30:
	while j < 100:
		#print(data[i,j], " ", end='')
		if data[i,j] == 1:
			ascii_list.append([i, j])
			countTilNextDot.append(counter)
			counter = 0
		counter += 1
		j += 1
	i += 1
	j = 0

print(ascii_list)
print("\n\n")
print(countTilNextDot)

morse = []

#translate dot pattern from morse into text
for i in countTilNextDot:
	morse.append(chr(i))
print(morse)

code = Morse()
print(type(code))
code.printAlphanumeric()
print()
translation = code.translateBrokenString(morse)

translation = ''.join(translation)

print(translation)


os.system("pause")


#np.save( filename + '.npy', data)

# visually testing our output
#img_array = np.load(filename + '.npy')
#plt.imshow(img_array) 
