#! /usr/bin/env python
# -*- coding:utf-8 -*-

import Image
import sys
import os


###############################################################################
if len(sys.argv) == 1 or '--help' in sys.argv:
    print """ Please use next syntax:
    im_to_ascii.py full_path_to_jpg [rezolution, default 128]"""

    sys.exit()

path_to_JPG_image = sys.argv[1]

if len(sys.argv) == 3:
    rezolution = int(sys.argv[2])
else:
    rezolution = 128

path_to_save_ACSII_image, image_JPEG_name = os.path.split(path_to_JPG_image)
#print path_to_save_ACSII_image, image_JPEG_name

###############################################################################


def get_proportion(w, h, rezolution):
    """ Return new proportion (w, h)."""
    large_side = rezolution
    k = float(w) / float(h)
    if w > h:
        w_prop = large_side
        h_prop = int(w_prop / k)
    elif w < h:
        h_prop = large_side
        w_prop = int(h_prop * k)
    else:
        h_prop = w_prop = large_side
    return (w_prop, h_prop)
###############################################################################


def return_hex(color):
    hex_color = hex(color)[2:]
    if len(hex_color) != 2:
        hex_color = hex_color.zfill(2)
    return hex_color


def get_color(im_obj):
    """
    Return ACSII image
    # Gray scale
    #   0 -  16 #
    #  17 -  32 M
    #  33 -  48 @
    #  49 -  64 H
    #  65 -  80 X
    #  81 -  96 $
    #  97 - 112 %
    # 113 - 128 +
    # 129 - 144 /
    # 145 - 160 ;
    # 161 - 176 :
    # 177 - 192 =
    # 193 - 208 -
    # 209 - 224 ,
    # 225 - 240 .
    # 241 - 256
    """
    #im = Image.open(path, 'r')
    ascii_pic = open(os.path.join(path_to_save_ACSII_image, 'ACSII_' +
    image_JPEG_name[:-4] + '.html'), 'w')
#    ascii_pic.write('<font face="Courier New">') #"Courier New"
    x, y = im_obj.size
#    print x, y
    pixel = ' '
    ascii_pic.write('<body bgcolor="#FFFFFF"><PRE><br>')

    for i in xrange(y):
        for j in xrange(x):
            colors = im_obj.getpixel((j, i))
            r, g, b = colors
            color_px = sum((int(r), int(g), int(b))) / 3
            print color_px
            r = return_hex(r)
            g = return_hex(g)
            b = return_hex(b)

            if 0 <= color_px <= 16:
                pixel = '<FONT COLOR=#%s%s%s>%s</FONT COLOR>' % (r, g, b, '#')
            elif 17 <= color_px <= 32:
                pixel = '<FONT COLOR=#%s%s%s>%s</FONT COLOR>' % (r, g, b, 'M')
            elif 33 <= color_px <= 48:
                pixel = '<FONT COLOR=#%s%s%s>%s</FONT COLOR>' % (r, g, b, '@')
            elif 49 <= color_px <= 64:
                pixel = '<FONT COLOR=#%s%s%s>%s</FONT COLOR>' % (r, g, b, 'H')
            elif 65 <= color_px <= 80:
                pixel = '<FONT COLOR=#%s%s%s>%s</FONT COLOR>' % (r, g, b, 'X')
            elif 81 <= color_px <= 96:
                pixel = '<FONT COLOR=#%s%s%s>%s</FONT COLOR>' % (r, g, b, '$')
            elif 97 <= color_px <= 112:
                pixel = '<FONT COLOR=#%s%s%s>%s</FONT COLOR>' % (r, g, b, '%')
            elif 113 <= color_px <= 128:
                pixel = '<FONT COLOR=#%s%s%s>%s</FONT COLOR>' % (r, g, b, '+')
            elif 129 <= color_px <= 144:
                pixel = '<FONT COLOR=#%s%s%s>%s</FONT COLOR>' % (r, g, b, '/')
            elif 145 <= color_px <= 160:
                pixel = '<FONT COLOR=#%s%s%s>%s</FONT COLOR>' % (r, g, b, ';')
            elif 161 <= color_px <= 176:
                pixel = '<FONT COLOR=#%s%s%s>%s</FONT COLOR>' % (r, g, b, ':')
            elif 177 <= color_px <= 192:
                pixel = '<FONT COLOR=#%s%s%s>%s</FONT COLOR>' % (r, g, b, '=')
            elif 193 <= color_px <= 208:
                pixel = '<FONT COLOR=#%s%s%s>%s</FONT COLOR>' % (r, g, b, '-')
            elif 209 <= color_px <= 224:
                pixel = '<FONT COLOR=#%s%s%s>%s</FONT COLOR>' % (r, g, b, ',')
            elif 225 <= color_px <= 240:
                pixel = '<FONT COLOR=#%s%s%s>%s</FONT COLOR>' % (r, g, b, '.')
            elif 241 <= color_px <= 256:
                pixel = ' '
            else:
                print 'ERROR'

            ascii_pic.write(pixel * 3)
            #print pixel,

            if j == x - 1:
                ascii_pic.write('\n')
                print ''

            #print pixel

    ascii_pic.write('</PRE>')
    ascii_pic.close()

    return True

###############################################################################

im_rgb = Image.open(path_to_JPG_image)
w, h = im_rgb.size

im_resize = im_rgb.resize(get_proportion(w, h, rezolution), 0)

#im_gray_scale = im_resize.convert('L')

get_color(im_resize)

#im_gray_scale.save(os.path.join(path_to_save_ACSII_image,
#'ACSII_' + image_JPEG_name), 'JPEG')


