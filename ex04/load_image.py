from PIL import Image
import numpy as np


def ft_load(path: str):
    """cargame la imagen de tu puta madre"""
    try:
        assert path[-4:] == '.jpg' or path[-5:] == '.jpeg', "invalid format"
        pixels = np.array(Image.open(path))
        print(f"The shape of the image is {pixels.shape}")
        return pixels
    except PermissionError as pe:
        print(f"{type(pe).__name__}: {pe}")
    except FileNotFoundError as fnfe:
        print(f"{type(fnfe).__name__}: {fnfe}")
    except AssertionError as ae:
        print(f"{type(ae).__name__}: {ae}")
