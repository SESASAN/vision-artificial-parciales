import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

import sys
sys.path.append("..")
from colorspaces import rgb_to_cmyk, rgb_to_hsi

img = np.array(Image.open("../images/mi_imagen.png").convert("RGB"))
print(img.shape, img.dtype)

# TODO: mostrar los tres canales de img por separado

# TODO: convertir img a CMYK y mostrar cada componente

# TODO: convertir img a HSI y mostrar S, H e I por separado
