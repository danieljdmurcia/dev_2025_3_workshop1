class Strings:
    def es_palindromo(self, texto):
        texto = texto.lower().replace(" ", "")
        return texto == texto[::-1]
    
    def invertir_cadena(self, texto):
        resultado = ""
        for char in texto:
            resultado = char + resultado
        return resultado
    
    def contar_vocales(self, texto):
        vocales = "aeiouAEIOU"
        contador = 0
        for char in texto:
            if char in vocales:
                contador += 1
        return contador
    
    def contar_consonantes(self, texto):
        consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        contador = 0
        for char in texto:
            if char in consonantes:
                contador += 1
        return contador
    
    def es_anagrama(self, texto1, texto2):
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())
    
    def contar_palabras(self, texto):
        palabras = texto.strip().split()
        return len(palabras)
    
    def palabras_mayus(self, texto):
        resultado = ""
        i = 0
        while i < len(texto):
            if texto[i].isspace():
                resultado += texto[i]
                i += 1
            else:
                start = i
                while i < len(texto) and not texto[i].isspace():
                    i += 1
                palabra = texto[start:i]
                resultado += palabra[0].upper() + palabra[1:].lower() if palabra else ""
        return resultado
    
    def eliminar_espacios_duplicados(self, texto):
        resultado = ""
        prev_espacio = False
        for char in texto:
            if char == " ":
                if not prev_espacio:
                    resultado += char
                prev_espacio = True
            else:
                resultado += char
                prev_espacio = False
        return resultado  # sin strip para conservar espacios iniciales y finales
    
    def es_numero_entero(self, texto):
        if texto == "":
            return False
        i = 0
        if texto[0] in "+-":
            if len(texto) == 1:
                return False
            i = 1
        while i < len(texto):
            if texto[i] < '0' or texto[i] > '9':
                return False
            i += 1
        return True
    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for char in texto:
            if 'a' <= char <= 'z':
                resultado += chr((ord(char) - ord('a') + desplazamiento) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                resultado += chr((ord(char) - ord('A') + desplazamiento) % 26 + ord('A'))
            else:
                resultado += char
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        if not subcadena:
            return []
        posiciones = []
        n = len(texto)
        m = len(subcadena)
        for i in range(n - m + 1):
            match = True
            for j in range(m):
                if texto[i + j] != subcadena[j]:
                    match = False
                    break
            if match:
                posiciones.append(i)
        return posiciones
