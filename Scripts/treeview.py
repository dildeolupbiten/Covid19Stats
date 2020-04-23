# -*- coding: utf-8 -*-

from .modules import dt, tk, Tv
from .csv_reader import read_csv_file


class Treeview(Tv):
    def __init__(
            self, csv: bool = True, 
            columns: tuple = (), 
            *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.pack(fill="y")
        self.csv = csv
        self.y_scrollbar = tk.Scrollbar(
            master=self.master,
            orient=tk.VERTICAL,
        )
        self.configure(yscrollcommand=self.y_scrollbar.set)
        self.y_scrollbar.configure(command=self.yview)
        self.y_scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.columns = columns
        self.configure(
            show="headings",
            columns=[f"#{i + 1}" for i in range(len(self.columns))],
            height=20,
            selectmode=tk.EXTENDED
        )
        self.pack(side=tk.LEFT)
        for i, j in enumerate(self.columns):
            self.column(
                column=f"#{i + 1}",
                minwidth=100,
                width=210,
                anchor=tk.CENTER
            )
            self._heading(
                treeview=self,
                col=i,
                text=j
            )
        if self.csv:
            self.confirmed = "time_series_covid19_confirmed_global.csv"
            self.deaths = "time_series_covid19_deaths_global.csv"
            self.recovered = "time_series_covid19_recovered_global.csv"
            self.confirmed_data = read_csv_file(filename=self.confirmed)
            self.deaths_data = read_csv_file(filename=self.deaths)
            self.recovered_data = read_csv_file(filename=self.recovered)
            self.times = tuple(
                dt.strptime(i + "20", "%m/%d/%Y") 
                for i in self.confirmed_data[0][1:]
            )
            self.columns = [i[0] for i in self.confirmed_data[1:]]
            for i, j in enumerate(self.confirmed_data[1:]):
                self.insert(
                    parent="",
                    index=i,
                    values=self.columns[i]
                )
            self.bind(
                sequence="<Control-a>",
                func=lambda event: self.select_all()
            )
            self.bind(
                sequence="<Control-A>",
                func=lambda event: self.select_all()
            )

    def _heading(
            self,
            treeview: Tv = None,
            col: int = 0,
            text: str = ""
    ):
        treeview.heading(
            column=f"#{col + 1}",
            text=text,
            command=lambda: self.sort_column(
                treeview=treeview,
                col=col,
                reverse=False
            )
        )

    def sort_column(
            self,
            treeview: Tv = None,
            col: int = 0,
            reverse: bool = False
    ):
        column = [
            (treeview.set(k, col), k)
            for k in treeview.get_children("")
        ]
        try:
            column.sort(key=lambda t: int(t[0]), reverse=reverse)
        except ValueError:
            column.sort(reverse=reverse)
        for index, (val, k) in enumerate(column):
            treeview.move(k, "", index)
        treeview.heading(
            column=col,
            command=lambda: self.sort_column(
                treeview=treeview,
                col=col,
                reverse=not reverse
            )
        )

    def select_all(self):
        for child in self.get_children():
            self.selection_add(child)
