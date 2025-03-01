import matplotlib.pyplot as plt
import numpy as np

labels = ['A', 'B', 'C', 'D', 'E']
values = [4, 3, 2, 5, 1]

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(angles, values, color='blue')
ax.fill(angles, values, color='blue', alpha=0.25)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
plt.title('Radar Chart Example')
plt.show()