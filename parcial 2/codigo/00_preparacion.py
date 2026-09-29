import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

import sys
sys.path.append("..")

img_path = "../images/mi_imagen.png"
img = np.array(Image.open(img_path).convert("RGB"))
print(img.shape, img.dtype)
plt.imshow(img)
plt.axis("off")
