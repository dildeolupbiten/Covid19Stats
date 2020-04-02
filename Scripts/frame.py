# -*- coding: utf-8 -*-

from .menu import Menu
from .modules import tk
from .entry import Entry
from .treeview import Treeview


class Frame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(side="bottom")
        self.menu = None
        self.treeview = Treeview(
            master=self, 
            columns=(
                "Province/State",
                "Country/Region",
                "Latitude",
                "Longitude"
            ),
            csv=True
        )
        self.entry = Entry(master=self.master, treeview=self.treeview)
        self.treeview.bind(
            sequence="<Button-3>",
            func=lambda event: self.entry.popup(
                event=event,
                func=self.button_3_on_entry
            )
        )
        
    def button_3_on_entry(self):
        self.menu = Menu(
            master=self.entry.right_click, 
            treeview=self.treeview
        )
