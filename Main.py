#!/usr/bin/env python3
# -*- coding: utf-8 -*

from PIL import Image
import numpy as np

if __name__ == '__main__':
    print("Processamento de Imagens.")
    img = Image.open("img/lena-gray.png")
    img.show()
    lena = np.asarray(img.convert('L'))
    print(lena)
    print("Fim execução!!")
   