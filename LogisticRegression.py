#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Logistic Regression
 
 References :
   - DeepLearningTutorials
   https://github.com/lisa-lab/DeepLearningTutorials


'''

import sys
import numpy
from utils import *


class LogisticRegression(object):
    def __init__(self, input, label, n_in, n_out):
        self.x = input
        self.y = label
        self.W = numpy.zeros((n_in, n_out))  # initialize W 0
        self.b = numpy.zeros(n_out)          # initialize bias 0

        # self.params = [self.W, self.b]

    def train(self, lr=0.1, input=None):
        if input is not None:
            self.x = input

        p_y_given_x = softmax(numpy.dot(self.x, self.W) + self.b)
        d_y = self.y - p_y_given_x
        
        self.W += lr * numpy.dot(self.x.T, d_y)
        self.b += lr * numpy.mean(d_y, axis=0)
        
        # cost = self.negative_log_likelihood()
        # return cost

    def negative_log_likelihood(self):
        sigmoid_activation = softmax(numpy.dot(self.x, self.W) + self.b)

        cross_entropy = - numpy.mean(
            numpy.sum(self.y * numpy.log(sigmoid_activation) +
            (1 - self.y) * numpy.log(1 - sigmoid_activation),
                      axis=1))

        return cross_entropy


    def predict(self, x):
        return softmax(numpy.dot(x, self.W) + self.b)


def test_lr(learning_rate=0.01, n_epochs=1000):
    # training data
    x = numpy.array([[1,1,1,0,0,0],
                     [1,0,1,0,0,0],
                     [1,1,1,0,0,0],
                     [0,0,1,1,1,0],
                     [0,0,1,1,0,0],
                     [0,0,1,1,1,0]])
    y = numpy.array([[1, 0],
                     [1, 0],
                     [1, 0],
                     [0, 1],
                     [0, 1],
                     [0, 1]])


    # construct LogisticRegression
    classifier = LogisticRegression(input=x, label=y, n_in=6, n_out=2)

    # train
    for epoch in xrange(n_epochs):
        classifier.train(lr=learning_rate)
        # cost = classifier.negative_log_likelihood(y=y)
        # print >> sys.stderr, 'Training epoch %d, cost is ' % epoch, cost
        learning_rate *= 0.95


    # test
    x = numpy.array([1, 1, 0, 0, 0, 0])
    print >> sys.stderr, classifier.predict(x)


if __name__ == "__main__":
    test_lr()
