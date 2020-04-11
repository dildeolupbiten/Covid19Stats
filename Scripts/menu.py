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
        self.increase_rate_cases = tk.Menu(
            master=self.master,
            tearoff=False
        )
        self.increase_rate_proportions = tk.Menu(
            master=self.master,
            tearoff=False
        )
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
        self.increase_rate.add_cascade(
            label="Case Rates",
            menu=self.increase_rate_cases
        )
        self.increase_rate.add_cascade(
            label="Proportion Rates",
            menu=self.increase_rate_proportions
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
        self.increase_rate_cases.add_command(
            label="Confirmed",
            command=lambda: self.view_data(
                data=self.treeview.confirmed_data,
                title="Confirmed",
                select="increase_rate"
            )
        )
        self.increase_rate_cases.add_command(
            label="Deaths",
            command=lambda: self.view_data(
                data=self.treeview.deaths_data,
                title="Deaths",
                select="increase_rate"
            )
        )
        self.increase_rate_cases.add_command(
            label="Recovered",
            command=lambda: self.view_data(
                data=self.treeview.recovered_data,
                title="Recovered",
                select="increase_rate"
            )
        )
        self.increase_rate_proportions.add_command(
            label="Deaths/Confirmed",
            command=lambda: self.view_data(
                data=[
                    self.treeview.confirmed_data,
                    self.treeview.deaths_data
                ],
                title="Deaths/Confirmed",
                select="increase_rate_proportion"
            )
        )
        self.increase_rate_proportions.add_command(
            label="Recovered/Confirmed",
            command=lambda: self.view_data(
                data=[
                    self.treeview.confirmed_data,
                    self.treeview.recovered_data
                ],
                title="Recovered/Confirmed",
                select="increase_rate_proportion"
            )
        )
        self.increase_rate_proportions.add_command(
            label="Recovered/Deaths",
            command=lambda: self.view_data(
                data=[
                    self.treeview.deaths_data,
                    self.treeview.recovered_data
                ],
                title="Recovered/Deaths",
                select="increase_rate_proportion"
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
    def find_proportion(x: list = [], y: list = []):
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
    
    def predict(
            self,
            case: int = 0,
            day: int = 0,
            increase: float = .0,
            proportion: bool = False
    ):
        if not day:
            if not proportion:
                return int(case)
            else:
                return round(case, 2)
        else:
            return self.predict(
                case=case + (case * increase / 100),
                day=day - 1,
                increase=increase,
                proportion=proportion
            )

    @staticmethod
    def deviation_percent(observed: float = .0, expected: float = .0):
        return f"{round((expected - observed) * 100 / expected, 2)} %"

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

    def get_values_for_proportion(
            self, data: list = [],
            items: list = [],
            compare: bool = False
    ):
        data1, data2 = data[0], data[1]
        return self.get_values(
            items=items,
            data=data1,
            compare=compare
        ), self.get_values(
            items=items,
            data=data2,
            compare=compare
        )

    def create_toplevel(
            self, title: str = "",
            countries: str = "",
            values: list = [],
            proportion: bool = False
    ):
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
            "Prediction of the next day",
            "Deviation Percent"
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
            if ind == 0:
                deviation = "0 %"
            else:
                try:
                    deviation = self.deviation_percent(
                        observed=values[ind],
                        expected=self.predict(
                            case=values[ind - 1],
                            day=1,
                            increase=mean[-1],
                            proportion=proportion
                        )
                    )
                except:
                    deviation = "0 %"
            mean.append(increase_rate)
            if proportion:
                j_ = round(j_, 2)
            prediction = self.predict(
                case=j_,
                day=1,
                increase=increase_rate,
                proportion=proportion
            )
            row_data = [
                i_.strftime('%Y.%m.%d'),
                j_,
                f"{round(increase_rate, 2)} %",
                f"{round(sum(mean) / len(mean), 2)} %",
                prediction,
                deviation
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
                filename=f'{countries}_{title.replace("/", "-")}.xlsx',
                columns=columns,
                data=all_data
            )
        )
        button.pack(side="bottom")

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
                value1, value2 = self.get_values_for_proportion(
                    data=data,
                    items=items
                )
                plot_data(
                    x=self.treeview.times, 
                    y=self.find_proportion(
                        x=value2,
                        y=value1,
                    ),
                    country=countries,
                    title=title
                )
            elif select == "proportion-compare":
                value1, value2 = self.get_values_for_proportion(
                    data=data,
                    items=items,
                    compare=True
                )
                if 2 <= len(value1) < 6:
                    plot_data(
                        x=self.treeview.times,
                        y=self.find_proportion(
                            x=value2,
                            y=value1,
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
                values = self.get_values(data=data, items=items)
                self.create_toplevel(
                    title=title,
                    countries=countries,
                    values=values
                )
            elif select == "increase_rate_proportion":
                y, x = self.get_values_for_proportion(
                    data=data,
                    items=items
                )
                values = self.find_proportion(x=x, y=y)
                self.create_toplevel(
                    title=title,
                    countries=countries,
                    values=values,
                    proportion=True
                )
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
