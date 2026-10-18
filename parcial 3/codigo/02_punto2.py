import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

import sys
sys.path.append("..")
from colorspaces import rgb_to_cmyk, rgb_to_hsi

img = np.array(Image.open("../images/mi_imagen.png").convert("RGB"))
print(img.shape, img.dtype)

plt.figure()
plt.imshow(img)
plt.axis("off")

for indice, nombre in enumerate(["R", "G", "B"]):
    plt.figure()
    plt.imshow(img[..., indice], cmap="gray", vmin=0, vmax=255)
    plt.axis("off")
    plt.savefig(f"../results/punto2_{nombre}.png", bbox_inches="tight", pad_inches=0)

cmyk = rgb_to_cmyk(img)

for indice, nombre in enumerate(["C", "M", "Y", "K"]):
    plt.figure()
    plt.imshow(cmyk[..., indice], cmap="gray", vmin=0, vmax=1)
    plt.axis("off")
    plt.savefig(f"../results/punto2_{nombre}.png", bbox_inches="tight", pad_inches=0)

hsi = rgb_to_hsi(img)

for indice, nombre in [(1, "saturacion"), (0, "tono"), (2, "intensidad")]:
    plt.figure()
    plt.imshow(hsi[..., indice], cmap="gray", vmin=0, vmax=1)
    plt.axis("off")
    plt.savefig(f"../results/punto2_{nombre}.png", bbox_inches="tight", pad_inches=0)
