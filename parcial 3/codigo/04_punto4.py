import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
from skimage.color import rgb2yiq, yiq2rgb

img = np.array(Image.open("../images/mi_imagen.png").convert("RGB"))
print(img.shape, img.dtype)

plt.figure()
plt.imshow(img)
plt.axis("off")

yiq = rgb2yiq(img)
print(yiq.min(axis=(0, 1)).round(3), yiq.max(axis=(0, 1)).round(3))

y = np.round(np.clip(yiq[..., 0], 0, 1) * 255).astype(np.uint8)

y_gamma = np.zeros_like(y)
cv2.intensity_transform.gammaCorrection(y, y_gamma, 1.5)

q_mod = -yiq[..., 2]

yiq_mod = yiq.copy()
yiq_mod[..., 0] = y_gamma / 255.0
yiq_mod[..., 2] = q_mod
resultado = np.clip(np.round(yiq2rgb(yiq_mod) * 255), 0, 255).astype(np.uint8)

Image.fromarray(resultado).save("../results/punto4_transformada.png")

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(resultado)
plt.axis("off")
plt.savefig("../results/punto4_comparacion.png", bbox_inches="tight", pad_inches=0)
