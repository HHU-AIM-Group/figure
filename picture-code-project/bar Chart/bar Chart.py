import matplotlib.pyplot as plt
import numpy as np

# 数据
local_attribute_cub = [53.52, 43.98, 43.42, 35.42, 61.78]
aggregate_attribute_cub = [66.62, 84.82, 93.46, 97.56, 100]

local_attribute_cifar = [79.34, 62.16, 60.86, 82.94, 83.52]
aggregate_attribute_cifar = [82.66, 95.12, 98.78, 99.84, 100]

# 定义条形图的位置
bar_width = 0.35
index = np.arange(len(local_attribute_cub))

# 创建图表
fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(9, 4))

# 绘制CUB数据集的条形图
ax1.bar(index - bar_width / 2, local_attribute_cub, bar_width, label='CUB', color='#87CEFA')
ax1.bar(index + bar_width / 2, local_attribute_cifar, bar_width, label='CIFAR', color='#FFA500')
ax1.set_title('Attribute Acc', fontsize=14)
ax1.set_xticks(index)
type_labels = ["Attr 1", "Attr 2", "Attr 3", "Attr 4", "Global"]
ax1.set_xticklabels(type_labels, fontsize=14)
ax1.set_ylabel('Accuracy (%)', fontsize=16)  # 设置y轴标签的字体大小
ax1.legend(loc="lower right")

# 设置y轴刻度标签的字体大小
ax1.yaxis.set_tick_params(labelsize=14)

# 绘制CIFAR数据集的折线图
ax2.plot(index + bar_width / 2, aggregate_attribute_cub, marker='o', label='CUB', color='#87CEFA')
ax2.plot(index + bar_width / 2, aggregate_attribute_cifar, marker='o', label='CIFAR', color='#FFA500')
ax2.set_title('Aggregate Attribute Top-k Acc', fontsize=14)
ax2.set_xticks(index + bar_width / 2)
ax2.set_xticklabels([f'Top {i + 1}' for i in range(len(local_attribute_cifar))], fontsize=14)
ax2.set_ylabel('Accuracy (%)', fontsize=16)  # 设置y轴标签的字体大小
ax2.legend(loc="lower right")

# 设置y轴刻度标签的字体大小
ax2.yaxis.set_tick_params(labelsize=14)

# 显示网格
for ax in [ax1,ax2]:
    ax.grid(axis='y', linestyle='--', alpha=0.7)

# 调整布局
plt.tight_layout()
# 显示图表
plt.show()

# plt.savefig('semantic_similarity_1.pdf', bbox_inches='tight')


