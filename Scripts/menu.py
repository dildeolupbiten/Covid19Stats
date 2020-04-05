# -*- coding: utf-8 -*-

from .modules import tk, array, showinfo
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
        self.compare = tk.Menu(master=self.master, tearoff=False)
        self.compare_proportion = tk.Menu(master=self.master, tearoff=False)
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
        self.master.add_cascade(
            label="Compare Case Graphs",
            menu=self.compare
        )
        self.master.add_cascade(
            label="Compare Proportion Graphs",
            menu=self.compare_proportion
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
        self.compare.add_command(
            label="Confirmed",
            command=lambda: self.view_data(
                data=self.treeview.confirmed_data,
                title="Confirmed",
                select="view-compare"
            )
        )
        self.compare.add_command(
            label="Deaths",
            command=lambda: self.view_data(
                data=self.treeview.deaths_data,
                title="Deaths",
                select="view-compare"
            )
        )
        self.compare.add_command(
            label="Recovered",
            command=lambda: self.view_data(
                data=self.treeview.recovered_data,
                title="Recovered",
                select="view-compare"
            )
        )
        self.compare_proportion.add_command(
            label="Deaths/Confirmed",
            command=lambda: self.view_data(
                data=[
                    self.treeview.confirmed_data,
                    self.treeview.deaths_data
                ],
                title="Deaths/Confirmed",
                select="proportion-compare"
            )
        )
        self.compare_proportion.add_command(
            label="Recovered/Confirmed",
            command=lambda: self.view_data(
                data=[
                    self.treeview.confirmed_data,
                    self.treeview.recovered_data
                ],
                title="Recovered/Confirmed",
                select="proportion-compare"
            )
        )
        self.compare_proportion.add_command(
            label="Recovered/Deaths",
            command=lambda: self.view_data(
                data=[
                    self.treeview.deaths_data,
                    self.treeview.recovered_data
                ],
                title="Recovered/Deaths",
                select="proportion-compare"
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
                if isinstance(x[i], list):
                    sub = []
                    for j in range(len(x[i])):
                        try:
                            sub.append(x[i][j] / y[i][j] * 100)
                        except ZeroDivisionError:
                            sub.append(0)
                    result.append(sub)
                else:
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

    @staticmethod
    def get_values(items: str = "", data=None, compare: bool = False):
        if not data:
            data = []
        values = []
        if not compare:
            for item in items:
                for i, j in enumerate(data[1:]):
                    if item == j[0]:
                        if isinstance(values, list):
                            values = array(
                                [int(k) for k in j[3:]]
                            )
                        else:
                            values += array(
                                [int(k) for k in j[3:]]
                            )
            return [int(i) for i in values]
        else:
            for item in items:
                for i, j in enumerate(data[1:]):
                    if item == j[0]:
                        values.append([int(k) for k in j[3:]])
            return values
              
    def view_data(
            self, 
            data=None, 
            title: str = "", 
            select: str = ""
    ):
        if not data:
            data = []
        if self.treeview.selection():
            items = [
                self.treeview.item(i)["values"][0]
                for i in self.treeview.selection()
            ]
            countries = ", ".join(items) \
                if len(items) < 6 \
                else f"Selected Countries = {len(items)}"
            if select == "proportion":
                data1, data2 = data[0], data[1]
                values = [[], []]
                values[0] = self.get_values(
                    items=items,
                    data=data1
                )
                values[1] = self.get_values(
                    items=items,
                    data=data2
                )
                plot_data(
                    x=self.treeview.times, 
                    y=self.find_proportion(
                        x=values[1],
                        y=values[0],
                    ),
                    country=countries,
                    title=title
                )
            elif select == "proportion-compare":
                data1, data2 = data[0], data[1]
                values = [[], []]
                values[0] = self.get_values(
                    items=items,
                    data=data1,
                    compare=True
                )
                values[1] = self.get_values(
                    items=items,
                    data=data2,
                    compare=True
                )
                if 2 <= len(values[0]) < 6:
                    plot_data(
                        x=self.treeview.times,
                        y=self.find_proportion(
                            x=values[1],
                            y=values[0],
                        ),
                        country=countries,
                        title=title,
                        compare=True
                    )
                else:
                    showinfo(
                        title="Info",
                        message="The number of selected country "
                                "should be at least 2 "
                                "and at most 5."
                    )
            elif select == "increase_rate":
                values = self.get_values(items=items, data=data)
                toplevel = tk.Toplevel()
                toplevel.title(f"{countries} - {title}")
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
                for ind, (i_, j_) in enumerate(
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
                        i_.strftime('%Y.%m.%d'),
                        j_,
                        f"{round(increase_rate, 2)} %",
                        f"{round(sum(mean) / len(mean), 2)} %",
                        self.predict(j_, increase_rate, 1)
                    ]
                    treeview.insert(
                        parent="",
                        index=ind,
                        values=[k for k in row_data]
                    )
                    all_data.append(row_data)
                countries = countries.replace("=", "-")
                button = tk.Button(
                    master=toplevel,
                    text="Export",
                    command=lambda: Spreadsheet(
                        filename=f'{countries}_{title}.xlsx',
                        columns=columns,
                        data=all_data
                    )
                )
                button.pack(side="bottom")
            elif select == "view":
                values = self.get_values(items=items, data=data)
                plot_data(
                    x=self.treeview.times,
                    y=values,
                    country=countries,
                    title=title,
                )
            elif select == "view-compare":
                values = self.get_values(
                    items=items,
                    data=data,
                    compare=True
                )
                if 2 <= len(values) < 6:
                    plot_data(
                        x=self.treeview.times,
                        y=values,
                        country=countries,
                        title=title,
                        compare=True
                    )
                else:
                    showinfo(
                        title="Info",
                        message="The number of selected country "
                                "should be at least 2 "
                                "and at most 5."
                    )
