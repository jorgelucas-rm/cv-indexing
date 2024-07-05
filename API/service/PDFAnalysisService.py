import os

import joblib
import spacy
from dotenv import load_dotenv
from service.ClassifierService import ClassifierService
from service.ExeptionService import CustomException, PDFErrorType
from spacypdfreader.spacypdfreader import pdf_reader

load_dotenv()
nlp = spacy.load(os.getenv("spacy_en"))
directory = os.getenv("file_path")
vectorizer = joblib.load(os.getenv("vectorizer"))


class PDFAnalysisService:

    def analyse_pdf(name):
        pdf = os.path.join(directory, name)

        if not os.path.exists(pdf):
            return CustomException(PDFErrorType.FILE_NOT_FOUND)

        resume = pdf_reader(pdf, nlp)

        prev = vectorizer.transform([resume.text])

        position = ClassifierService.classClassifie(prev)
        level = ClassifierService.levelClassifie(prev)

        if position == []:
            return "Undefined"

        return "The resume fits into the following position: {} at {} level".format(
            position[0], level[0]
        )
