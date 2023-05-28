# Reconocedor de cadenas

## Descripción

Sea un lenguaje como el siguiente:

$$
L = (^nabc)^{n−1}
$$

Asumamos que 

$$
n=1,2,…
$$ 

Desarrollemos un reconocedor de caadenas que acepte las cadenas de este mismo lenguaje.  Usemos Python junto con la librería PLY para implementar tal reconocedor.

## Tokens

Los tokens que se usan para reconocer las cadenas son los siguientes:

```python
tokens = ['ABC', 'PIZQ', 'PDER', 'ENTER']

t_ABC = r'abc'
t_PIZQ = r'\('
t_PDER = r'\)'
t_ENTER = r'\n'
```

## Gramática

La gramática que genera el lenguaje es la siguiente:

$$
S \rightarrow E_1 \newline
E_1 \rightarrow PIZQ E_2 \newline
E_2 \rightarrow E_1 PDER | ABC
$$

## Ejecución

Para ejecutar el programa se debe ejecutar el siguiente comando:

```bash
python3 parser.py
```

## Ejemplos

Entrada

```bash
abc
```

Salida

```bash
La cadena ingresada no pertenece al lenguaje.
```

Entrada

```bash
(abc)
```

Salida

```bash

La cadena ingresada no pertenece al lenguaje.
```

Entrada

```bash
((abc)
```

Salida

```bash
La cadena ingresada pertenece al lenguaje.
```

## Streamlit

Se puede acceder a la aplicación web en el siguiente [enlace](https://share.streamlit.io/alejandrogalaz1/reconocedor-de-cadenas/main/app.py).