# -*- coding: utf-8 -*-

from .modules import plt, mean, array
   
    
def plot_data(
        x: tuple = (), 
        y1: tuple = (),
        y2: tuple = (),
        y3: tuple = (),
        title: str = "",
):
    x = array(x)
    y = [array(y1), array(y2), array(y3)]
    titles = ["Confirmed", "Deaths", "Recovered"]
    axes = [
        plt.subplot2grid((2, 1), (0, 0)),
        plt.subplot2grid((2, 2), (1, 0)),
        plt.subplot2grid((2, 2), (1, 1))
    ]
    for i, ax in enumerate(axes):
        if i == 0:
            ax.set_title(title)
        ax.plot_date(
            x=x,
            y=y[i],
            fmt="-",
            color="black",
            label=titles[i],
            linewidth=0.7
        )
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
        for label in ax.xaxis.get_ticklabels():
            label.set_rotation(45)
        ax.tick_params(axis="x", colors="red")
        ax.tick_params(axis="y", colors="purple")
        ax.axhline(mean(y[i]), color="cyan", linewidth=2)
        ax.set_xlabel('Timeline')
        ax.set_ylabel(titles[i])
        ax.legend()
        ax.grid(
            True,
            color="black",
            linestyle="-",
            linewidth=1,
            alpha=0.2,
        )
        ax.figure.tight_layout()
    plt.gcf().set_size_inches(18.5, 10.5)
    plt.show()
