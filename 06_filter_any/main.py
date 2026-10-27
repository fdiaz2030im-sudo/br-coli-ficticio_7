"""EJERCICIO 06 — Revisión del inventario

ENUNCIADO
Cada producto tiene nombre y stock (entero no negativo).
Devuelve un diccionario con:
- reponer: lista de nombres con stock < 5, en el orden original.
- hay_agotados: booleano que indica si algún stock es igual a 0.
Usa filter con lambda para seleccionar, map con lambda para obtener nombres,
y any sobre map con lambda para detectar agotados.
No uses ciclos ni comprensiones ni modifiques los datos.
Para [] devuelve {"reponer": [], "hay_agotados": False}.

Con los datos entregados se espera:
{"reponer": ["te", "torta"], "hay_agotados": True}
Un producto con stock igual a 5 no debe aparecer en reponer.

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 06".
"""

def revisar_stock(productos):
    # Filtrar productos con stock menor a 5 y extraer sus nombres
    reponer = list(map(lambda p: p["nombre"], filter(lambda p: p["stock"] < 5, productos)))
    
    # Verificar si hay algún producto con stock igual a 0
    hay_agotados = any(map(lambda p: p["stock"] == 0, productos))
    
    return {
        "reponer": reponer,
        "hay_agotados": hay_agotados
    }


# Ejemplo de uso original:
productos = [
    {"nombre": "cafe", "stock": 8},
    {"nombre": "te", "stock": 0},
    {"nombre": "torta", "stock": 3},
]
print(revisar_stock(productos))

# Nuevo ejemplo añadido:
productos_2 = [
    {"nombre": "agua", "stock": 5}, 
    {"nombre": "jugo", "stock": 10}, 
    {"nombre": "galletas", "stock": 4}
]
print(revisar_stock(productos_2))
# Resultado esperado para productos_2:
# {'reponer': ['galletas'], 'hay_agotados': False}