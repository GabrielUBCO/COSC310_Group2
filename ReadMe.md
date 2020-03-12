RamsayBot

Written in Python 3.6.1 via conda virtual environment
Packages used:
nltk 3.4.5
numpy 1.18.1
tensorflow 1.13.1
tflearn 0.3.2
json5 0.9.1

A list of topics, including question patterns and responses is saved to a JSON file named topics.

The questions are then tokenized in to a list of words using nltk's word tolkenizer and added to words[]

Those lists are then added into list_x[] and the corresponding topics added to list_y[]

The words are then stemmed meaning reduced to the root using Lancaster stemming algorith(e.g. playing reduced play) then put into a set to remove duplicates.

The set is then made back into a list then sorted, topics are also sorted.

A training[] and output[] numpy array are initialized.(Numpy arrays are easier to operate on)

The lists of words from list_x are then stemmed, lowercased and added to a bag array as 1s if they exist in words[] and 0s if they don't.

Add the bag array to training.

We then create a simple neural network.

This one has a input layer, 3 hidden layers with 16 neurons, 16 neurons and 8 neurons respectively and an output layer.

The model is then trained using this neural network to learn to predict the users intention when they ask questions.

Each input in training[] passes through every neuron on the first hidden layer and from each on that layer to each neuron on the next, and so on.

The traing goes through 1000 cycles in batches of 10.

The bag_of_words function is used to compare the words from the user input to each bags of words to predict which topic the question pertains to.

The chat fuction allows the user to chat with RamsayBot.

RamsayBot will try to give a suitable response depending on what it predicts to be the topic of the question given.





