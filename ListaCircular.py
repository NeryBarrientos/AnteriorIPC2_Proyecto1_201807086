from nodo import Nodo

class ListaCircularxd(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def Vacio(self):
        if self.primero == None:
            return True
    
    def InsertarFinal(self,nombre='',n='',m=''):
        if self.Vacio():
            self.primero=self.ultimo = Nodo(nombre,n,m)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(nombre,n,m)
            self.ultimo.siguiente = self.primero
    
    def printLista(self):
        if self.Vacio():
            print('Lista Vacia')
        else:
            validar = True
            aux = self.primero
            n = 1
            while validar:

                print(f'{n}. {aux.nombre} {aux.m} {aux.n}')
                n += 1
                if aux == self.ultimo:
                    validar = False
                else:
                    aux = aux.siguiente