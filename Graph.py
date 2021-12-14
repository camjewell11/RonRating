import numpy as np

import matplotlib.pyplot as plt

beers = ["Puddin\' Pop Stout", "Zwickle"]
beerCategories = ["Sweetness", "Bitterness", "Strength", "Body", "Head"]
sampleData = [ [7,2,8,4,5], [5,3,6,7,9] ]

numVars = len(beerCategories)
angles = np.linspace(0, 2 * np.pi, numVars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

def add_to_radar(beerNum, color):
    values = sampleData[beerNum]
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=1, label=beers[beerNum])
    ax.fill(angles, values, color=color, alpha=0.25)

add_to_radar(0, '#1aaf6c')
add_to_radar(1, '#429bf4')

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
ax.legend(loc='upper left', bbox_to_anchor=(1.2, 1.2))
ax.tick_params(colors='#222222')
# ax.grid(color='#AAAAAA')
ax.spines['polar'].set_color('#222222')

plt.tight_layout()
plt.show()

print ('hi')