"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    import re

    data = []
    row = None

    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip()

            match = re.match(r"^\s*(\d+)\s+(\d+)\s+([\d,]+)\s+%\s+(.*)$", line)

            if match:
                if row is not None:
                    data.append(row)

                row = [
                    int(match.group(1)),
                    int(match.group(2)),
                    float(match.group(3).replace(",", ".")),
                    match.group(4).strip(),
                ]

            elif row is not None and line.strip() != "":
                row[3] += " " + line.strip()

    if row is not None:
        data.append(row)

    for row in data:
        texto = row[3].strip()
        texto = texto[:-1] if texto.endswith(".") else texto
        texto = re.sub(r"\s+", " ", texto)
        texto = re.sub(r"\s*,\s*", ", ", texto)
        row[3] = texto

    return pd.DataFrame(
        data,
        columns=[
            "cluster",
            "cantidad_de_palabras_clave",
            "porcentaje_de_palabras_clave",
            "principales_palabras_clave",
        ],
    )