#!/usr/bin/python
# -*- coding: utf-8 -*-

# import shutil
import csv
import re
from overrides import *
from sdg import open_sdg

INDEX_NAME = "indice.csv"


def create_index_csv():
    """
    Método que generará el índice para la correlación de cada serie con su nombre.
    """
    with open('data/%s' % INDEX_NAME, 'w', newline='', encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Indicador', 'Nombre'])
        with open('translations/es/subindicator.yml', 'r', encoding="utf-8") as translations_file:
            for line in translations_file.readlines():
                match = re.search(r'(.*)-nombre:\s?"(.*)"', line)
                if match:
                    csv_writer.writerow([str(match.groups()[0]), str(match.groups()[1])])


if __name__ == "__main__":
    # Validate the indicators.
    print("Validando datos...")
    validation_successful = open_sdg.open_sdg_check(config='config_data.yml')

    # If everything was valid, perform the build.
    if not validation_successful:
        raise Exception('There were validation errors. See output above.')
    else:
        print("Creando índice...")
        create_index_csv()
        print("Construyendo datos...")
        open_sdg.open_sdg_build(config='config_data.yml')