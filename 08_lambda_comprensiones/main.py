"""EJERCICIO 08 — Simulación de descuentos

ENUNCIADO
Define una lambda de dos parámetros: precio y porcentaje de descuento.
Debe calcular round(precio * (1 - porcentaje / 100), 2).
Invócala dentro de una comprensión anidada para devolver una lista de listas.
Cada fila corresponde a un porcentaje; cada columna corresponde a un precio.
Conserva el orden de ambas listas. No uses ciclos explícitos ni map.
Los precios son no negativos y los porcentajes están entre 0 y 100.
Si porcentajes está vacía, devuelve []. Si precios está vacía, devuelve
una fila vacía por cada porcentaje.

Precios: [10, 20, 40]. Porcentajes: [0, 10, 25].
Resultado esperado:
[[10.0, 20.0, 40.0], [9.0, 18.0, 36.0], [7.5, 15.0, 30.0]]

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 08".


"""
def generar_simulaciones(precios, porcentajes):
    # Lambda que aplica el descuento y redondea a 2 decimales
    aplicar_descuento = lambda p, desc: round(p * (1 - desc / 100), 2)
    
    # Comprensión anidada: la externa itera porcentajes (filas), la interna precios (columnas)
    return [[aplicar_descuento(p, desc) for p in precios] for desc in porcentajes]


# Ejemplo de uso original:
precios = [10, 20, 40]
porcentajes = [0, 10, 25]
print(generar_simulaciones(precios, porcentajes))

# Nuevo ejemplo añadido:
precios_2 = [100, 50]
porcentajes_2 = [15, 50]
print(generar_simulaciones(precios_2, porcentajes_2))
# Resultado esperado para precios_2 y porcentajes_2:
# [[85.0, 42.5], [50.0, 25.0]]

# Ejemplo con precios vacíos:
print(generar_simulaciones([], [10, 20]))
# Resultado esperado para precios vacíos: [[], []]