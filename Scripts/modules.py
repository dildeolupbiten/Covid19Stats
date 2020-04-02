# -*- coding: utf-8 -*-

import csv
import ssl
import tkinter as tk
import matplotlib.pyplot as plt

from numpy import array
from os import listdir
from os.path import exists
from statistics import mean

from urllib.request import urlopen
from datetime import datetime as dt
from tkinter.ttk import Treeview as Tv
from tkinter.messagebox import showinfo
from xlsxwriter.workbook import Workbook
from tkinter.filedialog import askopenfilename as ask

