# -*- coding: utf-8 -*-

from .modules import csv


def read_csv_file(filename: str = ""):
    return [row for row in csv.reader(open(filename))]


