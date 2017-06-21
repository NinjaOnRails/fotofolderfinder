#! /usr/bin/env python3
# idPhotoFolders.py - Identifies all of the photo folders on the hard drive.

import os, sys
from PIL import Image

folder = sys.argv[1]

for folderName, subfolders, filenames in os.walk(folder):
    photoFiles = 0
    
    for filename in filenames:
        if filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.gif') or filename.lower().endswith('.bmp') or filename.lower().endswith('.jpeg'):
            Im = Image.open(os.path.join(folderName, filename))
            width, height = Im.size
            if width > 500 and height > 500:
                photoFiles += 1
    if photoFiles > len(filenames)/2:
        print('Photo folder found: %s' % folderName)
