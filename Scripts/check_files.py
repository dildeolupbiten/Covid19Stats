# -*- coding: utf-8 -*-

from .modules import exists
from .copy_files import copy
from .constants import CONFIRMED, DEATHS, RECOVERED
            

def check():
    if not all([exists(CONFIRMED), exists(DEATHS), exists(RECOVERED)]):
        copy(source="Latest_Files", target=".", filename=CONFIRMED)
        copy(source="Latest_Files", target=".", filename=DEATHS)
        copy(source="Latest_Files", target=".", filename=RECOVERED)
