import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo

        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def imprimir_inorden(self):
        self._imprimir_inorden_recursivo(self.raiz)

    def _imprimir_inorden_recursivo(self, nodo):
        if nodo is not None:
            self._imprimir_inorden_recursivo(nodo.izquierda)
            print(nodo.valor, end=' ')
            self._imprimir_inorden_recursivo(nodo.derecha)

    def graficar_arbol(self):
        fig, ax = plt.subplots()
        self._graficar_recursivo(ax, self.raiz, 0, 0, 100)

        ax.axis('off')
        plt.show()

    def _graficar_recursivo(self, ax, nodo, x, y, nivel):
        if nodo is None:
            return

        ax.text(x, y, str(nodo.valor), style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

        if nodo.izquierda is not None:
            ax.plot([x, x - nivel], [y, y - 1], 'k-')
            self._graficar_recursivo(ax, nodo.izquierda, x - nivel, y - 1, nivel/2)

        if nodo.derecha is not None:
            ax.plot([x, x + nivel], [y, y - 1], 'k-')
            self._graficar_recursivo(ax, nodo.derecha, x + nivel, y - 1, nivel/2)