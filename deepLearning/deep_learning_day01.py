# coding: utf-8
import tensorflow as tf
import os


def tensorflow_demo():
    """
    TensorFLow的基本结构
    :return:
    """
    # 原生python加法运算
    a = 2
    b = 3
    c = a + b
    print('普通加法运算结构：\n', c)

    # TensorFlow实现加法运算
    a_t = tf.constant(2)
    b_t = tf.constant(3)
    c_t = a_t + b_t
    print('TensorFlow加法运算的结果：\n', c_t)

    # 开启回话
    with tf.Session() as sess:
        sum_t = sess.run(c_t)
        print('在sess当中的sum_t:\n', sum_t)


def graph_demo():
    """
    图的演示
    :return:
    """
    # TensorFlow实现加法运算
    a_t = tf.constant(2, name='a_t')  # 指定名称
    b_t = tf.constant(3, name='b_t')
    c_t = a_t + b_t
    print('a_t：\n', a_t)
    print('b_t：\n', b_t)
    print('c_t：\n', c_t)

    # 查看默认图
    # 方法1：调用方法
    default_g = tf.get_default_graph()
    print('default_g:\n', default_g)

    # 方法2：查看属性
    print('a_t的图属性：\n', a_t.graph)
    print('c_t的图属性：\n', c_t.graph)

    # 自定义图
    new_g = tf.Graph()
    # 在自己的图中定义数据和操作
    with new_g.as_default():
        a_new = tf.constant(20)
        b_new = tf.constant(30)
        c_new = a_new + b_new
        print('a_new：\n', a_t)
        print('b_new：\n', b_t)
        print('c_new：\n', c_t)
        print('a_new：\n', a_new.graph)
        print('b_new：\n', b_new.graph)
        print('c_new：\n', c_new.graph)

    # 开启回话
    with tf.Session() as sess:
        # c_t_value = sess.run(c_t)
        # 试图运行自定义图中的数据、操作
        # print('c_t_value:\n', c_t_value)
        print('c_t_value:\n', c_t.eval())
        print('sess的图属性:\n', sess.graph)
        # 1)将图写入本地生成events文件
        tf.summary.FileWriter('./tmp/summary', graph=sess.graph)  # cd tmp/summary  执行tensorboard --logdir=./

    with tf.Session(graph=new_g) as new_sess:
        c_new_value = new_sess.run((c_new))
        print("c_new_value:\n", c_new_value)
        print("new_sess的图属性：\n", new_sess.graph)


def session_demo():
    """
    会话演示
    :return:
    """
    a_t = tf.constant(2)
    b_t = tf.constant(3)
    c_t = a_t + b_t

    a_ph = tf.placeholder(tf.float16)
    b_ph = tf.placeholder(tf.float16)
    c_ph = tf.add(a_ph, b_ph)
    print('a_ph:\n', a_ph)
    print('b_ph:\n', b_ph)
    print('c_ph:\n', c_ph)

    # 开启回话
    with tf.Session(config=tf.ConfigProto(allow_soft_placement=True,
                                          log_device_placement=True)) as sess:
        # 运行placeholder
        c_ph_value = sess.run(c_ph, feed_dict={a_ph: 1.2, b_ph: 1.5})
        print('c_ph_value:\n', c_ph_value)
        a, b, c = sess.run([a_t, b_t, c_t])
        print('a b c:\n', a, b, c)
        print('c_t_value:\n', c_t.eval())
        print('sess的图属性:\n', sess.graph)


def tensor_demo():
    tf.InteractiveSession()
    """
    张量的演示
    :return:
    """
    tensor1 = tf.constant(1)
    tensor2 = tf.constant([1, 2, 3, 4])
    tensor3 = tf.constant([[1], [2], [3], [4]], dtype=tf.int32)

    print('tensor1:\n', tensor1)
    print('tensor2:\n', tensor2)  # 一维数组 4列
    print('tensor3_before:\n', tensor3)  # 二维数组 4*1

    zeros = tf.zeros(shape=[2, 3]).eval()  # 创建一个两行三列的零数组默认float32
    print(zeros)
    zeros = tf.zeros(shape=[2, 3, 4]).eval()  # 创建一个2*3*4的零数组默认float32
    print(zeros)

    randomnum = tf.random_normal(shape=[2, 2], mean=10, stddev=1).eval()  # 创建一个2*2数组，平均值10，方差1
    print(randomnum)

    # 张量类型的修改
    tensor3_cast = tf.cast(tensor3, dtype=tf.float32)
    print('tensor3_after:\n', tensor3)
    print('tensor3_cast:\n', tensor3_cast)

    a_ph = tf.placeholder(tf.float16, shape=[None, None])  # 占位符，是二维数组，但是不确定具体行和列
    b_ph = tf.placeholder(tf.float16, shape=[None, 10])  # 二维数组，不确定行，确定了列
    c_ph = tf.placeholder(tf.float16, shape=[3, 2])
    print('a_ph:\n', a_ph)  # shape中是?
    print('b_ph:\n', b_ph)
    print('c_ph:\n', c_ph)
    # 更新形状未确定的部分
    # a_ph.set_shape([2,2])
    # b_ph.set_shape([2,10])
    a_ph_reshape = tf.reshape(a_ph, shape=[1, 2, 3])
    print('a_ph_reshape:\n', a_ph_reshape)


