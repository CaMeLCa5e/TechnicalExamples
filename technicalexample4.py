"""
4. Write a command line utility called gif2png that takes a single 
command line argument (the name of a GIF file), opens the GIF file, 
converts the image format to PNG and stores the converted image as a 
new PNG file in the current working directory. """



    
from PIL import Image
import glob
import os

files = glob.glob("*.gif") 

for imageFile in files:
    filepath, filename = os.path.split(imageFile)
    filterame,exts = os.path.splitext(filename)
    print "Processing: " + imageFile,filterame
    im = Image.open(imageFile)
    im.save( imageFile+'.png','PNG')
    
    
    
    
    
    
    
    
    
    
    
    
    
    