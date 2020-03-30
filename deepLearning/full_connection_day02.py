# coding: utf-8
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


def full_connection():
    """
    用全连接来对手写数字进行识别
    :return:
    """
    # 1、准备数据
    mnist = input_data.read_data_sets('./mnist_data', one_hot=True)
    x = tf.placeholder(dtype=tf.float32, shape=(None, 784))  # 28*28 = 784 每个照片的像素为28*28
    y_true = tf.placeholder(dtype=tf.float32, shape=(None, 10))  # 共有十个类别  0、1、2 ... 9

    # 2、构建模型
    weights = tf.Variable(initial_value=tf.random_normal(shape=[784, 10]))
    bias = tf.Variable(initial_value=tf.random_normal(shape=[10]))
    y_predict = tf.matmul(x, weights) + bias
    # 3、构造损失函数
    error = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_predict))
    # 4、优化损失
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(error)

    # 5）增加准确率计算
    # 比较输出的结果最大值所在位置和真实值的最大值缩在位置
    # 求平均
    # argmax：表示f(x)取最大值时x的取值
    bool_list = tf.equal(tf.argmax(y_true, axis=1), tf.argmax(y_predict, axis=1))  # 比较预测值和实际值是否在同一个位置
    accuracy = tf.reduce_mean(tf.cast(bool_list, tf.float32))  # 求平均

    # 初始化变量
    init = tf.global_variables_initializer()

    # 开启会话
    with tf.Session() as sess:
        sess.run(init)
        image, label = mnist.train.next_batch(100)  # 返回的是下100个样本数据
        print('训练之前，权重为%f,偏置为%f' % sess.run(error, feed_dict={x: image, y_true: label}))

        # 开始训练
        for i in range(1000):
            _, loss, accuracy_new = sess.run([optimizer, error, accuracy], feed_dict={x: image, y_true: label})
            print('第%d次训练，损失为%f，准确率为%f' % (i + 1, loss, accuracy_new))


# playground.tensorflow.org


if __name__ == '__main__':
    full_connection()