def variable_demo():
    """
    变量的演示
    :return:
    """
    # 创建变量
    with tf.variable_scope('my_scope'):
        a = tf.Variable(initial_value=50)
        b = tf.Variable(initial_value=40)
    with tf.variable_scope('your_scope'):
        c = tf.add(a, b)
    print('a:\n', a)
    print('b:\n', b)
    print('c:\n', c)

    # 初始化变量
    init = tf.global_variables_initializer()

    # 开启回话
    with tf.Session() as sess:
        sess.run(init)
        a_value, b_value, c_value = sess.run([a, b, c])
        print('a_value:\n', a_value)
        print('b_value:\n', b_value)
        print('c_value:\n', c_value)


def linear_regression():
    """
    自实现一个线性回归
    :return:
    """
    with tf.variable_scope('prepare_data'):
        # 1) 准备数据
        X = tf.random_normal(shape=[100, 1])
        y_true = tf.matmul(X, [[0.8]]) + 0.7

    with tf.variable_scope('create_model'):
        # 2) 构造模型
        # 定义模型参数 用变量
        weights = tf.Variable(initial_value=tf.random_normal(shape=[1, 1]))
        bias = tf.Variable(initial_value=tf.random_normal(shape=[1, 1]))
        y_predict = tf.matmul(X, weights) + bias

    with tf.variable_scope('loss_function'):
        # 3) 构造损失函数
        error = tf.reduce_mean(tf.square(y_predict - y_true))

    with tf.variable_scope('optimizer'):
        # 4) 优化损失
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(error)

    # 2_收集变量
    tf.summary.scalar('error', error)
    tf.summary.histogram('weights', weights)
    tf.summary.histogram('bias', bias)

    # 3_合并变量
    merged = tf.summary.merge_all()

    saver = tf.train.Saver()

    # 显示地初始化变量
    init = tf.global_variables_initializer()

    # 开启会话
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init)

        # 1_创建事件文件]
        file_writer = tf.summary.FileWriter('./tmp/linear', graph=sess.graph)

        # 查看初始化模型参数之后的值
        print('训练前模型参数为：权重%f，偏置%f，损失为%f' % (weights.eval(), bias.eval(), error.eval()))

        # 开始训练
        for i in range(100):
            sess.run(optimizer)
            print("训练前模型参数为：权重%f，偏置%f，损失为%f" % (weights.eval(), bias.eval(), error.eval()))
            # 运行合并变量操作
            summary = sess.run(merged)
            # 将每次迭代后的变量写入事件文件
            file_writer.add_summary(summary, i)

            # 保存模型
            if i % 10 == 0:
                saver.save(sess, './tmp/model/my_linear.ckpt')

        if os.path.exists('./tmp/model/checkpoint'):
            saver.restore(sess,'./tmp/model/my_linear.ckpt')
        print("训练后模型参数为：权重%f，偏置%f，损失为%f" % (weights.eval(), bias.eval(), error.eval()))

# 1）定义命令行参数
tf.app.flags.DEFINE_integer("max_step", 100, "训练模型的步数")
tf.app.flags.DEFINE_string("model_dir", "Unknown", "模型保存的路径+模型名字")

# 2）简化变量名
FLAGS = tf.app.flags.FLAGS

def command_demo():
    """
    命令行参数演示
    :return:
    """
    print("max_step:\n", FLAGS.max_step)
    print("model_dir:\n", FLAGS.model_dir)

    """
    如何使用：  命令行 : python deep_learning_day01.py --max_step=10
    """

    return None

def main(argv):
    print(argv)
    print("code start")
    return None


if __name__ == '__main__':
    # tensorflow_demo()
    # graph_demo()
    # session_demo()
    # tensor_demo()
    # variable_demo()
    # linear_regression()
    # command_demo()
    tf.app.run()