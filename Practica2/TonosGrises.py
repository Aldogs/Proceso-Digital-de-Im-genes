# En este metodo simplemente sumamos los tres colores y lo dividimos entre 3. Damos ese valor cada pixel
def gris1(imagen, otra):
    rgb = imagen.convert('RGB')
    pixeles = otra.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r, g, b = rgb.getpixel((i, j))
            gris = int(round((r + g + b) / 3))
            pixeles[i, j] = (gris, gris, gris)
    return otra


# Damos gris como rojo*.3 + verde *.59 + azul *.11
def gris2(imagen, otra):
    rgb = imagen.convert('RGB')
    pixeles = otra.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r, g, b = rgb.getpixel((i, j))
            gris = int(round(r * 0.3 + g * 0.59 + b * 0.11))
            pixeles[i, j] = (gris, gris, gris)
    return otra


# Damos gris como rojo*.2126 + verde *.7152 + azul *.0722
def gris3(imagen, otra):
    rgb = imagen.convert('RGB')
    pixeles = otra.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r, g, b = rgb.getpixel((i, j))
            gris = int(round(r * 0.2126 + g * 0.7152 + b * 0.0722))
            pixeles[i, j] = (gris, gris, gris)
    return otra


# Desaturacion
def gris4(imagen, otra):
    rgb = imagen.convert('RGB')
    pixeles = otra.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r, g, b = rgb.getpixel((i, j))
            gris = int(round((max(r, g, b) + min(r, g, b)) / 2))
            pixeles[i, j] = (gris, gris, gris)
    return otra


# descomposición máxima
def gris5(imagen, otra):
    rgb = imagen.convert('RGB')
    pixeles = otra.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r, g, b = rgb.getpixel((i, j))
            gris = int(round((max(r, g, b))))
            pixeles[i, j] = (gris, gris, gris)
    return otra


# descomposición mínima
def gris6(imagen, otra):
    rgb = imagen.convert('RGB')
    pixeles = otra.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r, g, b = rgb.getpixel((i, j))
            gris = int(round((min(r, g, b))))
            pixeles[i, j] = (gris, gris, gris)
    return otra


# rojo
def gris7(imagen, otra):
    rgb = imagen.convert('RGB')
    pixeles = otra.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r, g, b = rgb.getpixel((i, j))
            pixeles[i, j] = (r, r, r)
    return otra


# verde
def gris8(imagen, otra):
    rgb = imagen.convert('RGB')
    pixeles = otra.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r, g, b = rgb.getpixel((i, j))
            pixeles[i, j] = (g, g, g)
    return otra


# azul
def gris9(imagen, otra):
    rgb = imagen.convert('RGB')
    pixeles = otra.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r, g, b = rgb.getpixel((i, j))
            pixeles[i, j] = (b, b, b)
    return otra
