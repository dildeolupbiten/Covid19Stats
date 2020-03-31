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
            sequence="<Button-3>",
            func=lambda event: self.entry.popup(
                event=event,
                func=self.button_3_on_entry
            )
        )
        
    def button_3_on_entry(self):
        view = tk.Menu(master=self.entry.right_click, tearoff=False)
        proportion = tk.Menu(master=self.entry.right_click, tearoff=False)
        self.entry.right_click.add_cascade(
            label="View Case Graphs",
            menu=view
        )
        self.entry.right_click.add_cascade(
            label="View Proportion Graphs",
            menu=proportion
        )
        view.add_command(
            label="Confirmed",
            command=lambda: self.view_data(
                data=self.treeview.confirmed_data,
                title="Confirmed"
            )
        )
        view.add_command(
            label="Deaths",
            command=lambda: self.view_data(
                data=self.treeview.deaths_data,
                title="Deaths"
            )
        )
        view.add_command(
            label="Recovered",
            command=lambda: self.view_data(
                data=self.treeview.recovered_data,
                title="Recovered"
            )
        )
        proportion.add_command(
            label="Deaths/Confirmed",
            command=lambda: self.view_data(
                data=[
                    self.treeview.confirmed_data, 
                    self.treeview.deaths_data
                ],
                title="Deaths/Confirmed",
                proportion=True
            )
        )
        proportion.add_command(
            label="Recovered/Confirmed",
            command=lambda: self.view_data(
                data=[
                    self.treeview.confirmed_data, 
                    self.treeview.recovered_data
                ],
                title="Recovered/Confirmed",
                proportion=True
            )
        )
        proportion.add_command(
            label="Recovered/Deaths",
            command=lambda: self.view_data(
                data=[
                    self.treeview.deaths_data, 
                    self.treeview.recovered_data
                ],
                title="Recovered/Deaths",
                proportion=True
            )
        )
        
    @staticmethod
    def proportion(x=None, y=None):
        if not all([x, y]):
            x = []
            y = []
        result = []
        for i in range(len(x)):
            try:
                result.append(x[i] / y[i] * 100)
            except ZeroDivisionError:
                result.append(0)
        return result    
              
    def view_data(self, data=None, title: str = "", proportion: bool = False):
        if not data:
            data = []
        if self.treeview.selection():
            item = self.treeview.item(self.treeview.selection())["values"]
            if proportion:
                data, _data = data[0], data[1]
                values = [(), ()]
                for i, j in enumerate(data[1:]):
                    if item[1] == j[1]:
                        values[0] = [int(k) for k in j[4:]]
                for i, j in enumerate(_data[1:]):
                    if item[1] == j[1]:
                        values[1] = [int(k) for k in j[4:]]
                plot_data(
                    x=self.treeview.times, 
                    y=self.proportion(
                        x=tuple(values[1]),
                        y=tuple(values[0]),
                    ),
                    country=item[1],
                    title=title
                )  
            else:
                data, _data = data, None
                for i, j in enumerate(data[1:]):
                    if item[1] == j[1]:
                        plot_data(
                            x=self.treeview.times, 
                            y=tuple([int(k) for k in j[4:]]),
                            country=item[1],
                            title=title
                        )

