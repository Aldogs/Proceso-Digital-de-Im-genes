from PIL import ImageTk
from tkinter import filedialog
from tkinter import *
from Brillo import *
from Imagen import *
from Mosaico import *
from TonosGrises import *

import tkinter.messagebox
import os


class Interfaz(Frame):
    # Variable global que usaremos para crear un objeto de la clase Imagen
    global image

    # Constructor de la clase
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True)
        self.imagen = None
        self.otra = None
        self.creaCanvas()
        self.creaMenu()

    # Crea las pestañas del menu
    def creaMenu(self):
        self.menuBar = Menu(self)

        self.archivoMenu = Menu(self.menuBar, tearoff=0)
        self.archivoMenu.add_command(label="Abrir", command=self.escogerImagen)
        self.archivoMenu.add_command(label="Guardar", command=self.preguntaGuardar)
        self.archivoMenu.add_command(label="Salir", command=self.salir)
        self.menuBar.add_cascade(label="Imagen", menu=self.archivoMenu)

        self.filtroMenu = Menu(self.menuBar, tearoff=0)
        self.filtroMenu.add_command(label="Brillo", command=self.aplicaBrillo)
        self.filtroMenu.add_command(label="Mosaico", command=lambda: self.aplicaMosaico(1))
        self.tonosGris = Menu(self.filtroMenu, tearoff=0)
        self.tonosGris.add_command(label="Gris 1", command=lambda: self.aplicaFiltro(1))
        self.tonosGris.add_command(label="Gris 2", command=lambda: self.aplicaFiltro(2))
        self.tonosGris.add_command(label="Gris 3", command=lambda: self.aplicaFiltro(3))
        self.tonosGris.add_command(label="Gris 4", command=lambda: self.aplicaFiltro(4))
        self.tonosGris.add_command(label="Gris 5", command=lambda: self.aplicaFiltro(5))
        self.tonosGris.add_command(label="Gris 6", command=lambda: self.aplicaFiltro(6))
        self.tonosGris.add_command(label="Gris 7", command=lambda: self.aplicaFiltro(7))
        self.tonosGris.add_command(label="Gris 8", command=lambda: self.aplicaFiltro(8))
        self.tonosGris.add_command(label="Gris 9", command=lambda: self.aplicaFiltro(9))
        self.filtroMenu.add_cascade(label="Tonos de Grises", menu=self.tonosGris)
        self.rgb = Menu(self.filtroMenu, tearoff=0)
        self.menuBar.add_cascade(label="Filtros", menu=self.filtroMenu)

        root.config(menu=self.menuBar)

        # Se crea el canvas derecho e izquierdo

    def creaCanvas(self):
        self.originalVentana = Canvas(self, bg="white", width=500, height=500)
        self.originalVentana.pack(side=TOP, fill=BOTH, expand=True)

        # Cierra el programa

    def salir(self):
        os._exit(0)

        # Pregunta al usuario el nombre a guardar

    def preguntaGuardar(self):
        if self.originalVentana.find_all() != ():
            self.top = Toplevel()

            self.label = Label(self.top,
                               text="Para guardar la imagen tienes que poner el nombre que le quieras poner seguido del formato de la imagen original.\n Ej: Si abriste \"perrito.jpeg\" puedes guardar la nueva imagen como \"perritonuevo.jpeg\"")
            self.label.pack()

            self.buttontext = StringVar()
            self.buttontext.set("Entendido, quiero guardar")
            self.button = Button(self.top, textvariable=self.buttontext, command=self.guardarImagen).pack()
        else:
            tkinter.messagebox.showwarning("Error", "No hay imagen")

            # Guarda la nueva imagen

    def guardarImagen(self):
        try:
            self.nuevaImagen.save(filedialog.asksaveasfilename())
        except AttributeError:
            tkinter.messagebox.showwarning("Error",
                                           "No puedes guardar una imagen en la que no se haya aplicado algún filtro")
        except ValueError:
            tkinter.messagebox.showwarning("Error", "Formato no valido, la imagen no se ha guardado")
        finally:
            self.top.destroy()

        # TODO: convertir tamaño de canvas a tamaño de imagen o viceversa
        # Abre la imagen en ambos canvas

    def escogerImagen(self):
        ruta = filedialog.askopenfilename()
        image = Imagen(ruta)
        self.imagen = image.getImagen()
        self.otra = image.getOtra()

        imageFile = ImageTk.PhotoImage(self.imagen)
        imageOtra = ImageTk.PhotoImage(self.otra)

        self.originalVentana.image = imageFile
        self.originalVentana.create_image(imageFile.width() / 2, imageFile.height() / 2, anchor=CENTER, image=imageFile,
                                          tags="bg_img")

        # Selecciona el filtro que le aplicaremos a la nueva imagen

    def aplicaFiltro(self, opcion):
        if self.originalVentana.find_all() != ():
            if opcion == 1:
                self.nuevaImagen = gris1(self.imagen, self.otra)
            elif opcion == 2:
                self.nuevaImagen = gris2(self.imagen, self.otra)
            elif opcion == 3:
                self.nuevaImagen = gris3(self.imagen, self.otra)
            elif opcion == 4:
                self.nuevaImagen = gris4(self.imagen, self.otra)
            elif opcion == 5:
                self.nuevaImagen = gris5(self.imagen, self.otra)
            elif opcion == 6:
                self.nuevaImagen = gris6(self.imagen, self.otra)
            elif opcion == 7:
                self.nuevaImagen = gris7(self.imagen, self.otra)
            elif opcion == 8:
                self.nuevaImagen = gris8(self.imagen, self.otra)
            elif opcion == 9:
                self.nuevaImagen = gris9(self.imagen, self.otra)
            imageOtra = ImageTk.PhotoImage(self.nuevaImagen)
            self.originalVentana.image = imageOtra
            self.originalVentana.create_image(imageOtra.width() / 2, imageOtra.height() / 2, anchor=CENTER,
                                              image=imageOtra, tags="bg_img")
        else:
            tkinter.messagebox.showwarning("Error", "No has seleccionado imagen a editar")

            # Da los parametros para el brillo

    def aplicaBrillo(self):
        if self.originalVentana.find_all() != ():
            self.top = Toplevel()
            self.label = Label(self.top, text="Ingresa un valor entre -255 y 255.")
            self.label.pack()

            self.entrytext = IntVar()
            Entry(self.top, textvariable=self.entrytext).pack()

            self.buttontext = StringVar()
            self.buttontext.set("Aplica Brillo")
            self.button = Button(self.top, textvariable=self.buttontext,
                                 command=lambda: self.sacaValor(self.entrytext)).pack()
        else:
            tkinter.messagebox.showwarning("Error", "No has seleccionado imagen a editar")

            # Guarda los valores dados para el brillo

    def sacaValor(self, valor):
        try:
            self.entrytext = valor.get()
            self.entrytext = int(self.entrytext)
        except Exception:
            tkinter.messagebox.showwarning("Error", "Valor ingresado no valido")
        self.nuevaImagen = brillo(self.imagen, self.otra, self.entrytext)
        imageOtra = ImageTk.PhotoImage(self.nuevaImagen)
        self.originalVentana.image = imageOtra
        self.originalVentana.create_image(imageOtra.width() / 2, imageOtra.height() / 2, anchor=CENTER, image=imageOtra,
                                          tags="bg_img")
        self.top.destroy()

        # Pregunta por los valores para los mosaicos

    def aplicaMosaico(self, opcion):
        if self.originalVentana.find_all() != ():
            self.top = Toplevel()
            self.label = Label(self.top, text="Introduce los valores del mosaico\ntienen que ser positivos para (x,y) ")
            self.label.pack()
            self.entraX = IntVar()
            Entry(self.top, textvariable=self.entraX).pack()
            self.entraY = IntVar()
            Entry(self.top, textvariable=self.entraY).pack()
            self.buttontext = StringVar()
            self.buttontext.set("Aplica mosaico")
            self.button = Button(self.top, textvariable=self.buttontext,
                                 command=lambda: self.obtenMosaico(self.entraX, self.entraY, opcion)).pack()
        else:
            tkinter.messagebox.showwarning("Error", "Escoge una imagen antes de aplicar un filtro")

            # Recibe los valores y hace el filtro Mosaico

    def obtenMosaico(self, valorX, valorY, opcion):
        self.entraX = valorX.get()
        self.entraY = valorY.get()
        self.nuevaImagen = mosaico(self.imagen, self.otra, self.entraX, self.entraY)
        imageOtra = ImageTk.PhotoImage(self.nuevaImagen)
        self.originalVentana.image = imageOtra
        self.originalVentana.create_image(imageOtra.width() / 2, imageOtra.height() / 2, anchor=CENTER, image=imageOtra,
                                          tags="bg_img")
        self.top.destroy()

        # Ejecuta nuestro programa


if __name__ == "__main__":
    root = Tk()
    root.title("Proceso digital de imagen: Práctica 1")
    root.wm_state("normal")
    app = Interfaz(root)
    root.mainloop()
