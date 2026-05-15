def calcular_promedio(lista):
    suma = sum(lista)
    cantidad = len(lista)
    promedio = suma / cantidad
    return promedio

def promedio_diccionario(diccionario):
    valores = diccionario.values()
    suma = sum(valores)
    cantidad = len(valores)
    promedio = suma / cantidad
    return promedio