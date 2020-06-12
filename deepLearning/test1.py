# coding: utf-8
import tensorflow as tf

with tf.variable_scope("conv1"):
    matrix1 = [[-1, -2, -3], [4, 5, 6], [7, 8, 9]]
    relu1_x = tf.nn.relu(matrix1)

    matrix2 = [[-1.0, -2.0, -3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    relu2_x = tf.nn.tanh(matrix2)

    matrix3 = [[-1.0, -2.0, -3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    relu3_x = tf.nn.sigmoid(matrix3)

    matrix4 = [[-1.0, -2.0, -3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    # 激活层
    relu4_x = tf.nn.softmax(matrix4)

with tf.Session() as sess:
    result1, result2, result3, result4 = sess.run([relu1_x, relu2_x, relu3_x, relu4_x])
    print(result1, '\n\n', result2, '\n\n', result3, '\n\n', result4, '\n\n')
