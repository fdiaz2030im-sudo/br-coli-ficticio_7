"""EJERCICIO 07 — Total de ventas

ENUNCIADO
Cada pedido es una tupla (producto, precio_unitario, cantidad).
Usa map con lambda para obtener los subtotales y reduce con lambda para sumarlos.
Importa reduce del módulo functools. Usa 0 como valor inicial de reduce.
No uses sum, ciclos ni comprensiones. Los valores son enteros no negativos.
Para [] devuelve 0.

Entrada: [("cafe", 10, 2), ("te", 8, 3), ("torta", 25, 1)]
Resultado esperado: 69

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 07".
"""

from functools import reduce

def total_ventas(pedidos):
    # map con lambda calcula el subtotal (precio_unitario * cantidad) de cada tupla
    subtotales = map(lambda p: p[1] * p[2], pedidos)
    
    # reduce con lambda suma los subtotales acumulándolos, partiendo de 0
    total = reduce(lambda acumulador, valor: acumulador + valor, subtotales, 0)
    
    return total


# Ejemplo de uso original:
pedidos = [("cafe", 10, 2), ("te", 8, 3), ("torta", 25, 1)]
print(total_ventas(pedidos))

# Nuevo ejemplo añadido:
pedidos_2 = [("agua", 2, 5), ("sandwich", 15, 2)]
print(total_ventas(pedidos_2))
# Resultado esperado para pedidos_2: 40 
# (Explicación: 2*5 = 10 para agua, 15*2 = 30 para sandwich, 10 + 30 = 40)

# Ejemplo con lista vacía:
print(total_ventas([]))
# Resultado esperado para []: 0
