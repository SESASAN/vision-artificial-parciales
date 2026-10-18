import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

import sys
sys.path.append("..")
from colorspaces import rgb_to_hsi, hsi_to_rgb

img = np.array(Image.open("../images/mi_imagen.png").convert("RGB"))
print(img.shape, img.dtype)

plt.figure()
plt.imshow(img)
plt.axis("off")

hsi = rgb_to_hsi(img)

intensidad = np.round(hsi[..., 2] * 255).astype(np.uint8)
intensidad_eq = cv2.equalizeHist(intensidad)

hsi_eq = hsi.copy()
hsi_eq[..., 2] = intensidad_eq / 255.0
resultado = hsi_to_rgb(hsi_eq)

Image.fromarray(resultado).save("../results/punto6_transformada.png")

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(resultado)
plt.axis("off")
plt.savefig("../results/punto6_comparacion.png", bbox_inches="tight", pad_inches=0)
