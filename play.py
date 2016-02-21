#!/usr/bin/python

import cv2
from alpr import Alpr
from pprint import pprint
import sys

v = cv2.VideoCapture(sys.argv[1])
width = 800
skip = 10
a = Alpr()
n = 0

def convert2pnm(im):
    # get image dimensions
    height, width, depth = (im.shape + (1,))[0:3]
    # P5 and P6 are the magic numbers for PGM and PPM formats, respectively 
    if depth == 3:
        # convert image from BRG to RGB (pnm uses RGB)
        im2 = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        format_ = "P6"
    elif depth == 1:
        # GRAY image, do nothing
        im2 = im
        format_ = "P5"
    else:
        return

    # and 255 is the max color allowed, see http://en.wikipedia.org/wiki/Netpbm_format#File_format_description        
    return "%s %d %d 255 " % (format_, width, height) + im2.tostring()

if __name__ == "__main__":
    if v.isOpened():
        rval, frame = v.read()
    else:
        rval = False
    while rval:
        # recognize 
        if n%skip == 0:
            result = a.recognize_array(convert2pnm(frame))
            for r in result['results']:
                pprint(r['plate'])
                cv2.imshow(r['plate'], frame)

        # resize
        factor = frame.shape[1] / float(width)
        height = int(frame.shape[0]/factor)
        resized = cv2.resize(frame, (width, height))
        # show resized frame
        cv2.imshow("video", resized)
        # capture quit key
        key = cv2.waitKey(1)
        if key == 27:
            break

        # next
        rval, frame = v.read()
        n += 1
        #print n
    
v.release()
