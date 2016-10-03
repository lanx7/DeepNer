import tensorflow as tf
import numpy as np
import os

def normalize(str):
    print "Orig> " + str
    str = str.lower()
    str = str.replace("."," . ")
    print "Norm> " + str
    return str

def get_id(str):
    try:
        id = vocab[str]
    except KeyError:
        id = 0
    return id

def feature_factory(str):
    global vocab, wordvec
    str = normalize(str)
    tokens = str.split(" ")
    n = len(tokens)
    features = []
    for idx in xrange(n-1):
        vec = []
        curr = tokens[idx]
        if(idx == 0):
            prev = "<s>"
        else:
            prev = tokens[idx-1]

        print idx, n-1
        if(idx == (n-2)):
            next = "</s>"
        else:
            next = tokens[idx+1]

        vec.append(get_id(prev))
        vec.append(get_id(curr))
        vec.append(get_id(next))
        print vec
        features.append(vec)

    for feature in features:
        print feature
        a = wordvec[feature[0]]
        b = wordvec[feature[1]]
        c = wordvec[feature[2]]
        d = np.concatenate((a,b,c), axis=0)
        print d

fv = open("data/vocab.txt","r")
buffer = fv.readlines()
vocab = {}
for idx, buf in enumerate(buffer):
    print idx, buf.strip()
    vocab[buf.strip()] = idx;

sample_str = "George is happy about the election outcome."
wordvec = np.genfromtxt('data/wordVectors.txt', delimiter=' ')
feature_factory(sample_str)





