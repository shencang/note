import tensorflow as tf
import sys

sess = tf.Session()
a = tf.constant(1)
b = tf.constant(2)
print(sess.run(a+b))