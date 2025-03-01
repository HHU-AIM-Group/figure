import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
sizes = [100, 200, 300, 400, 500]

plt.scatter(x, y, s=sizes, alpha=0.5)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Bubble Chart Example')
plt.show()