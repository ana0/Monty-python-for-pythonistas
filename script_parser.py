import nltk.data

def read_script():
    f = open('all_scripts.txt', 'r')
    tokenized = []
    for line in f:
        tokens = nltk.word_tokenize(line.decode('utf-8'))
        if len(tokens) > 0:
            tokenized.extend(tokens)
    print "tokenized"
    return tokenized

def make_singles(tokens):
    singles = []
    for token in tokens:
        if "'" in token:
            token = token.strip("'")
        if token.isalnum():
            singles.append(token.lower())
    print "made singles"
    return singles

def make_bigrams(tokens):
    bigrams_list = []
    bigrams = nltk.bigrams(tokens)
    for bigram in bigrams:
        bigrams_list.append(bigram[0].lower() + bigram[1].lower())
    print "made bigrams"
    return bigrams_list

def make_trigrams(tokens):
    trigrams_list = []
    trigrams = nltk.ngrams(tokens, 3)
    for trigram in trigrams:
        trigrams_list.append(trigram[0].lower() + trigram[1].lower() + trigram[2].lower())
    print "made trigrams"
    return trigrams


