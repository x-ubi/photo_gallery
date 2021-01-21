import numpy as np
from PIL import Image, ImageFilter


def crop(image_data, width, height, starting_x, starting_y):
    """Crop an image and return the cropped version.
    Keyword arguments:
    image_data -- numpy array of an image
    width -- desired width of the cropped image
    height -- desired height of the cropped image
    starting_x -- a starting point for the crop on the x axis
    starting_y -- a starting point for the crop on the y axis
    """
    cropped_image_data = image_data[starting_x:width, starting_y:height, :]
    cropped_image = Image.fromarray(cropped_image_data)
    return cropped_image


def rotate(image_data, times_to_rotate):
    """Rotate an image and return the rotated version.
    Keyword arguments:
    image_data -- numpy array of an image
    times_to_rotate -- how many times to rotate by 90 degrees
    """
    rotated_image_data = np.rot90(image_data, times_to_rotate)
    rotated_image = Image.fromarray(rotated_image_data)
    return rotated_image


def gaussianblur(image, chosen_r=2):
    """Blur an image and return the blurred version.
    Keyword arguments:
    image -- a PIL Image object that is to be blurred
    chosen_r -- radius of the gaussian blur (default 2)
    """
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=chosen_r))
    return blurred_image


def black_and_white(image):
    """Convert an image to black and white and return it.
    Keyword arguments:
    image -- a PIL Image object to convert
    """
    bw_image = image.convert('L')
    return bw_image
