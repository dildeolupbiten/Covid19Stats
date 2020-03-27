#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Scripts.modules import tk
from Scripts.frame import Frame
from Scripts.check_files import check
from Scripts.download_files import download


def main():
    download()
    check()
    root = tk.Tk()
    root.title("Covid19Stats")
    root.resizable(width=False, height=False)
    Frame(master=root).mainloop()


if __name__ == "__main__":
    main()
