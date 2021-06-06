from Mosaico import *
from TonosGrises import *
import random


def letra(imagen, otra, mosaicoX, mosaicoY, nombre):
    mos = mosaico(imagen, otra, mosaicoX, mosaicoY)
    ancho = mos.size[0]
    alto = mos.size[1]
    rgb = mos.convert('RGB')
    f = open(nombre + '.html', 'w')
    for i in range(alto):
        for j in range(ancho):
            r, g, b = rgb.getpixel((j, i))
            f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">M</font>')
        f.write('<br>')
    f.close()


def letraGris(imagen, otra, mosaicoX, mosaicoY, nombre):
    mos = mosaico(imagen, otra, mosaicoX, mosaicoY)
    gris = gris1(mos, otra)
    ancho = gris.size[0]
    alto = gris.size[1]
    rgb = gris.convert('RGB')
    f = open(nombre + '.html', 'w')
    for i in range(alto):
        for j in range(ancho):
            r, g, b = rgb.getpixel((j, i))
            f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">M</font>')
        f.write('<br>')
    f.close()


def letrasByN(imagen, otra, mosaicoX, mosaicoY, nombre):
    mos = mosaico(imagen, otra, mosaicoX, mosaicoY)
    gris = gris1(mos, otra)
    ancho = gris.size[0]
    alto = gris.size[1]
    rgb = gris.convert('RGB')
    f = open(nombre + '.html', 'w')
    f.write("<PRE>")
    for i in range(alto):
        for j in range(ancho):
            r, g, b = rgb.getpixel((j, i))
            if 0 <= r <= 15:
                f.write('<font size ="-2">M</font>')
            elif 16 <= r <= 31:
                f.write('<font size ="-2">N</font>')
            elif 32 <= r <= 47:
                f.write('<font size ="-2">H</font>')
            elif 48 <= r <= 63:
                f.write('<font size ="-2">#</font>')
            elif 64 <= r <= 79:
                f.write('<font size ="-2">Q</font>')
            elif 80 <= r <= 95:
                f.write('<font size ="-2">U</font>')
            elif 96 <= r <= 111:
                f.write('<font size ="-2">A</font>')
            elif 112 <= r <= 127:
                f.write('<font size ="-2">D</font>')
            elif 128 <= r <= 143:
                f.write('<font size ="-2">O</font>')
            elif 144 <= r <= 159:
                f.write('<font size ="-2">Y</font>')
            elif 160 <= r <= 175:
                f.write('<font size ="-2">2</font>')
            elif 176 <= r <= 191:
                f.write('<font size ="-2">$</font>')
            elif 192 <= r <= 209:
                f.write('<font size ="-2">%</font>')
            elif 210 <= r <= 225:
                f.write('<font size ="-2">+</font>')
            elif 226 <= r <= 239:
                f.write('<font size ="-2">.</font>')
            elif 240 <= r <= 255:
                f.write('<font size ="-2"> </font>')
        f.write('<br>')
    f.write("</PRE>")
    f.close()


def letrasColor(imagen, otra, mosaicoX, mosaicoY, nombre):
    mos = mosaico(imagen, otra, mosaicoX, mosaicoY)
    rgbMosaico = mos.convert('RGB')
    gris = gris1(mos, otra)
    ancho = gris.size[0]
    alto = gris.size[1]
    rgbGris = gris.convert('RGB')
    f = open(nombre + '.html', 'w')
    f.write("<PRE>")
    for i in range(alto):
        for j in range(ancho):
            r, g, b = rgbMosaico.getpixel((j, i))
            rc, gc, bc = rgbGris.getpixel((j, i))
            if 0 <= rc <= 15:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">M</font>')
            elif 16 <= rc <= 31:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">N</font>')
            elif 32 <= rc <= 47:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">H</font>')
            elif 48 <= rc <= 63:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">#</font>')
            elif 64 <= rc <= 79:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">Q</font>')
            elif 80 <= rc <= 95:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">U</font>')
            elif 96 <= rc <= 111:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">A</font>')
            elif 112 <= rc <= 127:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">D</font>')
            elif 128 <= rc <= 143:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">O</font>')
            elif 144 <= rc <= 159:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">Y</font>')
            elif 160 <= rc <= 175:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">2</font>')
            elif 176 <= rc <= 191:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">$</font>')
            elif 192 <= rc <= 207:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">%</font>')
            elif 208 <= rc <= 223:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">+</font>')
            elif 224 <= rc <= 239:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">.</font>')
            elif 240 <= rc <= 255:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');"> </font>')
        f.write('<br>')
    f.write("</PRE>")
    f.close()


