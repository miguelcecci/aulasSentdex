import tensorflow as tf
from tensorflow.examples.tutorials.mnist inport input_data

'''
input>weight>hidden layer 1 (activation funcation)>weights>hidden l 2
(activation function) > weights >outputlayer

compare output to intended output > cost function(cross entropy)
optimization function (optimizer) > minimize cost (adamoptimizer ... SGD, AdaGrad)

backpropagation

feed forward + backprop = epoch
'''


mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

#500 camadas em cada layer
n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_nl3 = 500


n_classes = 10

#numero de entradas por batch
batch_size = 100

#altura x largura
x = tf.placeholder('float',[None, 784])
def neural_network_model(data):
    #(input_data*weights)+biases
    hidden_1_layer = {'wights':tf.Variable(tf.random_normal([784, n_nodes_hl1])),
                      'biases':tf.Variable(tf.random_normal(n_nodes_hl1))

    hidden_2_layer = {'wights':tf.Variable(tf.random_normal([ n_nodes_hl1, n_nodes_hl2])),
                      'biases':tf.Variable(tf.random_normal(n_nodes_hl2))}

    hidden_3_layer = {'wights':tf.Variable(tf.random_normal([ n_nodes_hl2, n_nodes_hl3])),
                      'biases':tf.Variable(tf.random_normal(n_nodes_hl3))}

    output_layer = {'wights':tf.Variable(tf.random_normal([ n_nodes_hl3, n_classes])),
                      'biases':tf.Variable(tf.random_normal(n_classes))}

    l1 = tf.add(tf.matmultiply(data, hidden_1_layer['weights']) + hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmultiply(data, hidden_2_layer['weights']) + hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmultiply(data, hidden_3_layer['weights']) + hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)

    output = tf.add(tf.matmultiply(data, output_layer['weights']) + output_layer['biases'])
    return output
