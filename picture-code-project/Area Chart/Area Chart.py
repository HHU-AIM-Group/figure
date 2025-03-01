import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [15, 25, 35, 45, 55]

plt.stackplot(x, y1, y2, labels=['A', 'B'], colors=['orange', 'green'])
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Area Chart Example')
plt.legend()
plt.show()