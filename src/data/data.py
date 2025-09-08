class Data:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista)-1, -1, -1):
            invertida.append(lista[i])
        return invertida
    
    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        resultado = []
        for elem in lista:
            existe = False
            for r in resultado:
                if r == elem:
                    existe = True
                    break
            if not existe:
                resultado.append(elem)
        return resultado
    
    def merge_ordenado(self, lista1, lista2):
        i, j = 0, 0
        resultado = []
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1
        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1
        return resultado
    
    def rotar_lista(self, lista, k):
        n = len(lista)
        k = k % n
        rotada = []
        for i in range(n):
            rotada.append(lista[(n - k + i) % n])
        return rotada
    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_total = n * (n + 1) // 2
        suma_lista = 0
        for num in lista:
            suma_lista += num
        return suma_total - suma_lista
    
    def es_subconjunto(self, conjunto1, conjunto2):
        for elem in conjunto1:
            encontrado = False
            for c in conjunto2:
                if c == elem:
                    encontrado = True
                    break
            if not encontrado:
                return False
        return True
    
    def implementar_pila(self):
        pila = []
        def push(x):
            pila.append(x)
        def pop():
            if len(pila) == 0:
                return None
            return pila.pop()
        def peek():
            if len(pila) == 0:
                return None
            return pila[-1]
        def is_empty():
            return len(pila) == 0
        return {
            'push': push,
            'pop': pop,
            'peek': peek,
            'is_empty': is_empty
        }
    
    def implementar_cola(self):
        cola = []
        def enqueue(x):
            cola.append(x)
        def dequeue():
            if len(cola) == 0:
                return None
            return cola.pop(0)
        def peek():
            if len(cola) == 0:
                return None
            return cola[0]
        def is_empty():
            return len(cola) == 0
        return {
            'enqueue': enqueue,
            'dequeue': dequeue,
            'peek': peek,
            'is_empty': is_empty
        }
    
    def matriz_transpuesta(self, matriz):
        filas = len(matriz)
        columnas = len(matriz[0]) if filas > 0 else 0
        transpuesta = []
        for j in range(columnas):
            fila_transpuesta = []
            for i in range(filas):
                fila_transpuesta.append(matriz[i][j])
            transpuesta.append(fila_transpuesta)
        return transpuesta
