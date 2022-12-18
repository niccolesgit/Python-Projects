# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 10:21:00 2021

@author: User
"""
from PIL import Image
im = Image.new('RGB', (200,200))
im2 = im.crop((0,0,200,200))
im2.show()

                   