def letrasGrises(imagen, otra, mosaicoX, mosaicoY, nombre):
    mos = mosaico(imagen, otra, mosaicoX, mosaicoY)
    gris = gris1(mos, otra)
    ancho = gris.size[0]
    alto = gris.size[1]
    rgb = gris.convert('RGB')
    f = open(nombre + '.html', 'w')
    f.write("<PRE>")
    for i in range(alto):
        for j in range(ancho):
            r, g, b = rgb.getpixel((j, i))
            if 0 <= r <= 15:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">M</font>')
            elif 16 <= r <= 31:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">N</font>')
            elif 32 <= r <= 47:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">H</font>')
            elif 48 <= r <= 63:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">#</font>')
            elif 64 <= r <= 79:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">Q</font>')
            elif 80 <= r <= 95:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">U</font>')
            elif 96 <= r <= 111:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">A</font>')
            elif 112 <= r <= 127:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">D</font>')
            elif 128 <= r <= 143:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">O</font>')
            elif 144 <= r <= 159:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">Y</font>')
            elif 160 <= r <= 175:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">2</font>')
            elif 176 <= r <= 191:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">$</font>')
            elif 192 <= r <= 207:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">%</font>')
            elif 208 <= r <= 223:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">+</font>')
            elif 224 <= r <= 239:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">.</font>')
            elif 240 <= r <= 255:
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');"> </font>')
        f.write('<br>')
    f.write("</PRE>")
    f.close()


def palabras(imagen, otra, mosaicoX, mosaicoY, nombre, palabra):
    mos = mosaico(imagen, otra, mosaicoX, mosaicoY)
    ancho = mos.size[0]
    alto = mos.size[1]
    cont = 0
    rgb = mos.convert('RGB')
    f = open(nombre + '.html', 'w')
    f.write("<PRE>")
    for i in range(alto):
        for j in range(ancho):
            r, g, b = rgb.getpixel((j, i))
            if cont < len(palabra):
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">' + palabra[
                    cont] + '</font>')
                cont = cont + 1
            else:
                cont = 0
                f.write('<font size="-2" style="color:rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ');">' + palabra[
                    cont] + '</font>')
                cont = cont + 1
        f.write('<br>')
    f.write("</PRE>")
    f.close()


def dominoB(imagen, otra, mosaicoX, mosaicoY, nombre):
    mos = mosaico(imagen, otra, mosaicoX, mosaicoY)
    gris = gris1(mos, otra)
    ancho = gris.size[0]
    alto = gris.size[1]
    rgb = gris.convert('RGB')
    f = open(nombre + '.html', 'w')
    f.write(
        "<PRE><style>@font-face{font-family: 'Lasvwd__';src: url('fonts/Lasvwd__.ttf') format('truetype');}font{font-family: 'Lasvwd__'}</style>")
    for i in range(alto):
        for j in range(ancho):
            r, g, b = rgb.getpixel((j, i))
            if 0 <= r <= 25:
                f.write('<font size="-2">9(</font>')
            elif 26 <= r <= 51:
                f.write('<font size="-2">8i</font>')
            elif 52 <= r <= 77:
                f.write('<font size="-2">7&</font>')
            elif 78 <= r <= 103:
                f.write('<font size="-2">6^</font>')
            elif 104 <= r <= 129:
                f.write('<font size="-2">5%</font>')
            elif 130 <= r <= 155:
                f.write('<font size="-2">4%</font>')
            elif 156 <= r <= 181:
                f.write('<font size="-2">3#</font>')
            elif 182 <= r <= 207:
                f.write('<font size="-2">2@</font>')
            elif 208 <= r <= 233:
                f.write('<font size="-2">1!</font>')
            elif 234 <= r <= 255:
                f.write('<font size="-2">0)</font>')
        f.write('<br>')
    f.write('</PRE>')
    f.close()


