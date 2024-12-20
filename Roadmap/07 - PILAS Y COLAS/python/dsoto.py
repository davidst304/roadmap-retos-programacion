"""
* EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atras" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

# Esto es para una pila (LIFO)
lista =[]

lista.append(1) # meter elementos
lista.append(2) # meter elementos
lista.append(3) # meter elementos
ultimo = lista[-1]

print(lista)
print(lista.pop())
print(lista)

# Esto es para una cola (FIFO)

lista.append(4) # meter elementos
lista.append(5) # meter elementos
lista.append(7) # meter elementos
del lista[0]

# Caso real para usar pila y cola en un programa


listaWeb = []

listaWeb.append('https://cadizescapadas.com/')
listaWeb.append('https://9a811579.smoobu.net/es/')
listaWeb.append('https://www.youtube.com/watch?v=cBeRWS2X0CA')

from selenium import webdriver as web
driver = web.Firefox()

i = False

while i == False:
    mot = input("Adelante, Atrás, O i = True")
    driver.get(listaWeb[0])
    



