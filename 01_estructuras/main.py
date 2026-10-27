"""EJERCICIO 01 — Resumen de ventas

ENUNCIADO
Recibes una lista de tuplas (producto, cantidad). Devuelve un diccionario con:
- productos: set con los nombres vendidos.
- unidades: total de unidades vendidas.
- por_producto: diccionario con las cantidades acumuladas por producto.
Usa ciclos, un set y un diccionario. No modifiques la entrada.
Las cantidades son enteros positivos. Para [] devuelve estructuras vacías y total 0.

Ejemplo:
Entrada: [("cafe", 2), ("te", 1), ("cafe", 3)]
Resultado: {"productos": {"cafe", "te"}, "unidades": 6,
            "por_producto": {"cafe": 5, "te": 1}}
El orden de los elementos del set puede cambiar.

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 01".
"""

def resumir_ventas(ventas):
    productos = set()
    unidades = 0
    por_producto = {}
    
    for producto, cantidad in ventas:
        productos.add(producto)
        unidades += cantidad
        por_producto[producto] = por_producto.get(producto, 0) + cantidad
        
    return {
        "productos": productos,
        "unidades": unidades,
        "por_producto": por_producto
    }

# Ejemplo de uso original:
ventas = [("cafe", 2), ("te", 1), ("cafe", 3)]
print(resumir_ventas(ventas))

# Nuevo ejemplo añadido:
ventas_2 = [("manzana", 5), ("pera", 2), ("manzana", 1), ("uva", 4)]
print(resumir_ventas(ventas_2))
# Resultado esperado para ventas_2:
# {'productos': {'manzana', 'pera', 'uva'}, 'unidades': 12, 'por_producto': {'manzana': 6, 'pera': 2, 'uva': 4}}