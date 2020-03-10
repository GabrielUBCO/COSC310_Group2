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
        ["Hey I'm Gordon Ramsay, Chef and Restauranteur, 24 Restaurants accross the world. You know who the best chef is?",]
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
            r"(.*) you",
        ["You're not an idiot sandwich after all."]

    ],
    [
        r"No|Not yet",
        ["It's okay. You sack of uselessness."]
    ],
    [
        r"No|Not yet",
        ["It's okay. You sack of uselessness."]
    ],
    [
        r"Yes",
        ["Superb. Do you have any more questions for me?", "Good. Ask me anything else."]
    ],
    [
        r"what (.*) want ?",
        ["THE LAMB SAUCE!!!!",]

    ],
    [
        r"quit"|"Quit",
        ["","bye then"]

    ],
]

def chatty():
    print("Hi, I'm RamsayBot \n Type 'Quit' to leave ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatty()
