from src.estadistica import calcular_promedio
from src.estadistica import promedio_diccionario

datos = [10, 30, 40 ,50]

resultado = calcular_promedio(datos)


print ("el promedio de la lista es:", resultado)

nota = {
    "juan": 3.3,
    "ana": 4.2,
    "pedro": 4.6,
    "laura":3.9
}
promedio_notas = promedio_diccionario(nota)
print