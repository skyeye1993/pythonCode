from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)


def knn_iris():
    """
    用KNN算法对鸢尾花进行分类
    :return:
    """
    # 1、获取数据
    iris = load_iris()
    # 2、划分数据
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=6)
    # 3、特征工程：标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)  # 此步骤已经把x_train中的平均值、标准差放入transfer
    x_test = transfer.transform(x_test)  # 此处用的是x_train的平均值、标准差，然后对x_test数据进行转换

    # 4、KNN算法预估器
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train, y_train)  # 将特征值和目标值进行训练，生成模型

    # 5、模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('直接对比真实值和预测值：\n', y_test == y_predict)

    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率：\n', score)


def knn_iris_gscv():
    """
    用KNN算法对鸢尾花进行分类，添加网格搜索和交叉验证
    :return:
    """
    # 1、获取数据
    iris = load_iris()
    # 2、划分数据
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=6)
    # 3、特征工程：标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4、KNN算法预估器
    estimator = KNeighborsClassifier()

    # 加入网格搜索和交叉验证
    # 参数准备
    """
    网格搜索：穷举搜索：在所有候选的参数选择中，通过循环遍历，尝试每一种可能性，表现最好的参数就是最终的结果。其原理就像是在数组里找最大值。
    如下n_neighbors，会依次去遍历1到11这几个数，得到最优的记过
    """
    param_dict = {'n_neighbors': [1, 3, 4, 5, 7, 9, 11]}
    # cv:交叉验证(cross validation，源码中有介绍)，把所有的数据分成10份，9份为训练集，1份为测试集，进行训练，重复循环10次，保证每一份都会被当做测试集，最后成功率取平均数
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=10)
    estimator.fit(x_train, y_train)

    # 5、模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('直接对比真实值和预测值：\n', y_test == y_predict)

    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率：\n', score)

    # 最佳参数：best_params_
    print("最佳参数：\n", estimator.best_params_)
    # 最佳结果：best_score_
    print("最佳结果：\n", estimator.best_score_)
    # 最佳估计器：best_estimator_
    print("最佳估计器:\n", estimator.best_estimator_)
    # 交叉验证结果：cv_results_
    print("交叉验证结果:\n", estimator.cv_results_)


def facebook():
    data = pd.read_csv('train.csv')
    data.head()
    # 1、缩小数据范围
    data = data.query('x<2.5 & x>2 & y<1.5 & y>1.0')
    # 2、处理时间特征
    time_value = pd.to_datetime(data['time'], unit='s')
    date = pd.DatetimeIndex(time_value)
    data['weekday'] = date.weekday
    data['day'] = date.day
    data['hour'] = date.hour
    # 3、过滤签到次数少的地点
    palce_count = data.groupby('place_id').count()['row_id']
    data_final = data[data['place_id'].isin(palce_count[palce_count > 3].index.values)]
    print(data_final)

    # 筛选特征值和目标值
    x = data_final[['x', 'y', 'accuracy', 'day', 'weekday', 'hour']]
    y = data_final['place_id']

    # 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(x, y)

    # 3、特征工程：标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4、KNN算法预估器
    estimator = KNeighborsClassifier(n_neighbors=3)

    # 加入网格搜索和交叉验证
    # 参数准备
    param_dict = {'n_neighbors': [7, 9, 11]}
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=3)
    estimator.fit(x_train, y_train)

    # 5、模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('直接对比真实值和预测值：\n', y_test == y_predict)

    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率：\n', score)

    # 最佳参数：best_params_
    print("最佳参数：\n", estimator.best_params_)
    # 最佳结果：best_score_
    print("最佳结果：\n", estimator.best_score_)
    # 最佳估计器：best_estimator_
    print("最佳估计器:\n", estimator.best_estimator_)
    # 交叉验证结果：cv_results_
    print("交叉验证结果:\n", estimator.cv_results_)


def nb_new():
    """
    朴素贝叶斯算法对新闻进行分类
    :return:
    """
    # 1、获取数据
    news = fetch_20newsgroups(subset='all')
    # 2、划分数据集
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target)
    # 3、特征工程：文本特征抽取-tfidf
    transfer = TfidfVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4、朴素贝叶斯算法预估器流程
    estimator = MultinomialNB()
    estimator.fit(x_train, y_train)
    # 5、模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('直接对比真实值和预测值：\n', y_test == y_predict)

    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率为：\n", score)


def decision_iris():
    """
    用决策树对鸢尾花进行分类
    :return:
    """
    # 1、获取数据集
    iris = load_iris()
    # 2、划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22)

    # 3、决策树评估器
    estimator = DecisionTreeClassifier(criterion='entropy') # entropy 信息增益的熵
    estimator.fit(x_train, y_train)

    # 4、模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('直接对比真实值和预测值：\n', y_test == y_predict)

    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率为：\n", score)

    # 可视化决策树
    export_graphviz(estimator, out_file='iris_tree.dot', feature_names=iris.feature_names)  # http://webgraphviz.com/


def titanic_demo():
    # 1、获取数据
    path = 'http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt'
    titanic = pd.read_csv(path)
    x = titanic[['pclass', 'age', 'sex']]
    y = titanic['survived']

    # 2、数据处理
    # 1）缺失值处理
    x['age'].fillna(x['age'].mean(), inplace=True)
    # 2）转换成字典
    x = x.to_dict(orient='records')
    # 3）数据集划分
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22)
    # 4）字典特征抽取
    transfer = DictVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 3、决策树评估器
    estimator = DecisionTreeClassifier(criterion='entropy', max_depth=8)
    estimator.fit(x_train, y_train)
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('直接对比真实值和预测值：\n', y_test == y_predict)

    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print("准确率为：\n", score)

    # 可视化决策树
    export_graphviz(estimator, out_file='titanic_tree.dot',
                    feature_names=transfer.get_feature_names())  # http://webgraphviz.com/


# 随机森林
def titanic_tree_demo():
    # 1、获取数据
    path = 'http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt'
    titanic = pd.read_csv(path)
    x = titanic[['pclass', 'age', 'sex']]
    y = titanic['survived']

    # 2、数据处理
    # 1）缺失值处理
    x['age'].fillna(x['age'].mean(), inplace=True)
    # 2）转换成字典
    x = x.to_dict(orient='records')
    # 3）数据集划分
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22)
    # 4）字典特征抽取
    transfer = DictVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 随机森林对泰坦尼克号乘客的生存预测
    estimator = RandomForestClassifier()

    # 加入网格搜索和交叉验证
    # 参数准备
    param_dict = {'n_estimators': [120, 200, 300, 500, 800, 1200],
                  'max_depth': [5, 8, 15]}
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=3)
    estimator.fit(x_train, y_train)

    # 5、模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('y_predict:\n', y_predict)
    print('直接对比真实值和预测值：\n', y_test == y_predict)

    # 方法2：计算准确率
    score = estimator.score(x_test, y_test)
    print('准确率：\n', score)

    # 最佳参数：best_params_
    print("最佳参数：\n", estimator.best_params_)
    # 最佳结果：best_score_
    print("最佳结果：\n", estimator.best_score_)
    # 最佳估计器：best_estimator_
    print("最佳估计器:\n", estimator.best_estimator_)
    # 交叉验证结果：cv_results_
    print("交叉验证结果:\n", estimator.cv_results_)


if __name__ == '__main__':
    # knn_iris()
    knn_iris_gscv()
    # facebook()
    # nb_new()
    # decision_iris()
    # titanic_demo()
    # titanic_tree_demo()