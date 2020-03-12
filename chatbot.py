import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tensorflow as tf
import tflearn
import random
import json

with open("topics.json") as file:
    data = json.load(file)


    words = []
    labels = []
    list_x = []
    list_y = []
        
    for topic in data["topics"]:
        for pattern in topic["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            list_x.append(wrds)
            list_y.append(topic["tag"])
        
        if topic["tag"] not in labels:
            labels.append(topic["tag"])
         
    words = [stemmer.stem(w.lower()) for w in words]
    words = sorted(list(set(words)))
    
    labels = sorted(labels)
    
    training = []
    output = []
    
    empty = [0 for _ in range(len(labels))]
    
    for x, list in enumerate(list_x):
        bag = []
        
        wrds = [stemmer.stem(w.lower()) for w in list if w != "?"]
        
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)
            
        output_x = empty[:]
        output_x[labels.index(list_y[x]) ] = 1
    
        training.append(bag)
        output.append(output_x)

    training = numpy.array(training)
    output = numpy.array(output)

tf.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 16)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

model.fit(training, output, n_epoch=1000, batch_size=10, show_metric=True)
model.save("model.tflearn")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)


def chat():
    print("Hi, I'm RamsayBot \n Type 'quit' to leave ")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        for tg in data["topics"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        print(random.choice(responses))

chat()

