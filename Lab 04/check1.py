# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:06:22 2021

@author: Nicole lee
"""
from PIL import Image 
im = Image.new('RGB', (200,200))
im = im.resize((512,512))
im1 = Image.open("ca.jpg").resize((256, 256))
im2 = Image.open("im.jpg").resize((256, 256))
im3 = Image.open("hk.jpg").resize((256, 256))
im4 = Image.open("bw.jpg").resize((256, 256))
im.paste(im1, (0,0))
im.paste(im2, (256,0))
im.paste(im3, (0,256))
im.paste(im4, (256,256))
im.show()