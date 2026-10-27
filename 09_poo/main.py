"""EJERCICIO 09 — Clase Producto

ENUNCIADO
Implementa Producto con atributos de instancia nombre, precio y stock.
El constructor recibe esos tres valores. Precio y stock son enteros no negativos.
- valor_inventario(): devuelve precio * stock, sin modificar los atributos.
- vender(cantidad): si cantidad > 0 y hay suficiente stock, descuenta esa
  cantidad y devuelve True. En caso contrario devuelve False sin cambiar stock.
Las cantidades son enteras; no necesitas validar otros tipos.
Comprueba con print que dos instancias mantienen su stock de forma independiente.
No se requiere herencia ni métodos especiales adicionales al constructor.

ENTREGA
Completa la clase, ejecuta y compara los resultados con los comentarios.
Añade otro ejemplo con print y su resultado esperado en un comentario.
Haz un commit: "Resuelve ejercicio 09".
"""


class Producto:
    def __init__(self, nombre, precio, stock):
        # TODO: inicializa los atributos de instancia.
        pass

    def valor_inventario(self):
        # TODO: devuelve el valor del inventario.
        pass

    def vender(self, cantidad):
        # TODO: aplica las reglas de venta y devuelve un booleano.
        pass


cafe = Producto("cafe", 10, 5)
te = Producto("te", 8, 3)
print(cafe.valor_inventario())  # Esperado: 50
print(cafe.vender(2))          # Esperado: True
print(cafe.valor_inventario())  # Esperado: 30
print(cafe.vender(4))          # Esperado: False
print(cafe.vender(0))          # Esperado: False
print(cafe.vender(-1))         # Esperado: False
print(cafe.valor_inventario())  # Esperado: 30
print(te.valor_inventario())    # Esperado: 24 (no debe cambiar)
print(cafe.vender(3))          # Esperado: True
print(cafe.valor_inventario())  # Esperado: 0
# TODO: añade otro ejemplo con print y su resultado esperado en un comentario.
