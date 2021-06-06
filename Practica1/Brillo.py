
# Pedimos un valor entre -255 y 255, este valor se le suma a cada componente del rgb de los pixeles.
# Si se pasa de 255, se pone 255, si vale menos de 0, se pone 0
def brillo(imagen, otra, entrada):
    rgb = imagen.convert('RGB')
    pixels = otra.load()
    if -255 <= entrada <= 255:
        for i in range(imagen.size[0]):
            for j in range(imagen.size[1]):
                r, g, b = rgb.getpixel((i, j))
                r = r + entrada
                g = g + entrada
                b = b + entrada
                r = min(max(r, 0), 255)
                g = min(max(g, 0), 255)
                b = min(max(b, 0), 255)
                pixels[i, j] = (r, g, b)
        return otra
    elif entrada < -255:
        for i in range(imagen.size[0]):
            for j in range(imagen.size[1]):
                pixels[i, j] = (0, 0, 0)
        return otra
    else:
        for i in range(imagen.size[0]):
            for j in range(imagen.size[1]):
                pixels[i, j] = (255, 255, 255)
        return otra
