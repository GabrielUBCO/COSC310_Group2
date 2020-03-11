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
        r"who are you?|whats your name?|who are you|what's your name|",
        ["Hey I'm Gordon Ramsay, Chef and Restauranteur, 24 Restaurants accross the world. You know who the best chef is?",]
    ],
    [
        r"how are you?|how are you doing?|how is it going?",
        ["I'm doing good\nHow about You?",]
    ],
    [
        r"whats your (.*) dish?|whats your (.*) food?",
        ["Not to toot my own horn, but nothing beats a well prepared beef wellington",]
    ],
    [
        r"how (.*) steak|how (.*) this",
        ["well... \nIT'S RAWWWW!!",]
    ],
    [
        r"wassup?|what's up?|sup?",
        ["this conversation is a disaster, just like pineapple on pizza/n*tosses plate*",]
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
        ["I am 53 years old"]

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
        r"No|Not yet|nope|nah",
        ["It's okay. You sack of uselessness."]
    ],
    [
        r"Yes|yep|yeah|yah|yes",
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
