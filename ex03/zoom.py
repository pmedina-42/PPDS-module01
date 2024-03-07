from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def zoom(path: str):
    """hazle zoom a tu puta madre"""
    try:
        img_array = ft_load(path)
        print(img_array)
        chopchop = img_array[100:500, 450:850]
        zoomzoom = np.array(Image.fromarray(chopchop).convert('L'))
        print(f"New shape after slicing: {zoomzoom.shape}")
        print(zoomzoom)
        plt.imshow(zoomzoom, cmap='gray')
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """main otra vez de tu puta madre"""
    try:
        zoom("animal.jpeg")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == '__main__':
    """main de tu puta madre"""
    main()
