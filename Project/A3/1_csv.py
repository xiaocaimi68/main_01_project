# =========================
# Step 1：只做一件事 —— 生成「真实业务风格」数据，并保存为 CSV
# 不做任何算法、不做修正
# =========================

import pandas as pd

# -------------------------
# 1. 定义时间索引（周粒度）
# -------------------------
dates = pd.date_range("2024-06-01", periods=4, freq="W")

# -------------------------
# 2. 历史出库量数据（老品 & 场景来源）
# -------------------------
history_sales = pd.DataFrame({
    "date": dates,
    "BBQ_Meat": [120, 150, 180, 220],   # 烧烤肉串（烧烤主材）
    "BBQ_Tool": [80, 90, 110, 130],     # 烧烤工具
    "Beer_Old": [200, 210, 230, 240],   # 老款啤酒
    "Cola_1L": [300, 280, 260, 240],    # 大瓶可乐
})

history_sales.to_csv("history_sales.csv", index=False)

# -------------------------
# 3. 新品基础预测（来自三阶段算法的输出）
# -------------------------
base_prediction = pd.DataFrame({
    "date": dates,
    "Beer_New": [100, 100, 100, 100],     # 新品啤酒
    "Cola_500ml": [200, 200, 200, 200],   # 小瓶可乐
})

base_prediction.to_csv("base_prediction.csv", index=False)

# -------------------------
# 4. 标签 & 方向配置表（纯配置，无算法）
# -------------------------
label_config = pd.DataFrame({
    "entity": ["BBQ_Kit", "Beer", "Cola_1L", "Cola_500ml"],
    "tag": ["BBQ_Lead_Beer", "BBQ_Lead_Beer", "Cola_Substitute", "Cola_Substitute"],
    "role": ["lead", "follow", "both", "both"],
    "weight": [0.3, 1.0, -0.2, -0.2]
})

label_config.to_csv("label_config.csv", index=False)

print("✅ Step 1 完成：数据已生成并保存为 CSV 文件")
print("\n生成的文件包括：")
print(" - history_sales.csv")#历史真实销量（老品 & 场景来源）
print(" - base_prediction.csv")#新品基础预测（
print(" - label_config.csv")#标签 + 方向 + 权重（纯配置表）

print("\n📄 history_sales.csv 示例：")
print(history_sales)

print("\n📄 base_prediction.csv 示例：")
print(base_prediction)

print("\n📄 label_config.csv 示例：")
print(label_config)
