class Stats:
    def promedio(self, numeros):
        return sum(numeros) / len(numeros) if numeros else 0
    
    def mediana(self, numeros):
        n = len(numeros)
        if n == 0:
            return None
        nums = sorted(numeros)
        mid = n // 2
        if n % 2 == 0:
            return (nums[mid - 1] + nums[mid]) / 2
        else:
            return nums[mid]
    
    def moda(self, numeros):
        if not numeros:
            return None
        frecuencias = {}
        for num in numeros:
            frecuencias[num] = frecuencias.get(num, 0) + 1
        max_frecuencia = max(frecuencias.values())
        for num in numeros:
            if frecuencias[num] == max_frecuencia:
                return num
    
    def desviacion_estandar(self, numeros):
        n = len(numeros)
        if n == 0:
            return 0
        media = self.promedio(numeros)
        varianza = sum((x - media) ** 2 for x in numeros) / n
        return varianza ** 0.5
    
    def varianza(self, numeros):
        n = len(numeros)
        if n == 0:
            return 0
        media = self.promedio(numeros)
        return sum((x - media) ** 2 for x in numeros) / n
    
    def rango(self, numeros):
        if not numeros:
            return 0
        return max(numeros) - min(numeros)
