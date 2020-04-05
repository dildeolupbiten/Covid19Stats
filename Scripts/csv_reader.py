# -*- coding: utf-8 -*-

from .modules import csv


def read_csv_file(filename: str = ""):
    data = []
    countries = []
    for index, row in enumerate(csv.reader(open(filename))):
        if row[1] not in countries:
            data.append(row[1:])
            countries.append(row[1])
    return data
