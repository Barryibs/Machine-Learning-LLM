import spacy
from nltk.corpus import stopwords
import string
import re
import tarfile
import contractions


def import_tarfile(path, destination_directory):
    
    """
    To extract the contents of a gzip compressed tar file.
    
    Exemple usage:
    tarfile_path = '/path/to/your/archive.tar.gz'
    destination_dir = '/path/to/your/destination_directory'
    
    """
    with tarfile.open(path, 'r:gz') as tar:
        tar.extractall(destination_directory)

def remove_stopwords(text):
    nlp = spacy.load("en_core_web_sm")
    stop_words = set(stopwords.words('english'))
    cleaned_text = ' '.join([token.text for token in nlp(text) if token.text.lower() not in stop_words])
    
def remove_punctuation(text):
    """
    Remove punctuation from the given text.
    """
    return text.translate(str.maketrans('', '', string.punctuation))
    
def remove_special_characters(text):
    """
    Remove special characters from the given text.
    """
    return ''.join(char for char in text if char.isalnum() or char.isspace())

def tokenize_and_lemmatize(text):
    """
    Tokenize and lemmatize the given text using spaCy.
    
    1. Lemmatizing is the process of converting a word into it's root (base form).
    2. Tokenization is the process of breaking down words into smaller parts so that the machine can understand it.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    lemmatized_tokens = [token.lemma_ for token in doc]
    
    for token, lemma in zip(doc, lemmatized_tokens):
        print(f'{token.text} -> {lemma}')
        
    return lemmatized_tokens

def expand_contractions(text):
    
    """
    Expanding contracted words such as don't -> do not, haven't -> have not... 
    """
    expanded_words = []
    for word in text.split():
        expanded_words.append(contractions.fix(word))
    return ''.join(expanded_words)


def preprocessor(text):
    
    """
    Remove html markup, emoticons, non-word characters and converting to lowercase
    """
    
    text = re.sub('<[^>]*', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)',text)
    
    text = (re.sub('[\W]+', ' ', text.lower()) +
    ' '.join(emoticons).replace('-', '')) 
    return text

def clean_text(text):
    """
    Clean text by removing punctuation, special characters, contractions
    and applying tokenization and lemmatization.
    """
    # Remove punctuation
    text = remove_punctuation(text)
    
    # Remove special characters
    text = remove_special_characters(text)
    
    # expanding contracted words
    text = expand_contractions(text)

    # Tokenize and lemmatize
    cleaned_tokens = tokenize_and_lemmatize(text)
    
    # Join the cleaned tokens into a string
    cleaned_text = ' '.join(cleaned_tokens)
    
    
    return cleaned_text
