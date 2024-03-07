from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def rotate(path: str):
    """rotame esta"""
    img_array = ft_load(path)
    print(img_array)
    chopchop = img_array[100:500, 450:850]
    zoomzoom = np.array(Image.fromarray(chopchop).convert('L'))
    swoop = [list(i) for i in zip(*zoomzoom)]
    plt.imshow(swoop, cmap='gray')
    plt.show()


def main():
    """main otra vez de tu puta madre"""
    try:
        rotate("animal.jpeg")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == '__main__':
    """main de tu puta madre"""
    main()
