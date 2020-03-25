# -*- coding: utf-8 -*-

from .modules import plt, mean, array
   
    
def plot_data(
        x: tuple = (), 
        y: tuple = (), 
        title: str = "", 
        filename: str = ""
):
    x = array(x)
    y = array(y)
    if "confirmed" in filename:
        label_variable = "Confirmed Cases"
    else:
        label_variable = "Deaths"
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    ax1.plot_date(
        x=x,
        y=y,
        fmt="-",
        color="black",
        label=label_variable,
        linewidth=0.7
    )
    ax1.fill_between(
        x, 
        y, 
        mean(y), 
        where=(y > mean(y)), 
        color="green", 
        alpha=0.7, 
        label="above average"
    )
    ax1.fill_between(
        x, 
        y, 
        mean(y), 
        where=(y < mean(y)), 
        color="red", 
        alpha=0.7, 
        label="below average"
    )
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.tick_params(axis="x", colors="red")
    ax1.tick_params(axis="y", colors="purple")
    ax1.axhline(mean(y), color="cyan", linewidth=2)
    plt.subplots_adjust(
        left=0.2,
        bottom=0.2,
        right=0.9,
        top=0.9,
        wspace=0.2,
        hspace=0
    )
    plt.grid(
        True,
        color="black",
        linestyle="-",
        linewidth=1
    )
    plt.xlabel("Timeline")
    plt.ylabel(label_variable)
    plt.title(title)
    plt.legend()
    plt.show()


