#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: JulianMazo, CristianZapata & HaroldGonzález
This code uses certain data to create a CART or ID3 decision tree.
With this tree, it will be able to make prediction of future data.
Uses Graphviz to graph the tree.
"""

# IMPORT LIBRARIES

import os  # To facilitate interaction with users.
import pandas as pd  # To read the .csv files and put the DataFrames in arrays of arrays.
import cProfile  # To calculate the time profile of the algorithm.

# READ DATASETS

#O(n*m)
def read_csv():
    """ Reads a .csv file with certain data and creates a matrix with the data.

    :return: a tuple with a matrix and the labels of certain data.
    :rtype: tuple
    """
    os.system("cls")
    file = str(input("\nEnter the name of the .csv file to read: "))
    dataset = pd.read_csv(file, sep = ';')  # Reads the Dataset.

    try:
        filt = int(input("\nEnter 1 to filter the data, another key to continue: "))
        if filt == 1:
            dataset = filter(dataset)
    except(ValueError):
        print()

    labels = dataset.columns.tolist()  # Creates the list of labels.
    data = dataset.values.tolist()  # Creates the matrix with the data.
    print()
    os.system("pause")
    return data, labels

#O(n)
def filter(dataset):
    """ Prints a menu and calls a filter function given by the user.

    :param dataset: a DataFrame object.
    :type dataset: DataFrame
    :return: the filtered DataFrame.
    :rtype: DataFrame
    """
    switcher = {  # Emulates the structure switch-cases of Java language.
        1: filt_score,
        2: drop_na,
        3: filt_manual,
        4: cancel
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
    func = switcher.get(case, lambda: cancel)
    dataset = func(dataset)
    return dataset

#O(1)
def filt_score(dataset):
    """ Filters a dataset by scores.

    :param dataset: a DataFrame object.
    :type dataset: DataFrame
    :return: the filtered DataFrame.
    :rtype: DataFrame
    """
    dataset = dataset[["punt_lenguaje", "punt_matematicas", "punt_biologia", "punt_quimica", "punt_fisica", "punt_ciencias_sociales", "punt_filosofia", "punt_ingles", "exito"]]
    return dataset

#O(1)
def drop_na(dataset):
    """ Drops the columns of a dataset that have null values.

    :param dataset: a DataFrame object.
    :type dataset: DataFrame
    :return: the filtered DataFrame.
    :rtype: DataFrame
    """
    dataset = dataset.dropna(axis = 1)
    return dataset

#O(n)
def filt_manual(dataset):
    """ Drops columns of a dataset given by the user.

    :param dataset: a DataFrame object.
    :type dataset: DataFrame
    :return: the filtered DataFrame.
    :rtype: DataFrame
    """
    col = ""
    while col != "*":
        os.system("cls")
        col = str(input("Ingrese el nombre de la columna a eliminar o '*' para cancelar: " ))
        try:
            dataset = dataset.drop(columns = [col])
        except(KeyError):
            continue
    return dataset

#O(1)
def cancel(dataset):
    """ Cancels the filter operation.

    :param dataset: a DataFrame object.
    :type dataset: DataFrame
    :return: the same DataFrame.
    :rtype: DataFrame
    """
    return dataset

# TESTING TIME.
"""
def testing_read_csv(file):
    dataset = pd.read_csv(file, sep = ';')
    labels = dataset.columns.tolist()
    data = dataset.values.tolist()
    return data, labels

#cProfile.run('testing_read_csv("TRAIN 4.csv")')
"""
