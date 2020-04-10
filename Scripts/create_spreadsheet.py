# -*- coding: utf-8 -*-

from .modules import Workbook, showinfo


class Spreadsheet(Workbook):
    def __init__(
            self, 
            columns: tuple = (), 
            data: tuple = (),
            *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.sheet = self.add_worksheet()
        self.cols = [
            "A", "B", "C", 
            "D", "E", "F", 
            "G", "H", "I", 
            "J", "K", "L",
            "M", "N", "O",
            "P", "Q", "R"
        ]
        self.columns = columns
        self.data = data
        self.write()
        self.close()
        showinfo(title="Export", message="Data are exported.")
        
    def format(
            self,
            bold: bool = False,
            align: str = "",
            font_name: str = "Arial",
            font_size: int = 11
    ):
        return self.add_format(
            {
                "bold": bold,
                "align": align,
                "valign": "vcenter",
                "font_name": font_name,
                "font_size": font_size
            }
        )
        
    def write(self):
        n = 0
        for i in self.columns:
            self.sheet.merge_range(
                f"{self.cols[n]}1:{self.cols[n + 2]}1",
                i,
                self.format(align="center", bold=True)
            )
            n += 3
        for i, cols in enumerate(self.data, 2):
            n = 0
            for col in cols:
                self.sheet.merge_range(
                    f"{self.cols[n]}{i}:{self.cols[n + 2]}{i}",
                    col,
                    self.format(align="center")
                )
                n += 3
