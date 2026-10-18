import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

import sys
sys.path.append("..")
from colorspaces import rgb_to_cmy, cmy_to_rgb

desbalanceada = np.array(Image.open("../images/imagen_desbalanceada.tiff").convert("RGB"))
objetivo = np.array(Image.open("../images/imagen_objetivo.tiff").convert("RGB"))
print(desbalanceada.shape, objetivo.shape)

# TODO: analizar los canales de desbalanceada vs objetivo

# TODO
corregida = None

from skimage.metrics import structural_similarity as ssim

# TODO: calcular el SSIM entre corregida y objetivo
