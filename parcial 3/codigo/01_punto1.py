import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

img = np.array(Image.open("../images/mi_imagen.png").convert("RGB"))
print(img.shape, img.dtype)

# TODO: convertir img a escala de grises con rgb2gray
gray = None

# TODO: construir el negativo del mapa de color parula y graficar gray con él

# TODO: obtener la tripleta RGB del nivel 170 en el mapa de color
