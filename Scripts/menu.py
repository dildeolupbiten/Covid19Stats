# -*- coding: utf-8 -*-

from .plot import plot_data
from .treeview import Treeview
from .modules import tk, array, showinfo
from .create_spreadsheet import Spreadsheet


class Menu:
    def __init__(self, master, treeview):
        self.master = master
        self.treeview = treeview
        self.total = tk.Menu(master=self.master, tearoff=False)
        self.daily = tk.Menu(master=self.master, tearoff=False)
        for k, v in {self.total: "Total", self.daily: "Daily"}.items():
            self.master.add_cascade(
                label=v,
                menu=k
            )
            self.create_menus(k=k, v=v)

    def create_menus(self, k: tk.Menu = None, v: str = ""):
        view = tk.Menu(master=k, tearoff=False)
        proportion = tk.Menu(master=k, tearoff=False)
        increase_rate = tk.Menu(master=k, tearoff=False)
        increase_rate_cases = tk.Menu(
            master=k,
            tearoff=False
        )
        increase_rate_proportions = tk.Menu(
            master=k,
            tearoff=False
        )
        compare = tk.Menu(master=k, tearoff=False)
        compare_proportion = tk.Menu(master=k, tearoff=False)
        k.add_cascade(
            label="View Case Graphs",
            menu=view
        )
        k.add_cascade(
            label="View Proportion Graphs",
            menu=proportion
        )
        k.add_cascade(
            label="View Increase Rate",
            menu=increase_rate
        )
        k.add_cascade(
            label="Compare Case Graphs",
            menu=compare
        )
        k.add_cascade(
            label="Compare Proportion Graphs",
            menu=compare_proportion
        )
        increase_rate.add_cascade(
            label="Case Rates",
            menu=increase_rate_cases
        )
        increase_rate.add_cascade(
            label="Proportion Rates",
            menu=increase_rate_proportions
        )
        view.add_command(
            label="Confirmed",
            command=lambda: self.view_data(
                data=self.treeview.confirmed_data,
                title="Confirmed",
                select="view",
                daily_or_total=v
            )
        )
        view.add_command(
            label="Deaths",
            command=lambda: self.view_data(
                data=self.treeview.deaths_data,
                title="Deaths",
                select="view",
                daily_or_total=v
            )
        )
        view.add_command(
            label="Recovered",
            command=lambda: self.view_data(
                data=self.treeview.recovered_data,
                title="Recovered",
                select="view",
                daily_or_total=v
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
                select="proportion",
                daily_or_total=v
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
                select="proportion",
                daily_or_total=v
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
                select="proportion",
                daily_or_total=v
            )
        )
        increase_rate_cases.add_command(
            label="Confirmed",
            command=lambda: self.view_data(
                data=self.treeview.confirmed_data,
                title="Confirmed",
                select="increase_rate",
                daily_or_total=v
            )
        )
        increase_rate_cases.add_command(
            label="Deaths",
            command=lambda: self.view_data(
                data=self.treeview.deaths_data,
                title="Deaths",
                select="increase_rate",
                daily_or_total=v
            )
        )
        increase_rate_cases.add_command(
            label="Recovered",
            command=lambda: self.view_data(
                data=self.treeview.recovered_data,
                title="Recovered",
                select="increase_rate",
                daily_or_total=v
            )
        )
        increase_rate_proportions.add_command(
            label="Deaths/Confirmed",
            command=lambda: self.view_data(
                data=[
                    self.treeview.confirmed_data,
                    self.treeview.deaths_data
                ],
                title="Deaths/Confirmed",
                select="increase_rate_proportion",
                daily_or_total=v
            )
        )
        increase_rate_proportions.add_command(
            label="Recovered/Confirmed",
            command=lambda: self.view_data(
                data=[
                    self.treeview.confirmed_data,
                    self.treeview.recovered_data
                ],
                title="Recovered/Confirmed",
                select="increase_rate_proportion",
                daily_or_total=v
            )
        )
        increase_rate_proportions.add_command(
            label="Recovered/Deaths",
            command=lambda: self.view_data(
                data=[
                    self.treeview.deaths_data,
                    self.treeview.recovered_data
                ],
                title="Recovered/Deaths",
                select="increase_rate_proportion",
                daily_or_total=v
            )
        )
        compare.add_command(
            label="Confirmed",
            command=lambda: self.view_data(
                data=self.treeview.confirmed_data,
                title="Confirmed",
                select="view-compare",
                daily_or_total=v
            )
        )
        compare.add_command(
            label="Deaths",
            command=lambda: self.view_data(
                data=self.treeview.deaths_data,
                title="Deaths",
                select="view-compare",
                daily_or_total=v
            )
        )
        compare.add_command(
            label="Recovered",
            command=lambda: self.view_data(
                data=self.treeview.recovered_data,
                title="Recovered",
                select="view-compare",
                daily_or_total=v
            )
        )
        compare_proportion.add_command(
            label="Deaths/Confirmed",
            command=lambda: self.view_data(
                data=[
                    self.treeview.confirmed_data,
                    self.treeview.deaths_data
                ],
                title="Deaths/Confirmed",
                select="proportion-compare",
                daily_or_total=v
            )
        )
        compare_proportion.add_command(
            label="Recovered/Confirmed",
            command=lambda: self.view_data(
                data=[
                    self.treeview.confirmed_data,
                    self.treeview.recovered_data
                ],
                title="Recovered/Confirmed",
                select="proportion-compare",
                daily_or_total=v
            )
        )
        compare_proportion.add_command(
            label="Recovered/Deaths",
            command=lambda: self.view_data(
                data=[
                    self.treeview.deaths_data,
                    self.treeview.recovered_data
                ],
                title="Recovered/Deaths",
                select="proportion-compare",
                daily_or_total=v
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
                                [int(k) for k in j[1:]]
                            )
                        else:
                            values += array(
                                [int(k) for k in j[1:]]
                            )
            return [int(i) for i in values]
        else:
            for item in items:
                for i, j in enumerate(data[1:]):
                    if item == j[0]:
                        values.append([int(k) for k in j[1:]])
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

    @staticmethod
    def daily_or_total(arr: list = []):
        result = []
        for i in range(len(arr)):
            if i != 0:
                result.append(arr[i] - arr[i - 1])
            else:
                result.append(arr[i])
        return result

    def create_toplevel(
            self,
            title: str = "",
            countries: str = "",
            daily_or_total: str = "",
            values: list = [],
            proportion: bool = False
    ):
        toplevel = tk.Toplevel()
        toplevel.title(f"{countries} - {title}")
        toplevel.resizable(width=False, height=False)
        frame = tk.Frame(master=toplevel)
        frame.pack(side="top")
        if daily_or_total == "Total":
            columns = (
                "Date",
                title,
                "Increase Percent",
                "Mean Increase Percent",
                "Prediction of the next day",
                "Deviation Percent"
            )
        else:
            columns = (
                "Date",
                title,
                "Increase Percent",
                "Mean Increase Percent",
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
            prediction = self.predict(
                case=j_,
                day=1,
                increase=increase_rate,
                proportion=proportion
            )
            if proportion:
                j_ = f"{round(j_, 2)} %"
                prediction = f"{prediction} %"
            if daily_or_total == "Total":
                row_data = [
                    i_.strftime('%Y.%m.%d'),
                    j_,
                    f"{round(increase_rate, 2)} %",
                    f"{round(sum(mean) / len(mean), 2)} %",
                    prediction,
                    deviation
                ]
            else:
                row_data = [
                    i_.strftime('%Y.%m.%d'),
                    j_,
                    f"{round(increase_rate, 2)} %",
                    f"{round(sum(mean) / len(mean), 2)} %",
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
            select: str = "",
            daily_or_total: str = ""
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
                if daily_or_total == "Daily":
                    value1 = self.daily_or_total(arr=value1)
                    value2 = self.daily_or_total(arr=value2)
                plot_data(
                    x=self.treeview.times, 
                    y=self.find_proportion(
                        x=value2,
                        y=value1,
                    ),
                    country=f"{countries} ({daily_or_total})",
                    title=title
                )
            elif select == "proportion-compare":
                value1, value2 = self.get_values_for_proportion(
                    data=data,
                    items=items,
                    compare=True
                )
                if daily_or_total == "Daily":
                    for i in range(len(value1)):
                        value1[i] = self.daily_or_total(arr=value1[i])
                        value2[i] = self.daily_or_total(arr=value2[i])
                if 2 <= len(value1) < 6:
                    plot_data(
                        x=self.treeview.times,
                        y=self.find_proportion(
                            x=value2,
                            y=value1,
                        ),
                        country=f"{countries} ({daily_or_total})",
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
                if daily_or_total == "Daily":
                    values = self.daily_or_total(arr=values)
                    self.create_toplevel(
                        title=title,
                        countries=f"{countries} ({daily_or_total})",
                        daily_or_total=daily_or_total,
                        values=values
                    )
                else:
                    self.create_toplevel(
                        title=title,
                        countries=f"{countries} ({daily_or_total})",
                        daily_or_total=daily_or_total,
                        values=values
                    )
            elif select == "increase_rate_proportion":
                y, x = self.get_values_for_proportion(
                    data=data,
                    items=items
                )
                if daily_or_total == "Daily":
                    x = self.daily_or_total(arr=x)
                    y = self.daily_or_total(arr=y)
                    values = self.find_proportion(x=x, y=y)
                    self.create_toplevel(
                        title=title,
                        countries=f"{countries} ({daily_or_total})",
                        daily_or_total=daily_or_total,
                        values=values,
                        proportion=True
                    )
                else:
                    values = self.find_proportion(x=x, y=y)
                    self.create_toplevel(
                        title=title,
                        countries=f"{countries} ({daily_or_total})",
                        daily_or_total=daily_or_total,
                        values=values,
                        proportion=True
                    )
            elif select == "view":
                values = self.get_values(items=items, data=data)
                if daily_or_total == "Daily":
                    values = self.daily_or_total(arr=values)
                plot_data(
                    x=self.treeview.times,
                    y=values,
                    country=f"{countries} ({daily_or_total})",
                    title=title,
                )
            elif select == "view-compare":
                values = self.get_values(
                    items=items,
                    data=data,
                    compare=True
                )
                if daily_or_total == "Daily":
                    for i in range(len(values)):
                        values[i] = self.daily_or_total(arr=values[i])
                if 2 <= len(values) < 6:
                    plot_data(
                        x=self.treeview.times,
                        y=values,
                        country=f"{countries} ({daily_or_total})",
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
