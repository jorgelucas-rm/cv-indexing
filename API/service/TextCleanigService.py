import spacy
from spacy.lang.en import stop_words
from spacypdfreader.spacypdfreader import pdf_reader
from string import punctuation
import re

stopWords = stop_words.STOP_WORDS
punctuations = list(punctuation)
nlp = spacy.load("en_core_web_sm")

class TextCleaningService:

    def CleanText(pdf):
        text = pdf_reader(pdf, nlp)
        text = TextCleaningService.especialCleaning(text)
        text = TextCleaningService.lemmatization(text)
        text = TextCleaningService.stopwordCleaning(text)
        text = TextCleaningService.toString(text)
        return text    


    def especialCleaning(text):
        text  = re.sub(r'[^a-zA-Z0-9\s]', '', text.text)
        return text

    def lemmatization(text):
        text = nlp(text)
        text = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower for word in text ]
        return text

    def stopwordCleaning(text):
        text = [ word for word in text if word not in stopWords and word not in punctuations ]
        return text


    def toString(text):
        text = ' '.join(text)
        text = " ".join(text.split())
        return text