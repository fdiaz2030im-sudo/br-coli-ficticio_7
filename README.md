# Laboratorio de Python

## Objetivo
Practicar estructuras de datos, comprensiones, lambda, funciones como valores,
map, filter, any, reduce, POO básica y módulos. Cada carpeta es independiente.
No hay soluciones incluidas ni dependencias externas.

## Inicio
1. Crea tu repositorio con Use this template en la plantilla de la docente.
2. Clona tu repositorio y entra en su carpeta.
3. Completa DATOS_ESTUDIANTE.md y realiza un commit inicial.

## Ejercicios
| Número | Actividad | Carpeta |
| --- | --- | --- |
| 01 | Resumen de ventas | `01_estructuras/` |
| 02 | Preparar un catálogo | `02_comprensiones/` |
| 03 | Precios con recargo | `03_lambda/` |
| 04 | Funciones como valores y argumentos | `04_primera_clase/` |
| 05 | Subtotales de pedidos | `05_map/` |
| 06 | Revisión del inventario | `06_filter_any/` |
| 07 | Total de ventas | `07_reduce/` |
| 08 | Simulación de descuentos | `08_lambda_comprensiones/` |
| 09 | Clase Producto | `09_poo/` |
| 10 | Módulos e integración | `10_modulos_integrador/` |

## Cómo trabajar
Lee el enunciado dentro del .py. Completa los TODO y sustituye pass por tu código.
pass es un marcador que no realiza ninguna acción; no es la solución.
Las funciones incompletas imprimen None hasta que devuelvan sus resultados.
En el ejercicio 10 debes completar las importaciones y descomentar los print.

Ejecuta desde la raíz del repositorio:

```bash
python 01_estructuras/main.py
```

Usa python3 o py en lugar de python si ese es el comando de tu equipo.
Compara lo que imprime tu programa con los resultados esperados del enunciado.
Añade al menos un ejemplo propio con print y escribe el resultado esperado en
un comentario. Revisa también las listas vacías cuando el ejercicio las contemple.
No basta con imprimir un resultado escrito a mano: debes calcularlo con los datos.

Después de terminar cada ejercicio:

```bash
git add 01_estructuras/
git commit -m "Resuelve ejercicio 01"
git push
```

Cambia carpeta y número en cada ejercicio. No acumules todos en un solo commit.
Para el ejercicio 10 registra sus tres módulos juntos:

```bash
python 10_modulos_integrador/main.py
git add 10_modulos_integrador/
git commit -m "Resuelve ejercicio 10"
git push
```