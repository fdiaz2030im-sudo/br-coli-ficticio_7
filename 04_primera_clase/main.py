"""EJERCICIO 04 — Funciones como valores y argumentos

ENUNCIADO
Completa aplicar_operacion: recibe una lista y una función; aplica esa
función a cada elemento usando un ciclo y devuelve una lista.
Completa transformar: crea un diccionario de funciones lambda con las claves
"doble", "cuadrado" y "negativo". Usa aplicar_operacion para obtener
un diccionario con esas mismas claves y las listas transformadas.
No uses map ni modifiques la lista original.
Con [] cada lista del resultado debe estar vacía.

Entrada de transformar: [1, 2, 3]
Resultado esperado:
{"doble": [2, 4, 6], "cuadrado": [1, 4, 9], "negativo": [-1, -2, -3]}

Entrada de aplicar_operacion: [2, 4] y una función que sume 1.
Resultado esperado: [3, 5]

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 04".
"""

def aplicar_operacion(valores, operacion):
    resultado = []
    for valor in valores:
        resultado.append(operacion(valor))
    return resultado

def transformar(valores):
    operaciones = {
        "doble": lambda x: x * 2,
        "cuadrado": lambda x: x ** 2,
        "negativo": lambda x: -x
    }
    
    resultados_transformados = {}
    for clave, func in operaciones.items():
        resultados_transformados[clave] = aplicar_operacion(valores, func)
        
    return resultados_transformados


# Ejemplos de uso originales:
valores = [1, 2, 3]
print(transformar(valores))
print(aplicar_operacion([2, 4], lambda x: x + 1)) 
# Resultado esperado para aplicar_operacion: [3, 5]

# Nuevo ejemplo añadido:
valores_2 = [0, -5, 10]
print(transformar(valores_2))
# Resultado esperado para transformar(valores_2):
# {'doble': [0, -10, 20], 'cuadrado': [0, 25, 100], 'negativo': [0, 5, -10]}