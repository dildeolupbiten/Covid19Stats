# -*- coding: utf-8 -*-

from .modules import ssl, urlopen
from .constants import (
    CONFIRMED, DEATHS, RECOVERED, 
    URL_CONFIRMED, URL_DEATHS, URL_RECOVERED
)


def copy_files(source: str = "", target: str = "", filename: str = ""):
    with open(file=f"{source}/{filename}", mode="rb") as read:
        with open(file=f"{target}/{filename}", mode="wb") as write:
            write.write(read.read())


def get_data(url: str = ""):
    try:
        return urlopen(
            url=url,
            context=ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        ).read()
    except:
        return

def write_content(filename: str = "", url: str = ""):
    data = get_data(url=url)
    if not data:
        copy_files(source="Latest_Files", target=".", filename=filename)
    else:
        if data != open(f"Latest_Files/{filename}", "rb").read():
            with open(filename, "wb") as csv:
                csv.write(data)
            copy_files(source=".", target="Latest_Files", filename=filename)
        else:
            copy_files(source="Latest_Files", target=".", filename=filename)


def download():   
    write_content(filename=CONFIRMED, url=URL_CONFIRMED)
    write_content(filename=DEATHS, url=URL_DEATHS)
    write_content(filename=RECOVERED, url=URL_RECOVERED)
