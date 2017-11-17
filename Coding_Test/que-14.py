#code to generate POS tags in a sentence
"""import nltk
sentences = "I am good with text data"
tag = nltk.sent_tokenize(sentences.strip())
tag = [nltk.word_tokenize(sent) for sent in tag]
tag = [nltk.pos_tag(sent) for sent in tag]
print(tag)
"""
items =[1,2,3,4,5]
def twice(x):
    return x+x
print(map(twice, items))
#O/P: [2, 4, 6, 8, 10]
