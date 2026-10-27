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
    # TODO: implementa lo solicitado y devuelve el resultado.
    pass


# Ejemplo de uso: inicialmente imprime None porque falta la implementación.
precios = [10, 20, 40]
porcentajes = [0, 10, 25]
print(generar_simulaciones(precios, porcentajes))

# TODO: añade otro ejemplo con print y su resultado esperado en un comentario.
