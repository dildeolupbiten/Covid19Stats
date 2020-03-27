# -*- coding: utf-8 -*-


def copy(source: str = "", target: str = "", filename: str = ""):
    with open(file=f"{source}/{filename}", mode="rb") as read:
        with open(file=f"{target}/{filename}", mode="wb") as write:
            write.write(read.read())
