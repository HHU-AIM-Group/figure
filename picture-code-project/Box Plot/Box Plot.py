import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, vert=True, patch_artist=True)
plt.xlabel('Groups')
plt.ylabel('Values')
plt.title('Box Plot Example')
plt.show()