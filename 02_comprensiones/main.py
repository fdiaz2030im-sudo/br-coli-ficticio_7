"""EJERCICIO 02 — Preparar un catálogo

ENUNCIADO
Cada producto tiene nombre, precio y categoria. Los nombres son únicos.
Devuelve un diccionario con:
- disponibles: lista de nombres con precio <= 20, en el orden original.
- precios: diccionario nombre -> precio de todos los productos.
- categorias: set de todas las categorías.
Usa una comprensión para cada estructura. No uses ciclos explícitos.
No modifiques la entrada. Para [] devuelve las tres estructuras vacías.

Con los datos entregados se espera:
{"disponibles": ["cafe", "te"],
 "precios": {"cafe": 10, "torta": 25, "te": 8},
 "categorias": {"bebida", "postre"}}
El orden de los elementos del set puede cambiar.

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 02".
"""

def preparar_catalogo(productos):
    # Comprensión de lista para los nombres con precio <= 20
    disponibles = [p["nombre"] for p in productos if p["precio"] <= 20]
    
    # Comprensión de diccionario para el mapeo nombre -> precio
    precios = {p["nombre"]: p["precio"] for p in productos}
    
    # Comprensión de set para obtener las categorías únicas
    categorias = {p["categoria"] for p in productos}
    
    return {
        "disponibles": disponibles,
        "precios": precios,
        "categorias": categorias
    }


# Ejemplo de uso original:
productos = [
    {"nombre": "cafe", "precio": 10, "categoria": "bebida"},
    {"nombre": "torta", "precio": 25, "categoria": "postre"},
    {"nombre": "te", "precio": 8, "categoria": "bebida"},
]
print(preparar_catalogo(productos))

# Nuevo ejemplo añadido:
productos_2 = [
    {"nombre": "agua", "precio": 2, "categoria": "bebida"},
    {"nombre": "hamburguesa", "precio": 22, "categoria": "comida"},
    {"nombre": "papas", "precio": 15, "categoria": "comida"},
]
print(preparar_catalogo(productos_2))
# Resultado esperado para productos_2:
# {'disponibles': ['agua', 'papas'], 'precios': {'agua': 2, 'hamburguesa': 22, 'papas': 15}, 'categorias': {'bebida', 'comida'}}