def dominoN(imagen, otra, mosaicoX, mosaicoY, nombre):
    mos = mosaico(imagen, otra, mosaicoX, mosaicoY)
    gris = gris1(mos, otra)
    ancho = gris.size[0]
    alto = gris.size[1]
    rgb = gris.convert('RGB')
    f = open(nombre + '.html', 'w')
    f.write(
        "<PRE><style>@font-face{font-family: 'Lasvbld_';src: url('fonts/Lasvbld_.ttf') format('truetype');}font{font-family: 'Lasvbld_'}</style>")
    for i in range(alto):
        for j in range(ancho):
            r, g, b = rgb.getpixel((j, i))
            if 0 <= r <= 25:
                f.write('<font size="-2">0)</font>')
            elif 26 <= r <= 51:
                f.write('<font size="-2">1!</font>')
            elif 52 <= r <= 77:
                f.write('<font size="-2">2@</font>')
            elif 78 <= r <= 103:
                f.write('<font size="-2">3#</font>')
            elif 104 <= r <= 129:
                f.write('<font size="-2">4$</font>')
            elif 130 <= r <= 155:
                f.write('<font size="-2">5%</font>')
            elif 156 <= r <= 181:
                f.write('<font size="-2">6^</font>')
            elif 182 <= r <= 207:
                f.write('<font size="-2">7&</font>')
            elif 208 <= r <= 233:
                f.write('<font size="-2">8i</font>')
            elif 234 <= r <= 255:
                f.write('<font size="-2">9(</font>')
        f.write('<br>')
    f.write('</PRE>')
    f.close()


def naipes(imagen, otra, mosaicoX, mosaicoY, nombre):
    mos = mosaico(imagen, otra, mosaicoX, mosaicoY)
    gris = gris1(mos, otra)
    ancho = gris.size[0]
    alto = gris.size[1]
    rgb = gris.convert('RGB')
    f = open(nombre + '.html', 'w')
    f.write(
        "<PRE><style>@font-face{font-family: 'PLAYCRDS';src: url('fonts/PLAYCRDS.TTF') format('truetype');}font{font-family: 'PLAYCRDS'}</style>")
    for i in range(alto):
        for j in range(ancho):
            r, g, b = rgb.getpixel((j, i))
            if 0 <= r <= 23:
                especial = random.choice('123')
                if especial == 1:
                    f.write('<font size="-2">x</font>')
                elif especial == 2:
                    f.write('<font size="-2">y</font>')
                else:
                    f.write('<font size="-2">z</font>')
            elif 24 <= r <= 47:
                f.write('<font size="-2">w</font>')
            elif 48 <= r <= 71:
                f.write('<font size="-2">v</font>')
            elif 72 <= r <= 95:
                f.write('<font size="-2">u</font>')
            elif 96 <= r <= 119:
                f.write('<font size="-2">t</font>')
            elif 120 <= r <= 143:
                f.write('<font size="-2">s</font>')
            elif 144 <= r <= 167:
                f.write('<font size="-2">r</font>')
            elif 168 <= r <= 191:
                f.write('<font size="-2">q</font>')
            elif 192 <= r <= 215:
                f.write('<font size="-2">p</font>')
            elif 216 <= r <= 239:
                f.write('<font size="-2">o</font>')
            elif 240 <= r <= 255:
                f.write('<font size="-2">n</font>')
        f.write('<br>')
    f.write('</PRE>')
    f.close()
