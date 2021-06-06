import tkinter.messagebox


# Recibe dos valores, mosaicoX y mosaicoY que definen que tan grande seran los mosaicos, se recorre la imagen con
# estos valores. En cada mosaico sacamos el promedio de los valores rojo, verde y azul de cada pixel, con esto se
# aplica ese valor a cada componente de los pixeles del mosaico
def mosaico(imagen, otra, mosaicoX, mosaicoY):
    if mosaicoX < 1 or mosaicoY < 1:
        tkinter.messagebox.showwarning("Error", "El valor ingresado no es valido")
        return otra
    promedio = 0
    rprom = 0
    gprom = 0
    bprom = 0
    rgb = imagen.convert('RGB')
    pixeles = otra.load()
    for i in range(0, imagen.size[0], mosaicoX):
        recorreX = i + mosaicoX
        for j in range(0, imagen.size[1], mosaicoY):
            recorreY = j + mosaicoY
            for k in range(i, recorreX):
                if k >= imagen.size[0]:
                    break
                for l in range(j, recorreY):
                    if l >= imagen.size[1]:
                        break
                    r, g, b = rgb.getpixel((k, l))
                    rprom += r
                    gprom += g
                    bprom += b
                    promedio += 1
            promRojo = int(rprom / promedio)
            promVerde = int(gprom / promedio)
            promAzul = int(bprom / promedio)
            rprom = 0
            gprom = 0
            bprom = 0
            promedio = 0
            for k in range(i, recorreX):
                if k >= imagen.size[0]:
                    break
                for l in range(j, recorreY):
                    if l >= imagen.size[1]:
                        break
                    pixeles[k, l] = (promRojo, promVerde, promAzul)

    return otra
