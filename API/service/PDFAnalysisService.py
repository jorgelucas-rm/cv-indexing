import os

import joblib
import numpy as np
import spacy
from dotenv import load_dotenv
from model.mapping import mapping
from service.ExeptionService import CustomException, PDFErrorType
from spacypdfreader.spacypdfreader import pdf_reader

load_dotenv()
nlp = spacy.load(os.getenv("spacy_en"))
directory = os.getenv("file_path")
model = joblib.load(os.getenv("model"))
vectorizer = joblib.load(os.getenv("vectorizer"))


class PDFAnalysisService:

    def PDFAnalysis(name):
        pdf = os.path.join(directory, name)

        if not os.path.exists(pdf):
            return CustomException(PDFErrorType.FILE_NOT_FOUND)

        resume = pdf_reader(pdf, nlp)

        prev = vectorizer.transform([resume.text])

        probabilities = model.predict_proba(prev)

        top_indices = np.argsort(probabilities[0])[::-1][:3]

        topProbabilities = []

        for idx in top_indices:
            class_name = [
                key for key, value in mapping.classMapping.items() if value == idx
            ][0]
            if probabilities[0][idx] * 100 > 30.0:
                prob_percent = probabilities[0][idx] * 100
                topProbabilities.append(f"{class_name}: {prob_percent:.2f}%")

        if topProbabilities == []:
            topProbabilities = ["undefined"]

        return {"The resume fits into the following professions:": topProbabilities}
