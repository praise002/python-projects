from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import matplotlib_inline

#Reading
image = Image.open("cat.jpeg")

#Displaying
# image.show()  #this opens photo viewer
# plt.imshow(image)  #plots d image in axis

#Displaying properties of an image
print(image.size)  #prints size of image in a tuple, width by height
print(image.format)  #JPEG
print(image.mode)  #RGB

#Saving
# image.save("cat2.jpg")

#Cropping
left = 50
top = 120
right = 250
bottom = 230
crop_image = image.crop((left, top, right, bottom))
plt.imshow(crop_image)
crop_image.show()

#Copying
copied_image = image.copy()
# copied_image.show()

#Transposing