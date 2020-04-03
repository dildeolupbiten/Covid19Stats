# -*- coding: utf-8 -*-

from .modules import tk
from .plot import plot_data
from .treeview import Treeview
from .create_spreadsheet import Spreadsheet


class Menu:
    def __init__(self, master, treeview):
        self.master = master
        self.treeview = treeview
        self.view = tk.Menu(master=self.master, tearoff=False)
        self.proportion = tk.Menu(master=self.master, tearoff=False)
        self.increase_rate = tk.Menu(master=self.master, tearoff=False)
        self.master.add_cascade(
            label="View Case Graphs",
            menu=self.view
        )
        self.master.add_cascade(
            label="View Proportion Graphs",
            menu=self.proportion
        )
        self.master.add_cascade(
            label="View Increase Rate",
            menu=self.increase_rate
        )
        self.view.add_command(
            label="Confirmed",
            command=lambda: self.view_data(
                data=self.treeview.confirmed_data,
                title="Confirmed",
                select="view"
            )
        )
        self.view.add_command(
            label="Deaths",
            command=lambda: self.view_data(
                data=self.treeview.deaths_data,
                title="Deaths",
                select="view"
            )
        )
        self.view.add_command(
            label="Recovered",
            command=lambda: self.view_data(
                data=self.treeview.recovered_data,
                title="Recovered",
                select="view"
            )
        )
        self.proportion.add_command(
            label="Deaths/Confirmed",
            command=lambda: self.view_data(
                data=[
                    self.treeview.confirmed_data, 
                    self.treeview.deaths_data
                ],
                title="Deaths/Confirmed",
                select="proportion"
            )
        )
        self.proportion.add_command(
            label="Recovered/Confirmed",
            command=lambda: self.view_data(
                data=[
                    self.treeview.confirmed_data, 
                    self.treeview.recovered_data
                ],
                title="Recovered/Confirmed",
                select="proportion"
            )
        )
        self.proportion.add_command(
            label="Recovered/Deaths",
            command=lambda: self.view_data(
                data=[
                    self.treeview.deaths_data, 
                    self.treeview.recovered_data
                ],
                title="Recovered/Deaths",
                select="proportion"
            )
        )
        self.increase_rate.add_command(
            label="Confirmed",
            command=lambda: self.view_data(
                data=self.treeview.confirmed_data,
                title="Confirmed",
                select="increase_rate"
            )
        )
        self.increase_rate.add_command(
            label="Deaths",
            command=lambda: self.view_data(
                data=self.treeview.deaths_data,
                title="Deaths",
                select="increase_rate"
            )
        )
        self.increase_rate.add_command(
            label="Recovered",
            command=lambda: self.view_data(
                data=self.treeview.recovered_data,
                title="Recovered",
                select="increase_rate"
            )
        )
        
    @staticmethod
    def find_proportion(x=None, y=None):
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
    
    def predict(self, case, increase, day):
        if not day:
            return int(case)
        else:
            return self.predict(
                case + (case * increase / 100), 
                increase, 
                day - 1
            )             
              
    def view_data(
            self, 
            data=None, 
            title: str = "", 
            select: str = ""
    ):
        if not data:
            data = []
        if self.treeview.selection():
            item = self.treeview.item(self.treeview.selection())["values"]
            if select == "proportion":
                data1, data2 = data[0], data[1]
                values = [(), ()]
                for i, j in enumerate(data1[1:]):
                    if item[1] == j[1]:
                        values[0] = [int(k) for k in j[4:]]
                for i, j in enumerate(data2[1:]):
                    if item[1] == j[1]:
                        values[1] = [int(k) for k in j[4:]]
                plot_data(
                    x=self.treeview.times, 
                    y=self.find_proportion(
                        x=tuple(values[1]),
                        y=tuple(values[0]),
                    ),
                    country=item[1],
                    title=title
                )
            elif select == "increase_rate":
                for i, j in enumerate(data[1:]):
                    if item[1] == j[1]:
                        values = [int(k) for k in j[4:]]
                        toplevel = tk.Toplevel()
                        toplevel.title(f"{item[1]} - {title}")
                        toplevel.resizable(width=False, height=False)
                        frame = tk.Frame(master=toplevel)
                        frame.pack(side="top")
                        columns = (
                            "Date",
                            title,
                            "Increase Percent",
                            "Mean Increase Percent",
                            "Prediction of the next day"
                        )
                        treeview = Treeview(
                            master=frame, 
                            columns=columns,
                            csv=False
                        )
                        mean = []
                        all_data = []
                        for ind, (i, j) in enumerate(
                                zip(self.treeview.times, values)
                        ):
                            try:
                                increase_rate = 100 \
                                    * (values[ind] - values[ind - 1]) \
                                    / values[ind - 1]
                            except:
                                increase_rate = 0
                            if ind == 0:
                                increase_rate = 0
                            mean.append(increase_rate)
                            row_data = [
                                i.strftime('%Y.%m.%d'),
                                j,
                                f"{round(increase_rate, 2)} %",
                                f"{round(sum(mean) / len(mean), 2)} %",
                                f"{self.predict(j, increase_rate, 1)}"
                            ]
                            treeview.insert(
                                parent="",
                                index=ind,
                                values=[k for k in row_data]
                            )
                            all_data.append(row_data)
                        button = tk.Button(
                            master=toplevel, 
                            text="Export",
                            command=lambda: Spreadsheet(
                                filename=f"{item[1]}_{title}.xlsx", 
                                columns=columns,
                                data=all_data
                            ) 
                        )
                        button.pack(side="bottom")
            elif select == "view":
                for i, j in enumerate(data[1:]):
                    if item[1] == j[1]:
                        plot_data(
                            x=self.treeview.times, 
                            y=tuple([int(k) for k in j[4:]]),
                            country=item[1],
                            title=title
                        )
