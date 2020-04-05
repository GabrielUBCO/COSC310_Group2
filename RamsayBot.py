import nltk
from nltk.corpus import wordnet
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

from spellchecker import SpellChecker
import numpy
import tensorflow as tf
import tflearn
import random
import json
import tkinter
from tkinter import *

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
net = tflearn.fully_connected(net, 16)
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
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg.lower() == "quit":
        base.destroy()
        
    if msg != '':
        results = model.predict([bag_of_words(msg, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        
        for tg in data["topics"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="white", font=("Arial", 12 ))

        res = random.choice(responses)
        ChatLog.insert(END, "Gordon: " + res + '\n\n')
        
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


base = Tk()
base.title("RamsayBot")
base.geometry("800x450")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="#404040", height="10", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=2,
                    bd=0, bg="#FFB266", activebackground="white",fg='#ffffff',
                    command= chat )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="#E0E0E0",width="29", height="2", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=784,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=800)
EntryBox.place(x=128, y=401, height=30, width=660)
SendButton.place(x=6, y=401, height=30)

def greet():
    ChatLog.config(state=NORMAL)
    ChatLog.insert(END, "Hi, I'm RamsayBot \n Type 'quit' to leave " + '\n\n')
    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)

base.after(0, greet)
base.mainloop()
