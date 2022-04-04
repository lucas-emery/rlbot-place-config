import numpy as np
from PIL import Image


# RUN THIS BEFORE ADDING AN IMAGE

PATH = 'images/aphex.png'

color_map = {
    '#6D001A': 0,
    '#BE0039': 1,
    '#FF4500': 2,
    '#FFA800': 3,
    '#FFD635': 4,
    '#FFF8B8': 5,
    '#00A368': 6,
    '#00CC78': 7,
    '#7EED56': 8,
    '#00756F': 9,
    '#009EAA': 10,
    '#00CCC0': 11,
    '#2450A4': 12,
    '#3690EA': 13,
    '#51E9F4': 14,
    '#493AC1': 15,
    '#6A5CFF': 16,
    '#94B3FF': 17,
    '#811E9F': 18,
    '#B44AC0': 19,
    '#E4ABFF': 20,
    '#DE107F': 21,
    '#FF3881': 22,
    '#FF99AA': 23,
    '#6D482F': 24,
    '#9C6926': 25,
    '#FFB470': 26,
    '#000000': 27,
    '#515252': 28,
    '#898D90': 29,
    '#D4D7D9': 30,
    '#FFFFFF': 31
}


def rgb_to_hex(rgb):
    return ('#{:02X}{:02X}{:02X}'.format(rgb[0], rgb[1], rgb[2]))


try:
    data = Image.open(PATH)
    # convert png to np matrix
    image = np.asarray(data)
    height = image.shape[0]
    width = image.shape[1]
    matrix = np.zeros((height, width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            # if not transparent
            if image[i, j, 3] != 0:
                color = rgb_to_hex(image[i, j])
                if color not in color_map:
                    print('BROKEN IMAGE DO NOT COMMIT IT -', PATH)
                    exit()

    print('Image is valid -', PATH)
except:
    print('BROKEN IMAGE DO NOT COMMIT IT -', PATH)