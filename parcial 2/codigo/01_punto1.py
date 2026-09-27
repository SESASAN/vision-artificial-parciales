import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

import sys
sys.path.append("..")

img = np.array(Image.open("../images/mi_imagen.png").convert("RGB"))
gray = np.array(Image.fromarray(img).convert("L"))

plt.imshow(gray, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto1_gris.png", bbox_inches="tight", pad_inches=0)

hist = cv2.calcHist([gray], [0], None, [256], [0, 256]).flatten()

plt.figure()
plt.plot(hist)
plt.xlabel("Nivel de intensidad")
plt.ylabel("Numero de pixeles")
plt.savefig("../results/punto1_histograma_gris.png", bbox_inches="tight")

gray_eq = cv2.equalizeHist(gray)

plt.figure()
plt.imshow(gray_eq, cmap="gray")
plt.axis("off")
plt.savefig("../results/punto1_ecualizada.png", bbox_inches="tight", pad_inches=0)

hist_eq = cv2.calcHist([gray_eq], [0], None, [256], [0, 256]).flatten()

plt.figure()
plt.plot(hist_eq)
plt.xlabel("Nivel de intensidad")
plt.ylabel("Numero de pixeles")
plt.savefig("../results/punto1_histograma_ecualizado.png", bbox_inches="tight")

nivel_gris = int(np.argmax(hist))
prob_gris = hist[nivel_gris] / gray.size * 100
print(f"Nivel: {nivel_gris}")
print(f"Probabilidad: {prob_gris:.2f}%")

nivel_eq = int(np.argmax(hist_eq))
prob_eq = hist_eq[nivel_eq] / gray_eq.size * 100
print(f"Nivel: {nivel_eq}")
print(f"Probabilidad: {prob_eq:.2f}%")

prob_176 = hist_eq[176] / gray_eq.size * 100
print(f"Probabilidad de intensidad 176: {prob_176:.4f}%")
