# -*- coding: utf-8 -*-
"""HW4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1veBBXelLH1Wa4w72foiP_mCBB72kA_A3
"""

import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import tensorflow as tf
import keras as ks
import numpy as np

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Admissions.csv')

features = data[['gre','gpa','rank']]
featuresScale = preprocessing.minmax_scale(data[['gre','gpa','rank']])

labels = data[['admit']]
labels = np.array(labels)

one_hot = np.zeros(shape=(len(labels),2))

for i in range (0,len(labels)):
    if labels[i] == 1:
        one_hot[i] = [1,0]
    else:
        one_hot[i] = [0,1]

RANDOM_SEED = 42
tf.random.set_seed(RANDOM_SEED)

train_feats, test_feats, train_lab, test_lab = train_test_split(featuresScale, one_hot, test_size=0.3, random_state=RANDOM_SEED)

print('Training Data - feature')
print(train_feats.shape)
print(type(train_feats))
print(train_feats[:5,:])
#print(train_feats)

print('Trainig Data - Label')
print(train_lab.shape)
print(type(train_lab))
print(train_lab[:5,:])

print('Testing Data - feature')
print(test_feats.shape)
print(test_feats[:5,:])

print('Testing Data - Label')
print(test_lab.shape)
print(test_lab[:5,:])
print(tf.argmin(test_lab[:5,:], axis=1))

feat_shape = train_feats.shape[1]
hidden_nodes = 10
out_shape = train_lab.shape[1]

graph = tf.Graph()
with graph.as_default():
  inputs = tf.compat.v1.placeholder("float", shape=[None, feat_shape])
  outputs = tf.compat.v1.placeholder("float", shape=[None, out_shape])

  W1 = tf.compat.v1.get_variable(name="W1", shape=[feat_shape, hidden_nodes], initializer=tf.compat.v1.keras.initializers.VarianceScaling(scale=1.0, mode="fan_avg", distribution="uniform"))
  
  b1 = tf.compat.v1.get_variable(name="b1", shape=[hidden_nodes], initializer=tf.compat.v1.constant_initializer(0.0))

  H1 = tf.matmul(inputs, W1) + b1
  H1 = tf.sigmoid(H1)

  W2 = tf.compat.v1.get_variable(name="W2", shape=[hidden_nodes, out_shape], initializer=tf.compat.v1.keras.initializers.VarianceScaling(scale=1.0, mode="fan_avg", distribution="uniform"))

  b2 = tf.compat.v1.get_variable(name="b2", shape=[out_shape], initializer=tf.compat.v1.constant_initializer(0.0))

  pred_tensor= tf.matmul(H1, W2) + b2
  predict = tf.argmax(input=pred_tensor, axis=1)
  pred_tensor = tf.sigmoid(pred_tensor)

  cost = tf.reduce_mean(-outputs*tf.math.log(pred_tensor) - (1-outputs)*tf.math.log(1-pred_tensor))
  updates = tf.compat.v1.train.GradientDescentOptimizer(0.01).minimize(cost)

  with tf.compat.v1.Session(graph = graph) as sess:
    init = tf.compat.v1.global_variables_initializer()
    sess.run(init)

    for epoch in range(1000):
      for i in range(len(train_feats)):
        op, cst = sess.run([updates, cost], feed_dict={inputs: train_feats[i: i + 1], outputs: train_lab[i: i + 1]})


      test_accuracy = np.mean(np.argmax(test_lab, axis=1) == sess.run(predict, feed_dict={inputs: test_feats, outputs: test_lab}))

      if (epoch % 100) == 0:
        print("Epoch: %d, acc: %.2f, cost: %.5f" % (epoch, test_accuracy, cst))

    print('Test Accuracy: %.5f' % test_accuracy)
    print('Input-Hidden Layer Weights =', sess.run(W1))
    print('Input-Hidden Layer Bias =', sess.run(b1))
    print('Hidden-Output Weights =', sess.run(W2))
    print('Hidden-Output Bias =', sess.run(b2))

from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential()
model.add(Dense(10, activation='relu', input_dim=feat_shape))
model.add(Dense(out_shape, activation='softmax'))

model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=['mse'])

model.summary()

print(train_feats.shape)
print(train_lab.shape)

model.fit(train_feats, train_lab, epochs=1000, batch_size=128)

print(model.metrics_names)
score = model.evaluate(test_feats, test_lab, batch_size=128)
print(score)

out = model.predict(test_feats, batch_size=None, verbose=0, steps=None)

test_accuracy = np.mean(np.argmax(test_lab, axis=1) == np.argmax(out, axis=1))

print('Test Accuracy:', test_accuracy)

weightBias0 = model.layers[0].get_weights()

print('Input-Hidden Layer Weights =', weightBias0[0])
print('Input-Hidden Layer Bias =', weightBias0[1])

weightBias1 = model.layers[1].get_weights()

print('Hidden-Output Weights =', weightBias1[0])
print('Hidden-Output Bias =', weightBias1[1])