# -*- coding: utf-8 -*-

from .copy_files import copy
from .modules import ssl, urlopen, exists, listdir
from .constants import (
    CONFIRMED, DEATHS, RECOVERED, 
    URL_CONFIRMED, URL_DEATHS, URL_RECOVERED
)


def get_data(url: str = ""):
    return urlopen(
        url=url,
        context=ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    )

def write_content(name: str = "", filename: str = "", url: str = ""):
    data = get_data(url=url).read()
    if data != open(f"Latest_Files/{filename}", "rb").read():
        with open(filename, "wb") as csv:
            csv.write(data)
        copy(source=".", target="Latest_Files", filename=filename)


def download():   
    write_content(name="confirmed", filename=CONFIRMED, url=URL_CONFIRMED)
    write_content(name="deaths", filename=DEATHS, url=URL_DEATHS)
    write_content(name="recovered", filename=RECOVERED, url=URL_RECOVERED)
