import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
from skimage.color import rgb2ycbcr, ycbcr2rgb

img = np.array(Image.open("../images/mi_imagen.png").convert("RGB"))
print(img.shape, img.dtype)

plt.figure()
plt.imshow(img)
plt.axis("off")

ycbcr = rgb2ycbcr(img)
print(ycbcr.min(axis=(0, 1)).round(1), ycbcr.max(axis=(0, 1)).round(1))

cr = np.round(ycbcr[..., 2]).astype(np.uint8)

cr_log = np.zeros_like(cr)
cv2.intensity_transform.logTransform(cr, cr_log)
cr_mod = cv2.bitwise_not(cr_log)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(cr, cmap="gray", vmin=0, vmax=255)
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(cr_mod, cmap="gray", vmin=0, vmax=255)
plt.axis("off")
plt.savefig("../results/punto3_cr.png", bbox_inches="tight", pad_inches=0)

ycbcr_mod = ycbcr.copy()
ycbcr_mod[..., 2] = cr_mod
resultado = np.clip(np.round(ycbcr2rgb(ycbcr_mod) * 255), 0, 255).astype(np.uint8)

Image.fromarray(resultado).save("../results/punto3_transformada.png")

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(resultado)
plt.axis("off")
plt.savefig("../results/punto3_comparacion.png", bbox_inches="tight", pad_inches=0)
