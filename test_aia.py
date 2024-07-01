# coding: utf-8
from aia.network import RegressionNetwork
from aia.optimizer import Adam
from aia.functions import fit_transform, mean_squared_error

import numpy as np

# 擬似データの生成
# X = np.random.rand(1000, 10)  # 1000サンプル、10特徴量
X = np.random.rand(1000, 10)

y = X.sum(axis=1) + np.random.normal(0, 0.1, 1000)  # 出力は特徴量の合計にノイズを加えたもの

X_scaled = fit_transform(X)
y_reshaped = y.reshape(-1, 1)

network = RegressionNetwork(input_size=10, output_size=1, hidden_sizes=[64, 32])

optimizer = Adam(lr=0.01)

iters_num = 500000
train_size = X_scaled.shape[0]
batch_size = 100
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []
iter_per_epoch = max(train_size / batch_size, 1)

for i in range(iters_num):
    
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = X_scaled[batch_mask]
    t_batch = y_reshaped[batch_mask]

    grads = network.gradient(x_batch, t_batch)
    
    optimizer.update(network.params, grads)
    
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)
    
    if i % 50000 == 0:
        print(i, network.loss(X_scaled, y_reshaped))

network.save_params("regression.pkl")