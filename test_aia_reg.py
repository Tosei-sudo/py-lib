# coding: utf-8
from aia.network import RegressionNetwork
from aia.optimizer import Adam
from aia.functions import fit_transform, mean_squared_error

import numpy as np

# 擬似データの生成
# X = np.random.rand(1000, 10)  # 1000サンプル、10特徴量
X = np.random.rand(1000, 10)
y_anser = X.sum(axis=1) + np.random.normal(0, 0.1, 1000)  # 出力は特徴量の合計にノイズを加えたもの
X_scaled = fit_transform(X)

network = RegressionNetwork(input_size=10, output_size=1, hidden_sizes=[64, 32])
network.load_params("regression.pkl")

import matplotlib.pyplot as plt

y = network.predict(X_scaled)
y = y.reshape(-1)
y *= 10

plt.scatter(y, y_anser)
plt.show()