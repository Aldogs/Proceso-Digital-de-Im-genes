# Pasamos la imagen a un tono de gris y sacamos el promedio de los valores rojo,verde y azul. Si este promedio es
# menor o igual a 127 ponemos cada pixel igual a 0. Si es mayor de 127 ponemos cada pixel igual a 255.
def contraste(imagen, otra):
    rgb = imagen.convert('RGB')
    pixels = otra.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r, g, b = rgb.getpixel((i, j))
            promedio = int(round(r*0.3+g*0.59+b*0.11))
            if promedio <= 127:
                promedio = 0
            elif promedio > 127:
                promedio = 255
            pixels[i, j] = (promedio, promedio, promedio)
    return otra
