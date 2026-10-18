import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

import sys
sys.path.append("..")
from colorspaces import rgb_to_cmy, cmy_to_rgb

img = np.array(Image.open("../images/mi_imagen.png").convert("RGB"))
print(img.shape, img.dtype)

plt.figure()
plt.imshow(img)
plt.axis("off")

# TODO
cmy = None

# TODO
y_mod = None

# TODO
resultado = None

# TODO: mostrar img y resultado lado a lado
