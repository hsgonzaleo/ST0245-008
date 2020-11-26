# Reading and managing Datasets.

import os
import pandas as pd

"Reading and storing Datasets"

#O(n)
def read_csv():
    os.system("cls")
    file = str(input("\nIngrese el nombre del archivo .csv a leer: "))
    dataset = pd.read_csv(file, sep = ';')
    try:
        filt = int(input("\nIngrese 1 si desea filtrar los datos: "))
        if filt == 1:
            dataset = filter(dataset)
    except(ValueError):
        print()
    labels = dataset.columns.tolist()
    data = dataset.values.tolist()
    print()
    os.system("pause")
    return data, labels

#O(n)
def filter(dataset):
    switcher = {
        1: filt_punt,
        2: borrar_na,
        3: filt_manual,
        4: cancelar
    }
    case = 0
    while case < 1 or case > 4:
        os.system("cls")
        print("Seleccione el tipo de filtrado.")
        print()
        print("1. Filtrar los datos por los puntajes.")
        print("2. Eliminar las columnas con datos nulos.")
        print("3. Filtrar de manera manual.")
        print("4. Cancelar operación.")
        print()
        try:
            case = int(input())
        except(ValueError):
            case = 5
            print()
            print("Opción inválida. Intente de nuevo")
            print()
            os.system("pause")
    func = switcher.get(case, lambda: cancelar)
    dataset = func(dataset)
    return dataset

def filt_punt(dataset):
    dataset = dataset[["punt_lenguaje", "punt_matematicas", "punt_biologia", "punt_quimica", "punt_fisica", "punt_ciencias_sociales", "punt_filosofia", "punt_ingles", "exito"]]
    return dataset

def borrar_na(dataset):
    dataset = dataset.dropna(axis = 1)
    return dataset

def filt_manual(dataset):
    col = ""
    while col != "*":
        os.system("cls")
        col = str(input("Ingrese el nombre de la columna a eliminar o '*' para cancelar: " ))
        try:
            dataset = dataset.drop(columns = [col])
        except(KeyError):
            continue
    return dataset

def cancelar(dataset):
    return dataset


"""
# Prueba

training_data, header = read_csv()
print(header)"""