# -*- coding: utf-8 -*-

import csv
import tkinter as tk
import requests as requests
import matplotlib.pyplot as plt

from numpy import array
from os import listdir
from os.path import exists
from statistics import mean
from datetime import datetime as dt
from bs4 import BeautifulSoup as BS
from tkinter.ttk import Treeview as Tv
from tkinter.filedialog import askopenfilename as ask
