import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
from skimage.exposure import match_histograms

import sys
sys.path.append("..")

ref = np.array(Image.open("../images/Referencia.tif").convert("L"))
plt.imshow(ref, cmap="gray")
plt.axis("off")

hist_ref = cv2.calcHist([ref], [0], None, [256], [0, 256]).flatten()

plt.figure()
plt.plot(hist_ref)
plt.xlabel("Nivel de intensidad")
plt.ylabel("Numero de pixeles")
plt.savefig("../results/punto2_histograma_referencia.png", bbox_inches="tight")

img = np.array(Image.open("../images/mi_imagen.png").convert("RGB"))
gray = np.array(Image.fromarray(img).convert("L"))

gray_spec = match_histograms(gray, ref).astype(np.uint8)

plt.figure()
plt.imshow(gray_spec, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto2_especificacion.png", bbox_inches="tight", pad_inches=0)

hist_spec = cv2.calcHist([gray_spec], [0], None, [256], [0, 256]).flatten()

plt.figure()
plt.plot(hist_spec)
plt.xlabel("Nivel de intensidad")
plt.ylabel("Numero de pixeles")
plt.savefig("../results/punto2_histograma_especificacion.png", bbox_inches="tight")
