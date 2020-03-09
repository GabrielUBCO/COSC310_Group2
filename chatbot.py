import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"who are you?",
        ["Hey I'm Gordon Ramsay, Chef and Restauranteur, 24 Restaurants accross the world",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You?",]
    ],
    [
        r"sorry (.*)",
        ["WHAT ARE YOU","You're an IDIOT SANDWICH",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey",]
    ],
    [
        r"(.*) age?",
        ["53"]

    ],
    [
        r"what (.*) want ?",
        ["THE LAMB SAUCE!!!!",]

    ],
    [
        r"quit",
        ["","bye then"]

    ],
]

def chatty():
    print("Hi, I'm Gordon Ramsay \n Type quit to leave ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatty()
