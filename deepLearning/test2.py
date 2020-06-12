# coding: utf-8
import tensorflow as tf

with tf.variable_scope("conv1"):
    matrix1 = [[2.0, 2.0, 3.0], [1.0, 2.0, 3.0], [2.0, 5.0, 3.0]]
    sotfmax_x = tf.nn.softmax(matrix1,axis=1)

with tf.Session() as sess:
    result = sess.run(sotfmax_x)
    print(result)
