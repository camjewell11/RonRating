import copy
import numpy as np
import matplotlib.pyplot as plt

beerCategories = ["Sweetness", "Bitterness", "Strength", "Body", "Head"]

numVars = len(beerCategories)
angles = np.linspace(0, 2 * np.pi, numVars, endpoint=False).tolist()
angles += angles[:1]

def createRadar():
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), beerCategories)

    for label, angle in zip(ax.get_xticklabels(), angles):
        if angle in (0, np.pi):
            label.set_horizontalalignment('center')
        elif 0 < angle < np.pi:
            label.set_horizontalalignment('left')
        else:
            label.set_horizontalalignment('right')

    ax.set_ylim(0, 10)
    ax.set_rlabel_position(180/numVars)

    ax.set_title('BeeZr Beers', y=1.08)
    ax.tick_params(colors='#222222')
    # ax.grid(color='#AAAAAA')
    ax.spines['polar'].set_color('#222222')

    return ax

def add_to_radar(ax, beers, beerName, color):
    values = copy.deepcopy(beers[beerName])
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=1, label=beerName)
    ax.fill(angles, values, color=color, alpha=0.25)

def plotRadar(ax, beers, graphs):
    for graph in graphs.keys():
        add_to_radar(ax, beers, graph, graphs[graph])
    # plt.legend(loc='upper left', bbox_to_anchor=(1.25, 1.1))
    plt.tight_layout()
    plt.show()

# ax = createRadar()
# plotRadar(ax, graphs)