import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

img = np.array(Image.open("../images/mi_imagen.png").convert("RGB"))
print(img.shape, img.dtype)

plt.figure()
plt.imshow(img)
plt.axis("off")

laplaciano_4 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float64)

respuesta = cv2.filter2D(img.astype(np.float64), -1, laplaciano_4, borderType=cv2.BORDER_REPLICATE)
resultado = np.clip(img - respuesta, 0, 255).astype(np.uint8)

Image.fromarray(resultado).save("../results/punto7_transformada.png")

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(resultado)
plt.axis("off")
plt.savefig("../results/punto7_comparacion.png", bbox_inches="tight", pad_inches=0)
