"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    total = 0
    with open("data.csv", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            value = int(fields[1])
            total += value
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return total


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    registros = {}

    with open("data.csv", "r") as file:
        for line in file:
            letter = line.strip().split("\t")[0]
            registros[letter] = registros.get(letter, 0) + 1

    lista_tuplas = sorted(registros.items())

    return lista_tuplas


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    suma_letras = {}

    with open("data.csv", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            letter = fields[0]
            value = int(fields[1])
            suma_letras[letter] = suma_letras.get(letter, 0) + value

    lista_tuplas = sorted(suma_letras.items())

    return lista_tuplas
    return


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    registros_por_mes = {}

    with open("data.csv", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            date = fields[2]
            month = date.split("-")[1]

            if month in registros_por_mes:
                registros_por_mes[month] += 1
            else:
                registros_por_mes[month] = 1

    lista_tuplas = []
    for month in sorted(registros_por_mes.keys()):
        count = registros_por_mes[month]
        lista_tuplas.append((month, count))

    return lista_tuplas


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    valores_extremos = {}

    with open("data.csv", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            letter = fields[0]
            value = int(fields[1])

            if letter in valores_extremos:
                max_val, min_val = valores_extremos[letter]
                valores_extremos[letter] = (max(max_val, value), min(min_val, value))
            else:
                valores_extremos[letter] = (value, value)

    lista_tuplas = []
    for letter in sorted(valores_extremos.keys()):
        max_value, min_value = valores_extremos[letter]
        lista_tuplas.append((letter, max_value, min_value))

    return lista_tuplas


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    valores_max = {}
    valores_min = {}

    with open("data.csv", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            encoded_dict = fields[4]

            pairs = encoded_dict.split(",")
            for pair in pairs:
                key, value = pair.split(":")
                value = int(value)

                if key in valores_max:
                    valores_max[key] = max(valores_max[key], value)
                else:
                    valores_max[key] = value

                if key in valores_min:
                    valores_min[key] = min(valores_min[key], value)
                else:
                    valores_min[key] = value

    lista_tuplas = []
    for key in sorted(valores_max.keys()):
        max_value = valores_max[key]
        min_value = valores_min[key]
        lista_tuplas.append((key, min_value, max_value))

    return lista_tuplas


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    asociaciones = {}

    with open("data.csv", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            value = int(fields[1])
            letter = fields[0]

            if value in asociaciones:
                asociaciones[value].append(letter)
            else:
                asociaciones[value] = [letter]

    lista_tuplas = []
    for value, letters in sorted(asociaciones.items()):
        lista_tuplas.append((value, letters))

    return lista_tuplas


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    valores_letras = {}

    with open("data.csv", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            value = int(fields[1])
            letter = fields[0]

            if value in valores_letras:
                if letter not in valores_letras[value]:
                    valores_letras[value].append(letter)
            else:
                valores_letras[value] = [letter]

    lista_tuplas = []
    for value, letters in sorted(valores_letras.items()):
        lista_tuplas.append((value, sorted(letters)))

    return lista_tuplas


def pregunta_09():
    """
        Retorne un diccionario que contenga la cantidad de registros en que aparece cada
        clave de la columna 5.
    
        Rta/
        {
            "aaa": 13,
            "bbb": 16,
            "ccc": 23,
            "ddd": 23,
            "eee": 15,
            "fff": 20,
            "ggg": 13,
            "hhh": 16,
            "iii": 18,
            "jjj": 18,
        }

    """
    registros_por_clave = {}

    with open("data.csv", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            column5 = fields[4]

            pairs = column5.split(",")
            for pair in pairs:
                key, _ = pair.split(":")
                if key in registros_por_clave:
                    registros_por_clave[key] += 1
                else:
                    registros_por_clave[key] = 1

    return registros_por_clave
    

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista_tuplas = []

    with open("data.csv", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            letter = fields[0]
            column4 = fields[3]
            column5 = fields[4]

            elements_column4 = len(column4.split(","))
            elements_column5 = len(column5.split(","))

            lista_tuplas.append((letter, elements_column4, elements_column5))

    return lista_tuplas


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    suma_por_letra = {}

    with open("data.csv", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            letter_column4 = fields[3]
            value_column2 = int(fields[1])

            letters = letter_column4.split(",")
            for letter in letters:
                if letter in suma_por_letra:
                    suma_por_letra[letter] += value_column2
                else:
                    suma_por_letra[letter] = value_column2

    suma_por_letra_ordenada = {k: v for k, v in sorted(suma_por_letra.items())}

    return suma_por_letra_ordenada


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    diccionario_suma = {}

    with open("data.csv", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            letter_column1 = fields[0]
            column5 = fields[4]

            pairs = column5.split(",")
            for pair in pairs:
                _, value = pair.split(":")
                value = int(value)

                if letter_column1 in diccionario_suma:
                    diccionario_suma[letter_column1] += value
                else:
                    diccionario_suma[letter_column1] = value

    return diccionario_suma
