# -*- coding: utf-8 -*-

from .modules import plt, mean, array
   
    
def plot_data(
        x: tuple = (), 
        y: tuple = (),
        country: str = "",
        title: str = ""
):
    x = array(x)
    y = array(y)
    ax = plt.subplot2grid((1, 1), (0, 0))
    ax.plot_date(
        x=x,
        y=y,
        fmt="-",
        color="black",
        label=title,
        linewidth=0.7
    )
    ax.fill_between(
        x, 
        y, 
        mean(y), 
        where=(y > mean(y)), 
        color="green", 
        alpha=0.7, 
        label="above average"
    )
    ax.fill_between(
        x, 
        y, 
        mean(y), 
        where=(y < mean(y)), 
        color="red", 
        alpha=0.7, 
        label="below average"
    )
    for label in ax.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax.tick_params(axis="x", colors="red")
    ax.tick_params(axis="y", colors="purple")
    ax.axhline(mean(y), color="cyan", linewidth=2)
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
