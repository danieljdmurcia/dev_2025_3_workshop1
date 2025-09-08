class Magic:
    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
    
    def secuencia_fibonacci(self, n):
        seq = []
        a, b = 0, 1
        for _ in range(n):
            seq.append(a)
            a, b = b, a + b
        return seq
    
    def es_primo(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        primos = []
        for num in range(2, n+1):
            if self.es_primo(num):
                primos.append(num)
        return primos
    
    def es_numero_perfecto(self, n):
        if n < 2:
            return False
        suma = 1
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                suma += i
                if i != n // i:
                    suma += n // i
        return suma == n
    
    def triangulo_pascal(self, filas):
        resultado = []
        for i in range(filas):
            fila = [1]
            if resultado:
                ultima = resultado[-1]
                for j in range(len(ultima)-1):
                    fila.append(ultima[j] + ultima[j+1])
                fila.append(1)
            resultado.append(fila)
        return resultado
    
    def factorial(self, n):
        resultado = 1
        for i in range(2, n+1):
            resultado *= i
        return resultado
    
    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        return abs(a*b) // self.mcd(a, b) if a and b else 0
    
    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))
    
    def es_numero_armstrong(self, n):
        digitos = str(abs(n))
        p = len(digitos)
        suma = sum(int(d)**p for d in digitos)
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        if any(len(fila) != n for fila in matriz):
            return False
        suma_objetivo = sum(matriz[0])
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False
        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_objetivo:
                return False
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False
        if sum(matriz[i][n-1-i] for i in range(n)) != suma_objetivo:
            return False
        return True
