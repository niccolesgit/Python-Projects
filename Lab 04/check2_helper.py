# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:51:20 2021

@author: Nicole Lee
"""
def make_square(image):
    size = image.size
    width = size[0]
    height = size[1]
    if size[0] > size[1]:
        image = image.crop((0,0,width,width)) #crop(left top right bottom)
        return image
    elif size[1] > size[0]:
        image = image.crop((0,0, height, height))
        return image
    else:
        image = image
        return image