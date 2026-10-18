import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

import sys
sys.path.append("..")
from colorspaces import rgb_to_cmy, cmy_to_rgb, rgb_to_cmyk, cmyk_to_rgb, rgb_to_hsi, hsi_to_rgb

img_original = np.array(Image.open("../images/mi_imagen_original.png").convert("RGB"))
print(img_original.shape, img_original.dtype)

alto, ancho = img_original.shape[:2]
lado = min(alto, ancho)
y0 = (alto - lado) // 2
x0 = (ancho - lado) // 2
cuadrada = img_original[y0:y0 + lado, x0:x0 + lado, :]

img = cv2.resize(cuadrada, (1024, 1024), interpolation=cv2.INTER_CUBIC)
Image.fromarray(img).save("../images/mi_imagen.png")
assert img.shape == (1024, 1024, 3), img.shape
print(img.shape, img.dtype)

plt.figure()
plt.imshow(img)
plt.axis("off")

# TODO: ida y vuelta por cada espacio y SSIM contra img
