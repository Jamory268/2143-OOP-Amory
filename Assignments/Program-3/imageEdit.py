"""
Name: Jeron Amory
Class: 2143 OOP
Program 3
"""

from PIL import Image
# Imports image library stuff
import urllib, cStringIO
# Imports libs to read image from internet
import random
# Import sys so we can access argv for command line args
import sys


class imageEd(object):

    def __init__(self, img):
        self.image = img
        self.width, self.height = img.size
    

    def glass_effect(self, img, dist = 10)
        for i in range(dist, self.width - dist):
            for j in range(dist, self.height - dist):
                cc = (width  + i + distance % width)
                rr = (height + j + distance % height)
                c = img.get(cc, rr)
                self.img = img.set(i, j, c)
        return self.img
        
    
    def flip(self, img):
        for x in range(self.width / 2):
            for y in range(self.height):
                # swap pix and pix2
                pxl = getPixel(img, x, y)
                pxl2 = setPixel(img, width-1-x, y)
            return self.pxl2


    def blur(self, img):
        kernel = 10
        k = kernel * 2
        for i in range(kernel, width - kernel):
            for j in range(kernel, height - kernel):
                r = 0
                g = 0
                b = 0
                for x in range(-kernel, kernel):
                    for y in range(-kernel, kernel):
                        pixel = img.getpixel(i+x, j+y)
                        rTotal += pixel[0]
                        gTotal += pixel[1]
                        bTotal += pixel[2]
                    px = img.putpixel((i,j), (r//k), (g//k), (b//k))
                    r = 0
                    g = 0
                    b = 0
                return self.px
                                                

    def posterize(self, img, snap_value = 200):
        for pixel in range(self.width):
            for pixel in range(self.height):
                current = self.img.getpixel((x, y))
                r = current[0]
                g = current[1]
                b = current[2]
                if (r % snap_val) < (snap_val // 2):
                        r -= r%snap_val
                else:
                    r += (snap_val - r % snap)
                
                if (g % snap) < (snap_val // 2):
                    g -= g % snap_val
                else:
                    g += (snap_val - g % snap_val)

                if (b%snap_val) < (snap_val // 2):
                    b -= b%snap_val
                else:
                    b += (snap_val - b % snap_val)

                self.img.putpixel((x,y), (r,g,b))
        return self.img


    def solarize(self, img, threshold = 200):
        current = img
        for i in range(self.width):
            for j in range(self.height):
                rgb = self.img.getpixel((x, y))
                rgb2 = (255-rgb[0],255-rgb[1],255-rgb[2])
                if current > threshold:
                    self.img.putpixel((x,y),rgb2)
        return self.img

    def warhol(self, img, snap_value = 100):
        pass

    def __snap_color__(self,color,snap_val):
        color = int(color)
        m = color % snap_val
        if m < (snap_val // 2):
            color -= m
        else:
            color += (snap_val - m)

        return int(color)
        



