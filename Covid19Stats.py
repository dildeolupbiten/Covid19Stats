#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Scripts.modules import tk
from Scripts.frame import Frame


def main():
    root = tk.Tk()
    root.title("Covid19Stats")
    root.resizable(width=False, height=False)
    Frame(master=root).mainloop()


if __name__ == "__main__":
    main()
