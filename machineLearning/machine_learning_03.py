# -*- coding: utf-8 -*-
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.externals import joblib
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)


def linear1():
    """
    正规方程的优化方法对波士顿放假进行预测
    :return:
    """
    # 1、获取数据
    boston = load_boston()
    # 2、划分数据集
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state=22)

    # 3、标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4、预估器
    estimator = LinearRegression()
    estimator.fit(x_train, y_train)
    # 5、得出模型
    print('正规方程权重系数：\n', estimator.coef_)
    print('正规方程偏置为：\n', estimator.intercept_)
    # 6、模型评估
    y_predict = estimator.predict(x_test)
    print('预测房价：\n', y_predict)
    error = mean_squared_error(y_test, y_predict)
    print('正规方程-均方误差：\n', error)


def linear2():
    """
    梯度下降的优化方法对波士顿放假进行预测
    :return:
    """
    # 1、获取数据
    boston = load_boston()
    # 2、划分数据集
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state=22)

    # 3、标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4、预估器
    estimator = SGDRegressor(learning_rate='constant', eta0=0.01, max_iter=10000)
    estimator.fit(x_train, y_train)
    # 5、得出模型
    print('梯度下降权重系数：\n', estimator.coef_)
    print('梯度下降偏置为：\n', estimator.intercept_)
    # 6、模型评估
    y_predict = estimator.predict(x_test)
    print('预测房价：\n', y_predict)
    error = mean_squared_error(y_test, y_predict)
    print('正规方程-均方误差：\n', error)


def linear3():
    """
    岭回归对波士顿放假进行预测
    :return:
    """
    # 1、获取数据
    boston = load_boston()
    print('特征数量:\n', boston.data.shape)
    # 2、划分数据集
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state=22)

    # 3、标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4、预估器
    estimator = Ridge(max_iter=100)
    estimator.fit(x_train, y_train)

    # 保存模型
    # joblib.dump(estimator,'my_ridge.pkl')
    # 加载模型
    # estimator = joblib.load('my_ridge.pkl')
    # 5、得出模型
    print('岭回归权重系数：\n', estimator.coef_)
    print('岭回归偏置为：\n', estimator.intercept_)
    # 6、模型评估
    y_predict = estimator.predict(x_test)
    print('预测房价：\n', y_predict)
    error = mean_squared_error(y_test, y_predict)
    print('正规方程-均方误差：\n', error)


def cancer_demo():
    """
    逻辑回归对癌症的影响
    :return:
    """
    # 1、数据读取
    path = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
    column_name = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                   'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                   'Normal Nucleoli', 'Mitoses', 'Class']

    data = pd.read_csv(path, names=column_name)

    # 2、缺失值处理
    # 替换np.nan
    data = data.replace(to_replace='?', value=np.nan)
    # 删除缺失样本
    data.dropna(inplace=True)
    # 删除特征值和目标值
    x = data.iloc[:, 1:-1]
    y = data['Class']

    # 3、数据划分
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    # 4、标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 5、预估器流程
    estimator = LogisticRegression()
    estimator.fit(x_train, y_train)

    # 逻辑回归的模型参数：回归系数和偏置
    # estimator.coef_
    # estimator.intercept_

    # 5、模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('直接对比真实值和预测值：\n', y_test == y_predict)

    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率：\n', score)
    print('-------------------------------------------')
    report = classification_report(y_test, y_predict, labels=[2, 4], target_names=["良性", "恶性"])
    print(report)
    print('-------------------------------------------')
    # y_true：每个样本的真实类别，必须为0（反例），1（正例）标记
    # 将y_test 转换成0 1
    y_true = np.where(y_test > 3, 1, 0)
    print(roc_auc_score(y_true, y_predict))


if __name__ == '__main__':
    # 正规方程
    # linear1()
    # 梯度下降
    # linear2()
    linear3()
    # cancer_demo()
