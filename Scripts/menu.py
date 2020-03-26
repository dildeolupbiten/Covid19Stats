# -*- coding: utf-8 -*- 

from .modules import dt, tk, Tv, ask
from .csv_reader import read_csv_file


class Menu(tk.Menu):
    def __init__(self, treeview: Tv = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master.configure(menu=self)
        self.treeview = treeview
        self.file = tk.Menu(master=self, tearoff=False)
        self.add_cascade(label="File", menu=self.file)
        self.file.add_command(label="Open", command=self.open)
        self.filename = None
        self.data = None
        self.times = None
        
    def open(self):
        try:
            self.filename = ask(filetypes=[("CSV Files", ".csv")])
            self.data = read_csv_file(filename=self.filename)
            self.times = tuple(
                dt.strptime(i + "20", "%m/%d/%Y") for i in self.data[0][4:]
            )
            columns = [i[:4] for i in self.data[1:]]
            for i, j in enumerate(self.data[1:]):
                self.treeview.insert(
                    parent="",
                    index=i,
                    values=[j if j else None for j in columns[i]]
                )
        except (FileNotFoundError, TypeError):
            pass
