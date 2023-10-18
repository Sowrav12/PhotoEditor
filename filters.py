# implemented all the necessary libraries

import numpy as np
import cv2 
from PIL import Image

# created all the filters 

def gray_filter(image, intensity):
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    filtered = cv2.addWeighted(gray, intensity, 0, 0, 0)
    return Image.fromarray(filtered)

def black_and_white_filter(image, intensity):
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    bandw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    filtered = cv2.addWeighted(bandw, intensity, 0, 0, 0)
    return Image.fromarray(filtered)

def pencil_sketch_filter(image, intensity):
    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (21, 21), 0, 0)
    pencil_sketch = cv2.divide(gray, blur, scale=256)
    filtered = cv2.addWeighted(pencil_sketch, intensity, 0, 0, 0)
    return Image.fromarray(filtered)

def blur_filter(image, intensity):
    img = np.array(image)
    blur = cv2.GaussianBlur(img, (21, 21), 0, 0)
    filtered = cv2.addWeighted(blur, intensity, 0, 0, 0)
    return Image.fromarray(filtered)

def invert_filter(image, intensity):
    img = np.array(image)
    inverted = 255 - img
    filtered = cv2.addWeighted(inverted, intensity, 0, 0, 0)
    return Image.fromarray(filtered)

# applied all the filters 

def apply_filter(filters, image, intensity):
    if filters == 'Gray Image':
        return gray_filter(image, intensity)
    elif filters == 'Black and White':
        return black_and_white_filter(image, intensity)
    elif filters == 'Pencil Sketch':
        return pencil_sketch_filter(image, intensity)
    elif filters == 'Blur Effect':
        return blur_filter(image, intensity)
    elif filters == 'Invert':
        return invert_filter(image, intensity)
    else:
        return Image.fromarray(np.array(image))
