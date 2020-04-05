RamsayBot

Written in Python 3.6.1 via conda virtual environment
Packages used:
nltk 3.4.5,
numpy 1.18.1,
tensorflow 1.13.1,
tflearn 0.3.2,
json5 0.9.1.

A list of topics, including question patterns and responses is saved to a JSON file named topics.

The questions are then tokenized in to a list of words using nltk's word tolkenizer and added to words[]

Those lists are then added into list_x[] and the corresponding topics added to list_y[]

The words are then stemmed, meaning reduced to the root using Lancaster stemming algorithm (e.g. playing reduced play) then put into a set to remove duplicates.

The set is then made back into a list then sorted; topics are also sorted.

A training[] and output[] numpy array are initialized.(Numpy arrays are easier to operate on)

The lists of words from list_x are then stemmed, lowercased, and added to a bag array as 1s if they exist in words[] and 0s if they don't.

Add the bag array to training.

We then create a simple neural network.

This one has a input layer, 3 hidden layers with 16 neurons, 16 neurons, and 8 neurons respectively and an output layer.

The model is then trained using this neural network to learn to predict the users intention when they ask questions.

Each input in training[] passes through every neuron on the first hidden layer and from each on that layer to each neuron on the next, and so on.

The training goes through 1000 cycles in batches of 10.

The bag_of_words function is used to compare the words from the user input to each bag of words to predict which topic the question pertains to.

The chat fuction allows the user to chat with RamsayBot.

RamsayBot will try to give a suitable response depending on what it predicts to be the topic of the question given.

Features programmed in assignment 3:

- GUI so user is typing into a nicer interface. GUI makes the chatbot more user friendly (easier to read, simple layout). For example, we have increased the spacing between lines of dialogue; the text is white and the background is dark, enhancing readibility.

- Extra topic to agent's repertoire: Gordon Ramsay providing relationship advice. The original topic covers content about Gordon Ramsay's personal life and answers to some general questions. The new topic focuses on relationship advice; RamsayBot will answer user's questions about relationships by providing his own advice. For example, when the user asks for dating activities, RamsayBot recommends "Cooking for each other" or "Doing exercise together", activities which Gordon Ramsay himself would enjoy.

- Feature that enables agent to give at least 5 different reasonable responses when user enters something outside the two topics. As we only have a limited set of questions, we included 5 different responses when the user enters something outside the two topics, informing the user to ask another question. This is to make the conversation as smooth and natural as possible. For example, we have included the following response when the user enters something outside the two topics: "Sorry, I am having some difficulty understanding that. Can you ask another question?"

- Feature that enables agent to handle spelling mistakes of the words which agent should recognize. We have included a feature that enables the agent to provide a suitable response when the user types a question with spelling errors in it. This is to make the conversation as smooth and natural as possible. For example, when the user types "what si your favourit sport", the agent will recognize the spelling errors and provide the standard reply.

- Feature that enables agent to recognize synonyms and handle them appropriately. We have included a feature that enables the agent to provide a suitable response when the user types a question using a synonym for any of the tags listed under topics.json. This is to make the conversation as smooth and natural as possible. For example, when the user asks "Should I prioritize my career or my relationship?" or "Should I prioritize my job or my relationship?", the agent will provide the same answer since 'career' and 'job' have the same meaning.

- Feature that enables agent to have a conversation with another agent via sockets. As one of the goals of the assignment is for our chatbot to be able to have a conversation with another chatbot in class via sockets, we have included this feature into our chatbot. However, as we do not have access to any other chatbots from the class due to the current circumstances, we are unable to demonstrate this feature.



