from PIL import Image


class Imagen:

    # Constructor de la clase Imagen
    def __init__(self, ruta):
        size = 500, 500
        self.imagen = Image.open(ruta)
        self.otra = Image.open(ruta)
        self.imagen.thumbnail(size, Image.LANCZOS)
        self.otra.thumbnail(size, Image.LANCZOS)

    # Funcion para obtener la imagen original
    def getImagen(self):
        return self.imagen

    # Funcion para obtener la imagen a la que se le aplicara el filtro
    def getOtra(self):
        return self.otra
