from abc import ABC, abstractmethod

class EncolableAbstract(ABC):
    @abstractmethod
    def esta_vacia(self):
        pass

    @abstractmethod
    def vaciar(self):
        pass

    @abstractmethod
    def agregar(self, elemento):
        pass

    @abstractmethod
    def contiene(self, elemento):
        pass

    @abstractmethod
    def tomar(self):
        pass

    @abstractmethod
    def primer_elemento(self):
        pass

    @abstractmethod
    def eliminar(self):
        pass

    @abstractmethod
    def imprimir(self):
        pass

    @abstractmethod
    def iterador(self):
        pass

class Cola(EncolableAbstract):
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def vaciar(self):
        self.items = []

    def agregar(self, elemento):
        self.items.append(elemento)

    def contiene(self, elemento):
        return elemento in self.items

    def tomar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def primer_elemento(self):
        if not self.esta_vacia():
            return self.items[0]
        return None

    def eliminar(self):
        if not self.esta_vacia():
            self.items.pop(0)

    def imprimir(self):
        print(self.items)

    def iterador(self):
        return iter(self.items)

# Prueba de los métodos de la clase Cola
cola = Cola()

print("¿La cola está vacía?", cola.esta_vacia())

cola.agregar(1)
cola.agregar(2)
cola.agregar(3)

print("¿La cola contiene el elemento 2?", cola.contiene(2))

cola.imprimir()

print("Primer elemento de la cola:", cola.primer_elemento())

print ("Eliminamos el primer elemento de la cola:"), cola.eliminar()

cola.imprimir()

print("Tomar un elemento de la cola:", cola.tomar())

cola.imprimir()

cola.vaciar()

print("¿La cola está vacía?", cola.esta_vacia())
