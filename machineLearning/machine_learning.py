from scipy import sparse
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
from scipy.stats import pearsonr
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import jieba
import pandas as pd


def datasets_demo():
    """
    sklearn数据集使用
    数据集地址：Y:\python\Lib\site-packages
    :return:
    """
    iris = load_iris()
    print("鸢尾花数据集：\n", iris)
    print('查看数据集描述:\n', iris['DESCR'])
    print('查看特征值的名字\n', iris.feature_names)
    print('查看特征值\n', iris.data, iris.data.shape)

    # 数据集划分  random_state  随机数种子，如果设置了，每次分割的结果  x_train,x_test的数据都是一样的，如果不设置，每次的结果都是不一样的
    # 将iris.data中的数据按划分规则分给x_train,x_test，将iris.target中的数据按规则划分给y_train，y_test
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
    print('训练集的特征值:\n', x_train, x_train.shape)


def dict_demo():
    """
    字典特征抽取
    :return:
    """
    data = [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 80}, {'city': '深圳', 'temperature': 60}]
    transfer = DictVectorizer(sparse=False)  # 是否转换为稀疏矩阵
    data_new = transfer.fit_transform(data)
    print('data_new\n', data_new)
    print('特征名称\n', transfer.get_feature_names())


def count_demo():
    """
    文本特征抽取：CountVecotrizer
    :return:
    """
    data = ['life is short, i like like python', 'life is too long, i dislike python']
    # 1、实例化一个转换器
    transfer = CountVectorizer(stop_words=['too'])  # stop_words 停用词，不统计

    # 2、调用
    data_new = transfer.fit_transform(data)
    print('data_new:\n', data_new.toarray())
    print('特征名称:\n', transfer.get_feature_names())  # 统计每个特征词出现的个数


def count_chinese_demo():
    """
    文本特征抽取：CountVecotrizer
    :return:
    """
    data = ['我 爱 北京 天安门', '天安门 上 太阳 升']
    # 1、实例化一个转换器
    transfer = CountVectorizer()

    # 2、调用
    data_new = transfer.fit_transform(data)
    print('data_new:\n', data_new.toarray())
    print('特征名称:\n', transfer.get_feature_names())  # 统计每个特征词出现的个数


def cut_word(text):
    """
    进行中文分词：“我爱北京天安门”->我 爱 北京 天安门
    :param text:
    :return:
    """
    data = ' '.join(list(jieba.cut(text)))
    # print(data)
    return data


def count_chinese_demo2():
    """
    中文文本特征抽取：自动分词
    :return:
    """
    data = ['一种还是一种今天很残酷，明天更残酷，后天更美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。',
            '我们看到的从很远信息来的光是在几百万年之前发出的，这样当我们看到宇宙是，我们是在看它的过去',
            '如果只用一种方式了解某样事务，你就不会真正了解他。了解事务真正含义的秘密取决于如何将其与我们所了解的事务相关联']
    data_new = []
    # 将中文文本进行分词
    for tmp in data:
        data_new.append(cut_word(tmp))
    # print(data_new)

    # 1、实例化一个转换器
    transfer = CountVectorizer()

    # 2、调用
    data_new = transfer.fit_transform(data_new)
    print('data_new:\n', data_new.toarray())
    print('特征名称:\n', transfer.get_feature_names())  # 统计每个特征词出现的个数


