import tkinter.messagebox

# Poner una mica con los colores RGB y hacer un AND con cada pixel
# El resultado es el pixel que hay que pintar.
def filtroRGB(imagen, otra, entradaR, entradaG, entradaB):
    if entradaR < 0 or entradaR > 255 or entradaG < 0 or entradaG > 255 or entradaB < 0 or entradaB > 255:
        tkinter.messagebox.showwarning("Error", "Ingresa valores validos.")
        return otra
    rgb = imagen.convert('RGB')
    pixeles = otra.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r, g, b = rgb.getpixel((i, j))
            pixeles[i, j] = (r & entradaR, g & entradaG, b & entradaB)
    return otra


