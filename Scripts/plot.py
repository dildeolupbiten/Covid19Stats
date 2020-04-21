# -*- coding: utf-8 -*-

from .modules import plt, mean, array
   
    
def plot_data(
        x: tuple = (), 
        y: tuple = (),
        country: str = "",
        title: str = "",
        compare: bool = False
):
    x = array(x)
    if compare:
        y = [array(i) for i in y]
    else:
        y = [array(y)]
    ax = plt.subplot2grid((1, 1), (0, 0))
    colors = [
        "#F005D1",
        "#0525F0",
        "#5EFF00",
        "#F7FF00",
        "#FF8900",
    ]
    countries = country.split(",")
    for i in range(len(y)):
        ax.plot_date(
            x=x,
            y=y[i],
            fmt="-",
            color=colors[i],
            label=countries[i].split("(")[0],
            linewidth=0.7
        )
        if not compare:
            ax.fill_between(
                x,
                y[i],
                mean(y[i]),
                where=(y[i] > mean(y[i])),
                color="green",
                alpha=0.7,
                label="above average"
            )
            ax.fill_between(
                x,
                y[i],
                mean(y[i]),
                where=(y[i] < mean(y[i])),
                color="red",
                alpha=0.7,
                label="below average"
            )
            ax.axhline(mean(y[i]), color="cyan", linewidth=2)
        for label in ax.xaxis.get_ticklabels():
            label.set_rotation(45)
        ax.tick_params(axis="x", colors="red")
        ax.tick_params(axis="y", colors="purple")
    plt.grid(
        True,
        color="black",
        linestyle="-",
        linewidth=1
    )
    plt.subplots_adjust(
        left=0.2,
        bottom=0.2,
        right=0.9,
        top=0.9,
        wspace=0.2,
        hspace=0
    )
    plt.xlabel("Timeline")
    plt.ylabel(title)
    plt.title(country)
    plt.legend()
    plt.show()
