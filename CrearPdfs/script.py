__author__ = 'JCordova'

from reportlab.pdfgen import canvas
from PIL import Image
import os
import glob

def getDirectorios(raiz):
    directorios = glob.glob(str(raiz)+"\\*")
    for direccion in directorios:
        print direccion+"\n"
        if not os.path.isdir(direccion):
            directorios.remove(direccion)

    return directorios


def getFicheros(raiz):
    ficheros = glob.glob(str(raiz)+"\\*")
    print "Ficheros del Directorio : "+str(raiz)+"\\* \n"
    for fichero in ficheros:
        print fichero+"\n"
        if not os.path.isfile(fichero) or fichero[len(fichero)-1]=='b':
            ficheros.remove(fichero)
    return ficheros


def Script():

    n = raw_input("Direccion a ejecutar el Script : ")
    fexa = raw_input("Fecha : ")
    if os.path.isdir(str(n)):

        print "Usted Ingreso el Directorio... : "+str(n)+"\n"
        print "Buscando Subcarpetas... \n"

        directorios = getDirectorios(str(n))

        for directorio in directorios:

            ficheros = getFicheros(directorio)

            aux = canvas.Canvas(str(directorio)+".pdf")

            for fichero in ficheros:
                img = Image.open(str(fichero))
                a, b = img.size

                if(a>b or a==b):
                    aux.setPageSize((845,595))
                    aux.drawImage(str(fichero),10,10,825,575)
                elif (b>a):
                    aux.setPageSize((595,845))
                    aux.drawImage(str(fichero),10,10,575,825)

                aux.showPage()

            #aux.drawString(50,200,"EJEMPLO DE INSERCION DE IMAGEN EN PDF")

            aux.save()

    else:
        print "El texto ingresado no es un Directorio :( "


if "__main__"==__name__:
    print "Se inica el Script"
    print Script()