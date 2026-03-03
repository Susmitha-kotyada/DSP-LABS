#1 converting image into matrix
'''
from PIL import Image
import numpy as np
#load the image
img=Image.open('C:/Users/kotya/OneDrive/Documents/mine.jpg')
#converting to rgb
img=img.convert('RGB')
#converting to matrix
img_matrix=np.array(img)
#display matrix shape
print('image shape(row,column,RGB):',img_matrix.shape)
#display first 5*5 pixels
print(img_matrix[:5,:5])
img.show()
'''
#2 
