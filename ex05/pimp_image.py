import numpy as np
from PIL import Image


def ft_invert(array):
    """Inverts the color of the image received."""
    inverted = 255 - array
    Image.fromarray(inverted).show()
    return inverted


def ft_red(array):
    """Prints the image in red scale."""
    red_channel = array[:, :, 0]
    image = np.zeros_like(array)
    image[:, :, 0] = red_channel
    Image.fromarray(image).show()
    return image


def ft_green(array):
    """Prints the image in green scale."""
    green_channel = array[:, :, 1]
    image = np.zeros_like(array)
    image[:, :, 1] = green_channel
    Image.fromarray(image).show()
    return image


def ft_blue(array):
    """Prints the image in blue scale."""
    blue_channel = array[:, :, 2]
    image = np.zeros_like(array)
    image[:, :, 2] = blue_channel
    Image.fromarray(image).show()


def ft_grey(array):
    """Prints the image in gray scale."""
    red_channel = array[:, :, 0] / 3
    green_channel = array[:, :, 1] / 3
    blue_channel = array[:, :, 2] / 3
    rgb = [red_channel, green_channel, blue_channel]
    grey_channel = sum(rgb)
    grey_image = np.stack([grey_channel, grey_channel, grey_channel], axis=2)
    Image.fromarray(grey_image.astype(np.uint8)).show()
