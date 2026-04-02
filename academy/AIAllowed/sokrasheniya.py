import re
import unicodedata
from spellchecker import SpellChecker
from yastrider import normalize_text




text = "I can't go to café cuz I havv a meeeting!!!"
normalize_text(text)

# === 1. Словарь сокращений ===
CONTRACTIONS = {
    "don't": "do not",
    "can't": "cannot",
    "i'm": "i am",
    "it's": "it is",
    "you're": "you are",
    "isn't": "is not",
    "won't": "will not",
    "should've": "should have",
    'cuz': 'because'
}

def expand_contractions(text: str) -> str:
    """
    Раскрытие сокращений (don't -> do not)
    """
    pattern = re.compile(r'\b(' + '|'.join(CONTRACTIONS.keys()) + r')\b')

    def replace(match):
        return CONTRACTIONS[match.group(0)]

    return pattern.sub(replace, text)

def remove_accents(text: str) -> str:
    """
    Удаление акцентов (café -> cafe)
    """
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('utf-8')
    return text

def correct_spelling(text: str) -> str:
    """
    Исправление опечаток
    """
    spell = SpellChecker()
    corrected = []

    for word in text.split():
        corrected.append(spell.correction(word) or word)

    return " ".join(corrected)

def normalize_text(text: str) -> str:
    """
    Полная нормализация текста
    """

    # 1. lowercase
    text = text.lower()
    # Зачем: уменьшает размер словаря :contentReference[oaicite:1]{index=1}  

    # 2. раскрытие сокращений
    text = expand_contractions(text)
    # Зачем: "don't" и "do not" должны быть одинаковыми :contentReference[oaicite:2]{index=2}  

    # 3. удаление акцентов
    text = remove_accents(text)
    # Зачем: café = cafe :contentReference[oaicite:3]{index=3}  

    # 4. удаление лишних символов (опционально)
    text = re.sub(r'[^\w\s]', ' ', text)

    # 5. исправление опечаток
    text = correct_spelling(text)
    # Зачем: улучшает качество модели :contentReference[oaicite:4]{index=4}  

    # 6. нормализация пробелов
    text = re.sub(r'\s+', ' ', text).strip()

    return text


normalized = normalize_text(text)

print("Исходный:", text)
print("Нормализованный:", normalized)


















































