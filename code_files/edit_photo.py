import numpy as np
from PIL import Image, ImageFilter


def crop(image_data, width, height, starting_x, starting_y):
    cropped_image_data = image_data[starting_x:width, starting_y:height, :]
    cropped_image = Image.fromarray(cropped_image_data)
    return cropped_image


def rotate(image_data, times_to_rotate):
    rotated_image_data = np.rot90(image_data, times_to_rotate)
    rotated_image = Image.fromarray(rotated_image_data)
    return rotated_image


def gaussianblur(image, chosen_r=2):
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius=chosen_r))
    return blurred_image


def black_and_white(image):
    bw_image = image.convert('L')
    return bw_image
