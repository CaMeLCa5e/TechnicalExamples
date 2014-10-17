
"""
4. Write a command line utility called gif2png that takes a single 
command line argument (the name of a GIF file), opens the GIF file, 
converts the image format to PNG and stores the converted image as a 
new PNG file in the current working directory. """

# - For #4, make sure you have "include Image" at the top. Also make
# sure you open the .gif first using the Image library, then save it as
# .png. Otherwise the Image library doesn't have data to save.

# 
 
# import glob
# import os
# 
# files = glob.glob("gopher2.gif")
# 
# for imageFile in files:
# 	
# 	filepath, filename =  os.path.split(imageFile)
# 	
# 	filtername, exts = os.path.splitext(filename)
# 	
# 	im = Image.open(imageFile)
# 	im.save ("" +filtername+'.png', PNG)

# im = Image.open('gopher2.gif')
# transparency = im.info['transparency']
# imsave('icon.gif', transparency = transparency)



    
from pillow import Image
import glob
import os

files = glob.glob("dir/*.gif") 

for imageFile in files:
    filepath, filename = os.path.split(imageFile)
    filterame,exts = os.path.splitext(filename)
    print "Processing: " + imageFile,filterame
    im = Image.open(imageFile)
    im.save( 'dir_/'+new_file+'.png','PNG')
    
    
    
    