def tfidf_demo():
    """
    用TF-IDF的方法进行文本特征抽取
    TF-IDF表示词的重要性
    TfidfVectorizer会根据指定的公式将文档中的词转换为概率表示
    :return:
    """
    """
    TF-IDF是一种统计方法，用以评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度。
    字词的重要性随着它在文件中出现的次数成正比增加，但同时会随着它在语料库中出现的频率成反比下降。 
    假如一篇文件的总词语数是100个，而词语“母牛”出现了3次，那么“母牛”一词在该文件中的词频就是3/100=0.03。
    一个计算文件频率 (IDF) 的方法是文件集里包含的文件总数除以测定有多少份文件出现过“母牛”一词。
    所以，如果“母牛”一词在1,000份文件出现过，而文件总数是10,000,000份的话，其逆向文件频率就是 lg(10,000,000 / 1,000)=4。
    最后的TF-IDF的分数为0.03 * 4=0.12。   
    """
    data = ['一种还是一种今天很残酷，明天更残酷，后天更美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。',
            '我们看到的从很远信息来的光是在几百万年之前发出的，这样当我们看到宇宙是，我们是在看它的过去',
            '如果只用一种方式了解某样事务，你就不会真正了解他。了解事务真正含义的秘密取决于如何将其与我们所了解的事务相关联']
    data_new = []
    # 将中文文本进行分词
    for tmp in data:
        data_new.append(cut_word(tmp))
    # print(data_new)

    # 1、实例化一个转换器
    transfer = TfidfVectorizer(stop_words=['一种', '所以'])

    # 2、调用
    data_new = transfer.fit_transform(data_new)
    print('data_new:\n', data_new.toarray())
    print('特征名称:\n', transfer.get_feature_names())  # 统计每个特征词出现的个数


def minmax_demo():
    """
    归一化
    MinMaxScaler：将数据矩阵缩放到[0,1]之间（将每一列数据做归一化处理）
    :return:
    """
    # 1、获取数据
    data = pd.read_csv("dating.txt")  # 详见day1视频12
    data = data.iloc[:, :3]
    # 2、实例化一个转换器  feature_range=[2,3]：表示特征值在2到3之间
    transfer = MinMaxScaler(feature_range=[2, 3])
    # 3、调用fit_transform
    data_new = transfer.fit_transform(data)
    print(data_new)


def stand_demo():
    """
    标准化
    经过处理后的数据均值为0，标准差为1
    :return:
    """
    # 1、获取数据
    data = pd.read_csv("dating.txt")  # 详见day1视频13
    data = data.iloc[:, :3]
    # 2、实例化一个转换器
    transfer = StandardScaler()
    # 3、调用fit_transform
    data_new = transfer.fit_transform(data)
    print(data_new)


def variance_demo():
    """
    去掉取值变化小的特征（删除低方差特征）
    :return:
    """
    # 1、获取数据
    data = pd.read_csv('factor_returns.csv')
    data = data.iloc[:, 1:-2]
    print('data\n', data)

    # 2、实例化一个转换器类
    transfer = VarianceThreshold(threshold=100)  # 过滤掉方差小于100的

    # 3、调用fit_transform
    data_new = transfer.fit_transform(data)
    print('data_new:\n', data_new, data_new.shape)

    # 计算某两个变量之间的相关系数
    r1 = pearsonr(data['pe_ratio'],data['pb_ratio'])
    print('相关系数:\n',r1)

    r2 = pearsonr(data['revenue'], data['total_expense'])
    print('相关系数:\n', r2)

def pac_demo():
    """
    pca降维
    :return:
    """
    data = [[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]]
    # 1、实例化一个转换器
    # transfer = PCA(n_components=2) #从4维降低到2维
    transfer = PCA(n_components=0.95)  #保留95%的信息

    # 2、调用fit_transform
    data_new = transfer.fit_transform(data)
    print('data_new:\n',data_new)

    estimator = KMeans(n_clusters=3)  #聚类操作
    estimator.fit(data_new)

    print('----------------------------------------')
    y_predict = estimator.predict(data_new)
    print(y_predict)

    # silhouette_score(data_new,y_predict)

if __name__ == "__main__":
    # datasets_demo()
    # dict_demo()
    # count_demo()
    # count_chinese_demo()
    # cut_word('我爱北京天安门')
    # count_chinese_demo2()
    # tfidf_demo()
    # minmax_demo()
    # stand_demo()
    # variance_demo()
    pac_demo()