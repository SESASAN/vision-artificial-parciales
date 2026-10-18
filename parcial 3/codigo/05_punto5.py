import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

import sys
sys.path.append("..")
from colorspaces import rgb_to_cmy, cmy_to_rgb

img = np.array(Image.open("../images/mi_imagen.png").convert("RGB"))
print(img.shape, img.dtype)

plt.figure()
plt.imshow(img)
plt.axis("off")

cmy = rgb_to_cmy(img)

amarillo = np.round(cmy[..., 2] * 255).astype(np.uint8)

amarillo_mod = np.zeros_like(amarillo)
cv2.intensity_transform.contrastStretching(amarillo, amarillo_mod, 80, 60, 210, 120)

cmy_mod = cmy.copy()
cmy_mod[..., 2] = amarillo_mod / 255.0
resultado = cmy_to_rgb(cmy_mod)

Image.fromarray(resultado).save("../results/punto5_transformada.png")

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(resultado)
plt.axis("off")
plt.savefig("../results/punto5_comparacion.png", bbox_inches="tight", pad_inches=0)
