"""EJERCICIO 03 — Precios con recargo

ENUNCIADO
Dentro de la función, define una lambda que reciba un precio y devuelva
ese precio con un recargo del 10 %, redondeado a dos decimales con round.
Aplica la lambda mediante un ciclo y devuelve una lista.
No uses map todavía. Los precios son no negativos. No modifiques la entrada.
Para [] devuelve [].

Entrada: [10, 20, 35]
Resultado esperado: [11.0, 22.0, 38.5]

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 03".
"""

def calcular_importes(precios):
    # Definimos la lambda que calcula el recargo del 10% y redondea a 2 decimales
    aplicar_recargo = lambda p: round(p * 1.10, 2)
    
    importes = []
    # Usamos un ciclo explícito para aplicar la lambda a cada precio
    for precio in precios:
        importes.append(aplicar_recargo(precio))
        
    return importes


# Ejemplo de uso original:
precios = [10, 20, 35]
print(calcular_importes(precios))

# Nuevo ejemplo añadido:
precios_2 = [0, 15.5, 99.99]
print(calcular_importes(precios_2))
# Resultado esperado para precios_2: [0.0, 17.05, 109.99] 
# (Explicación: 0 * 1.1 = 0.0, 15.5 * 1.1 = 17.05, 99.99 * 1.1 = 109.989 que redondea a 109.99)