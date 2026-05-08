import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()

def clean_text(text):

    text = str(text)

    text = text.lower()

    # Remove URLs
    text = re.sub(
        r'http\\S+|www\\S+|https\\S+',
        '',
        text
    )

    # Remove HTML
    text = re.sub(r'<.*?>', '', text)

    # Remove numbers
    text = re.sub(r'\\d+', '', text)

    # Remove punctuation
    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    # Remove extra spaces
    text = text.strip()

    text = re.sub(r'\\s+', ' ', text)

    words = text.split()

    cleaned_words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    cleaned_text = ' '.join(cleaned_words)

    return cleaned_text