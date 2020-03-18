# coding: utf-8
import os
import tensorflow as tf


def picture_read(filelist):
    """
    狗图片的处理
    :return:
    """
    # 1、构造文件名队列
    file_queue = tf.train.string_input_producer(filelist)
    # 2、读取与解码
    reader = tf.WholeFileReader()
    # key文件名  value 一张图片的原始编码形式
    key, value = reader.read(file_queue)
    print('key:\n', key)
    print('value:\n', value)
    # 解码阶段
    image = tf.image.decode_jpeg(value)
    print('image:\n', image)

    # 图像的形状、类型修改
    image_resized = tf.image.resize_images(image, [200, 200])
    print('image_resized_before:\n', image_resized)

    # 静态形状修改
    image_resized.set_shape([200, 200, 3])
    print('image_after:\n',image_resized)

    # 3、批处理
    image_batch = tf.train.batch([image_resized], batch_size=100, num_threads=1, capacity=100)
    print('image_batch:\n', image_batch)

    # 开启会话
    with tf.Session() as sess:
        # 开启线程
        # 线程协调员
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)

        key_new, value_new, image_new, image_resized_new,image_batch_new = sess.run([key, value, image, image_resized, image_batch])
        print('key_new：\n', key_new)
        print('value_new：\n', value_new)
        print('image_new：\n', image_new)
        print('image_resized_new：\n', image_resized_new)
        print('image_batch_new：\n', image_batch_new)

        # 回收线程
        coord.request_stop()
        coord.join(threads)


if __name__ == '__main__':
    filename = os.listdir('./dog')
    filelist = [os.path.join('./dog/', file) for file in filename]
    picture_read(filelist)
