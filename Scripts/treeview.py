# -*- coding: utf-8 -*-

from .modules import tk, Tv


class Treeview(Tv):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill="y")
        self.y_scrollbar = tk.Scrollbar(
            master=self.master,
            orient=tk.VERTICAL,
        )
        self.configure(yscrollcommand=self.y_scrollbar.set)
        self.y_scrollbar.configure(command=self.yview)
        self.y_scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.columns = [
            "Province/State",
            "Country/Region",
            "Latitude",
            "Longitude"
        ]
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
                width=140,
                anchor=tk.CENTER
            )
            self._heading(
                treeview=self,
                col=i,
                text=j
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

