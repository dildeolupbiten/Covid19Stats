# -*- coding: utf-8 -*-

from .menu import Menu
from .modules import tk
from .entry import Entry
from .plot import plot_data
from .treeview import Treeview


class Frame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(side="bottom")
        self.treeview = Treeview(master=self)
        self.entry = Entry(master=self.master, treeview=self.treeview)
        self.menu = Menu(master=self.master, treeview=self.treeview)
        self.data = None
        self.treeview.bind(
            sequence="<Double-Button-1>",
            func=lambda event: self.double_button1_on_treeview()
        )
        
    def double_button1_on_treeview(self):
        if self.treeview.selection():
            item = self.treeview.item(self.treeview.selection())["values"]
            for i in self.menu.data[1:]:
                if item[1] == i[1]:
                    plot_data(
                        x=self.menu.times, 
                        y=tuple([int(j) for j in i[4:]]), 
                        title=item[1]
                    )
                    

