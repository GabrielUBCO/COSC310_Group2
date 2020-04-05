from nltk.corpus import wordnet
#this function takes in a word and a sentence and then checks if a synonym of the word exists in the sentence
def get_word_synonyms_from_sent(word, sent):
    word_synonyms = []
    for synset in wordnet.synsets(word):
        for lemma in synset.lemma_names():
            if lemma in sent and lemma != word:
                word_synonyms.append(lemma)
    return word_synonyms
#replace 'word' with the keywords for each response (use a loop to go through them)
word = "annoying"
#this will be the user's response in which we will look for synonyms for the keywords
sent = ['Yohen', 'is', 'so', 'irritating', '.']
word_synonyms = get_word_synonyms_from_sent(word, sent)
print ("word:", word)
print ("sentence:", sent)
print ("Synonyms for '" + word.upper() + "' in the sentence : " + ", ".join(word_synonyms))