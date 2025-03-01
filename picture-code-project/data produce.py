import numpy as np
"""
# 生成 200 个 0 到 π 之间的均匀分布随机数
uniform_random_numbers = np.random.uniform(0, np.pi, 2000)

# 将均匀分布的随机数通过正弦函数映射到 0 到 1 之间
sine_distributed_numbers = np.sin(uniform_random_numbers)

# 将每个数写入文件，每个数占一行
with open('sine_random_numbers.txt', 'w') as file:
    for number in sine_distributed_numbers:
        file.write(f"{number:.6f}\n")

print("随机数已生成并保存到 sine_random_numbers.txt 文件中。")
"""


# 生成 200 个从 1.0 线性递减到 0.0 的浮点数
n = 200
linear_decrease = [1.0 - i / (n - 1) for i in range(n)]

# 将结果保存到文件
with open("output.txt", "w") as file:
    for value in linear_decrease:
        file.write(f"{value}\n")