# -*- coding: utf-8 -*-

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
        self.treeview.bind(
            sequence="<Double-Button-1>",
            func=lambda event: self.double_button1_on_treeview()
        )
        
    def double_button1_on_treeview(self):
        if self.treeview.selection():
            item = self.treeview.item(self.treeview.selection())["values"]
            for confirmed, deaths, recovered in zip(
                    self.treeview.confirmed_data[1:],
                    self.treeview.deaths_data[1:],
                    self.treeview.recovered_data[1:]
            ):
                if item[1] == confirmed[1]:
                    plot_data(
                        x=self.treeview.times, 
                        y1=tuple([int(i) for i in confirmed[4:]]),
                        y2=tuple([int(i) for i in deaths[4:]]),
                        y3=tuple([int(i) for i in recovered[4:]]),
                        title=item[1],
                    )
