# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 10:36:14 2021

@author: Nicole Lee
"""
import wikimedia
from PIL import Image 
from check2_helper import make_square
search = input('Please enter a query: ')
images = wikimedia.find_images(search,2) 
im = Image.new('RGB', (512,512))
num = len(images) 
print("Your query returned {} images".format(num)) 
if num < 2:
    print("Error not enough images returned")
else:
    im.paste(make_square((images[0].resize((256, 256)))), (0,0))
    im.paste(make_square(images[1].resize((256, 256))), (0, 256))
    im.show()