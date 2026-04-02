import nltk
nltk.download()
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize, word_tokenize
import spacy
from textblob import Word
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
from gensim.models import FastText
from transformers import AutoTokenizer, AutoModel
import torch

text = 'Running run runs badly fearless susuper unnormal'

# def get_wordnet_pos(treebank_tef):
#     if treebank_tef.startswith('J'):
#         return wordnet.ADJ
#     elif treebank_tef.startswith('V'):
#         return wordnet.VERB
#     elif treebank_tef.startswith('N'):
#         return wordnet.NOUN
#     elif treebank_tef.startswith('R'):
#         return wordnet.ADV
#     else:
#         return wordnet.NOUN
# lemmatizer = WordNetLemmatizer()
# tokens = nltk.word_tokenize(text)
# post = nltk.pos_tag(tokens)
# l = [lemmatizer.lemmatize(word,get_wordnet_pos(pos)) for word, pos in post]
# print(f'TEXT: {l}')



# nlp = spacy.load('en_core_web_sm')
# doc = nlp(text)
# lammas = [token.lemma_ for token in doc]
# print(Word('words').lemmatize())
# print(Word('words').lemmatize('a'))



corpus = [
    "I love NLP and Python",
    "Python makes NLP tasks easier",
    "I love machine learning"
]

vectorizer = CountVectorizer()
X_bow = vectorizer.fit_transform(corpus)

print("Feature names:", vectorizer.get_feature_names_out())
print("BoW matrix:\n", X_bow.toarray())

vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(corpus)

print("TF-IDF features:", vectorizer.get_feature_names_out())
print("TF-IDF matrix:\n", X_tfidf.toarray())

# corpus должен быть списком токенизированных предложений
sentences = [
    ["i", "love", "nlp"],
    ["python", "nlp", "easy"],
    ["nlp", "and", "machine", "learning"]
]

model = Word2Vec(sentences, vector_size=100, window=5, min_count=1)
print(model.wv['nlp'])  # вектор для слова 'nlp'

model_ft = FastText(sentences, vector_size=100, window=3, min_count=1)
print(model_ft.wv['nlp'])

print(torch.__version__)
print(torch.cuda.is_available())  # True если есть GPU

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

text = "I love natural language processing"
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)

# CLS-вектор — обобщённый вектор предложения
cls_vector = outputs.last_hidden_state[:, 0, :]
print(cls_vector)






# :) :3 :^ 









































































































