import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
from skimage.color import rgb2gray
from matplotlib.colors import ListedColormap

import sys
sys.path.append("..")
from colorspaces import PARULA

img = np.array(Image.open("../images/mi_imagen.png").convert("RGB"))
print(img.shape, img.dtype)

gray = np.round(rgb2gray(img) * 255).astype(np.uint8)

plt.figure()
plt.imshow(gray, cmap="gray", vmin=0, vmax=255)
plt.axis("off")
plt.savefig("../results/punto1_gris.png", bbox_inches="tight", pad_inches=0)

parula_negativa = ListedColormap(1.0 - PARULA)

plt.figure()
plt.imshow(gray, cmap=parula_negativa, vmin=0, vmax=255)
plt.axis("off")
plt.savefig("../results/punto1_parula_negativa.png", bbox_inches="tight", pad_inches=0)

indice = int(170 / 255 * len(PARULA))
tripleta = np.round(np.array(parula_negativa(170 / 255)[:3]) * 255).astype(int)
print(f"Índice {indice} de {len(PARULA)}, RGB = {tuple(int(v) for v in tripleta)}")
