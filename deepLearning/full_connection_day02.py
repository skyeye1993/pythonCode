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
    x = tf.placeholder(dtype=tf.float32, shape=(None, 784))
    y_true = tf.placeholder(dtype=tf.float32, shape=(None, 10))

    # 2、构建模型
    weights = tf.Variable(initial_value=tf.random_normal(shape=[784, 10]))
    bias = tf.Variable(initial_value=tf.random_normal(shape=[10]))
    y_predict = tf.matmul(x, weights) + bias
    # 3、构造损失函数
    error = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_predict))
    # 4、优化损失
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(error)

    # 5）增加准确率计算
    bool_list = tf.equal(tf.argmax(y_true, axis=1), tf.argmax(y_predict, axis=1))
    accuracy = tf.reduce_mean(tf.cast(bool_list, tf.float32))

    # 初始化变量
    init = tf.global_variables_initializer()

    # 开启会话
    with tf.Session() as sess:
        sess.run(init)
        image, label = mnist.train.next_batch(100)
        print('训练之前，权重为%f,偏置为%f' % sess.run(error, feed_dict={x: image, y_true: label}))

        # 开始训练
        for i in range(1000):
            _, loss, accuracy_new = sess.run([optimizer, error, accuracy], feed_dict={x: image, y_true: label})
            print('第%d次训练，损失为%f，准确率为%f' % (i + 1, loss, accuracy_new))


# playground.tensorflow.org


if __name__ == '__main__':
    full_connection()
