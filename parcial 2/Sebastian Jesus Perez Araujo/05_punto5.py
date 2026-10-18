import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

def convolucion(im, kernel):
    kernel_flip = kernel[::-1, ::-1]
    return cv2.filter2D(im, -1, kernel_flip, borderType=cv2.BORDER_REPLICATE)

img = np.array(Image.open("../images/mi_imagen.png").convert("RGB"))
gray = np.array(Image.fromarray(img).convert("L")).astype(np.float64)

laplaciano_4 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float64)

respuesta_4 = convolucion(gray, laplaciano_4)
realce_4 = np.clip(gray - respuesta_4, 0, 255).astype(np.uint8)

plt.imshow(realce_4, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_realce_4vecinos.png", bbox_inches="tight", pad_inches=0)

laplaciano_8 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]], dtype=np.float64)

respuesta_8 = convolucion(gray, laplaciano_8)
realce_8 = np.clip(gray - respuesta_8, 0, 255).astype(np.uint8)

plt.imshow(realce_8, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto5_realce_8vecinos.png", bbox_inches="tight", pad_inches=0)
