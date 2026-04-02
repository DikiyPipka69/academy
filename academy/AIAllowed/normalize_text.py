import re
import unicodedata
from spellchecker import SpellChecker
from yastrider import normalize_text
import string
from nltk.tokenize import sent_tokenize, word_tokenize

text = "Hello, world! How's it going?"
# normalize text
normalize_text(text)

# remove punktuation
def remove_punkt(text):
    text = re.sub(r'[^\w\s]', text)
    return text

# translate text
# translator = str.maketrans('','',string.punktuation)
# text.translate(translator)



print(remove_punkt(text))

sent_tokenize(text)
word_tokenize(text)






























































































