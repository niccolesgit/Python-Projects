# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 10:48:52 2021

@author: User
"""
from PIL import Image
from check2_helper import make_square

im = Image.new('RGB', (1000,360))
im = im.resize((512,512))
im1 = Image.open("ca.jpg")
im2 = Image.open("im.jpg")
im3 = Image.open("hk.jpg")
im4 = Image.open("bw.jpg")
im5 = Image.open("hw.jpg")
im6 = Image.open("fl.jpg")

im1 = make_square(im1)
im2 = make_square(im2)
im3 = make_square(im3)
im4 = make_square(im4)
im5 = make_square(im5)
im6 = make_square(im6)

im1 = im1.resize()

im.paste(im1, (31,20))
im.paste(im2, (41,60))
im.paste(im3, (51,100))
im.paste(im4, (61,140))
im.paste(im5, (71,180))
im.paste(im5, (81,220))
im.show()