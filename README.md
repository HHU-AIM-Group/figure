# 画图的代码   
```python
import matplotlib.pyplot as plt
from matplotlib import patheffects
import numpy as np
# 读取两个TXT文件中的数据
with open('output/State-Air/map_对抗.txt', 'r') as file:
    data1 = [float(line.strip()) for line in file.readlines()]

with open('output/State-Air/map_无对抗.txt', 'r') as file:
    data2 = [float(line.strip()) for line in file.readlines()]
    
with open('output/State-Air/loss_对抗.txt', 'r') as file:
    data3 = [float(line.strip()) for line in file.readlines()]

with open('output/State-Air/loss_无对抗.txt', 'r') as file:
    data4 = [float(line.strip()) for line in file.readlines()]


with open('output/AU-AIR/map_对抗训练.txt', 'r') as file:
    data1 = [float(line.strip()) for line in file.readlines()]

with open('output/AU-AIR/map_无对抗训练.txt', 'r') as file:
    data2 = [float(line.strip()) for line in file.readlines()]

with open('output/AU-AIR/loss_对抗训练.txt', 'r') as file:
    data3 = [float(line.strip()) for line in file.readlines()]

with open('output/AU-AIR/loss_无对抗训练.txt', 'r') as file:
    data4 = [float(line.strip()) for line in file.readlines()]

# Generate x-axis data
x1 = [i*10 for i in range(len(data1))]
x2 = [i for i in range(len(data3))]

# Create subplots
fig, ax1 = plt.subplots(figsize=(8, 6), frameon=False)
plt.gca().set_facecolor('#F2F2F2')  # Set background color

# Plot mAP curves with narrower shaded regions
std_multiplier = 0.12  # Adjust this value to control the width of the shaded region

line1, = ax1.plot(x1, data1, label='mAP w/ Adversarial', color='#FF9500', linestyle='-', marker='o', markersize=5, markevery=1, linewidth=2, clip_on=False)
line2, = ax1.plot(x1, data2, label='mAP w/o Adversarial', color='#D5558B', linestyle='--', marker='^', markersize=5, markevery=1, linewidth=2, clip_on=False)
ax1.fill_between(x1, np.array(data1) - std_multiplier * np.std(data1), np.array(data1) + std_multiplier * np.std(data1), color='#FF9500', alpha=0.2)
ax1.fill_between(x1, np.array(data2) - std_multiplier * np.std(data2), np.array(data2) + std_multiplier * np.std(data2), color='#D5558B', alpha=0.2)
ax1.set_ylabel('mAP', color='black', fontsize=14)
ax1.set_ylim(0, max(data1 + data2) * 1.1)
# Create the second y-axis for loss
ax2 = ax1.twinx()
line3, = ax2.plot(x2, data3, label='loss w/ Adversarial', color='#00B8DA', linestyle='-', linewidth=2, clip_on=False)
line4, = ax2.plot(x2, data4, label='loss w/o Adversarial', color='#8D5242', linestyle='--', linewidth=2, clip_on=False)
ax2.fill_between(x2, np.array(data3) - std_multiplier * np.std(data3), np.array(data3) + std_multiplier * np.std(data3), color='#00B8DA', alpha=0.2)
ax2.fill_between(x2, np.array(data4) - std_multiplier * np.std(data4), np.array(data4) + std_multiplier * np.std(data4), color='#8D5242', alpha=0.2)
ax2.set_ylabel('Loss', color='black', fontsize=14)
# Add title and labels
fig.text(0.5, 0.04, 'Epochs', ha='center', fontsize=14)
# plt.title('Impact of Adversarial Learning')

# Create a combined legend
lines = [line1, line2, line3, line4]
labels = [line.get_label() for line in lines]
plt.legend(lines, labels, fontsize=16, loc='right')

# Remove borders
for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

plt.grid(True, linestyle='solid', color='white', alpha=1, axis="both")
plt.xlim(0, 200)
# plt.ylim(0, 0.35)
# Display the plot
plt.show()

"""# 生成x轴数据
x1 = [i*10 for i in range(len(data1))]
x2 = [i for i in range(len(data3))]

# 绘制曲线图
fig, ax1 = plt.subplots(figsize=(8, 6), frameon=False)
plt.gca().set_facecolor('#F2F2F2')  # 设置背景色为灰色

line1, = ax1.plot(x1, data1, label='mAP w/ Adversarial', color='#FF9500', linestyle='-', marker='o', markersize=5, markevery=1, linewidth=2)
line2, = ax1.plot(x1, data2, label='mAP w/o Adversarial', color='#D5558B', linestyle='--', marker='^', markersize=5, markevery=1, linewidth=2)
ax1.set_ylabel('mAP', color='black')

# 创建第二个y轴
ax2 = ax1.twinx()
line3, = ax2.plot(x2, data3, label='loss w/ Adversarial', color='#00B8DA', linestyle='-', linewidth=2)
line4, = ax2.plot(x2, data4, label='loss w/o Adversarial', color='#8D5242', linestyle='--', linewidth=2)
ax2.set_ylabel('Loss', color='black')
plt.xlabel('Epochs')
plt.title('Impact of Adversarial Learning')
plt.legend([line1, line2, line3, line4], ['mAP w/ Adversarial', 'mAP w/o Adversarial',
                                          'loss w/ Adversarial','loss w/o Adversarial'], fontsize=20, loc='right')

# Add shadows to the lines
for line in [line1, line2, line3, line4]:
    line.set_path_effects([patheffects.withStroke(linewidth=4, foreground='black')])

plt.grid(True, linestyle='-', color='gray', alpha=0.7, axis="both")

plt.show()"""

"""# 生成x轴数据
x1 = [i*10 for i in range(len(data1))]
x2 = [i for i in range(len(data3))]

# 绘制曲线图
fig, ax1 = plt.subplots(figsize=(8, 6))
line1, = ax1.plot(x1, data1, label='mAP w/ Adversarial', color='#FF9500', linestyle='-', marker='o', markersize=5, markevery=1, linewidth=2)
line2, = ax1.plot(x1, data2, label='mAP w/o Adversarial', color='#D5558B', linestyle='--', marker='^', markersize=5, markevery=1, linewidth=2)
ax1.set_ylabel('mAP', color='black')

# 创建第二个y轴
ax2 = ax1.twinx()
line3, = ax2.plot(x2, data3, label='loss w/ Adversarial', color='#00B8DA', linestyle='-', linewidth=2)
line4, = ax2.plot(x2, data4, label='loss w/o Adversarial', color='#8D5242', linestyle='--', linewidth=2)
ax2.set_ylabel('Loss', color='black')
plt.xlabel('Epochs')
plt.title('Impact of Adversarial Learning')
plt.legend([line1, line2, line3, line4], ['mAP w/ Adversarial', 'mAP w/o Adversarial',
                                          'loss w/ Adversarial','loss w/o Adversarial'], fontsize=20, loc='right')


plt.grid(True, linestyle='-', color='gray', alpha=0.7, axis="both")

plt.show()
"""
"""# 绘制曲线图
plt.plot(x1, data1, label='mAP w/ Adversarial', color='blue')
plt.plot(x1, data2, label='mAP w/o Adversarial', color='red')
plt.plot(x2, data3, label='loss w/ Adversarial', color='green')
plt.plot(x2, data4, label='loss w/o No Adversarial', color='orange')

plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Impact of Adversarial Learning')
plt.legend(fontsize=14)
plt.grid(True)
plt.show()"""

"""# 绘制曲线图
fig, ax1 = plt.subplots()
line1, = ax1.plot(x1, data1, label='mAP w/ Adversarial', color='#FF9500')
line2, = ax1.plot(x1, data2, label='mAP w/o Adversarial', color='#D5558B')
ax1.set_ylabel('mAP', color='black')

# 创建第二个y轴
ax2 = ax1.twinx()
line3, = ax2.plot(x2, data3, label='loss w/ Adversarial', color='#00B8DA')
line4, = ax2.plot(x2, data4, label='loss w/o No Adversarial', color='#007560')
ax2.set_ylabel('Loss', color='black')
"""
# 设置整个图的背景色
# plt.figure(facecolor='lightgrey')
```
### 绘制出的图像效果示意图为以下两张图片,第一张为State-Air.svg，第二张为AU-Air.svg
![State-Air.svg](https://s2.loli.net/2024/12/11/NyQUmtWhrC9ReDO.png)
![AU-Air.svg](https://s2.loli.net/2024/12/11/NyQUmtWhrC9ReDO.png)
