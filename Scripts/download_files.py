# -*- coding: utf-8 -*-

from .copy_files import copy
from .modules import BS, requests, exists, listdir
from .constants import CONFIRMED, DEATHS, RECOVERED


def write_content(name: str = "", filename: str = "", links: tuple = ()):
    item = next(links)
    if "global" in item.lower() and name in item.lower():
        if requests.get(item).content != \
                open(f"Latest_Files/{filename}", "rb").read():
            with open(filename, "wb") as csv:
                csv.write(requests.get(item).content)


def download():   
    html = BS(
        requests.get(
            "https://data.humdata.org/m/dataset/"
            "novel-coronavirus-2019-ncov-cases"
        ).text, 
        "html.parser"
    )
    links = (
        "https://data.humdata.org" + i["href"] 
        for i in html.select('a[title="Download"]')
    )
    write_content(name="confirmed", filename=CONFIRMED, links=links)
    write_content(name="deaths", filename=DEATHS, links=links)
    write_content(name="recovered", filename=RECOVERED, links=links)
    if all([exists(CONFIRMED), exists(DEATHS), exists(RECOVERED)]):
        copy(source=".", target="Latest_Files", filename=CONFIRMED)
        copy(source=".", target="Latest_Files", filename=DEATHS)
        copy(source=".", target="Latest_Files", filename=RECOVERED)     
