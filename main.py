from os import pipe, system
import xml.etree.ElementTree as ET
from ListaCircular import ListaCircularxd
system("cls")
datos = []

def Cargar():
    global datos
    print('Opcion Cargar Archivo:\nIngrese la ruta del archivo:' ,end='')
    lectura = input()
    tree = ET.parse(lectura)
    root = tree.getroot()
    for element in root.findall('matriz'):
        #print(element.attrib)
        nombre = element.attrib
        prueba = ListaCircularxd()
        prueba.InsertarFinal(nombre['nombre'],nombre['n'],nombre['m'])
        prueba.printLista()
        for i in element.findall('dato'):
            print(i.text)

def menu():
    print('Menu Principal:\n     1.Cargar Archivo\n     2.Procesar Archivo\n     3.Escribir Archivo salida\n     4.Mostrar Datos del estudiante\n     5.Generar Grafica\n     6.Salir')
    print('Escoja una opcion: ', end='')
    lectura = input()
    if int(lectura) == 1:
        Cargar()
menu()
tree = ET.parse('prueba.xml')
root = tree.getroot()
