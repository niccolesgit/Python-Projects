# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 16:00:37 2021

@author: User
"""
from PIL import Image
from check2_helper import make_square
im = Image.new('RGB', (200,200))
im = im.resize((512,512))
im1 = Image.open("ca.jpg").resize((256, 256))
im2 = Image.open("im.jpg").resize((256, 256))
im3 = Image.open("hk.jpg").resize((256, 256))
im4 = Image.open("bw.jpg").resize((256, 256))

im1 = make_square(im1)
im2 = make_square(im2)
im3 = make_square(im3)
im4 = make_square(im4)

im.paste(im1, (0,0))
im.paste(im2, (256,0))
im.paste(im3, (0,256))
im.paste(im4, (256,256))
im.show()