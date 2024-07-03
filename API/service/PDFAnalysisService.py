import os

import joblib
from dotenv import load_dotenv
from service.ExeptionService import CustomException, PDFErrorType
from service.TextCleanigService import TextCleaningService as tc

load_dotenv()
directory = os.getenv("file_path")
model = joblib.load("model/cv_ai")
vectorizer = joblib.load("model/cv_vectorizer")


class PDFAnalysisService:

    def PDFAnalysis(name):
        pdf = os.path.join(directory, name)

        if not os.path.exists(pdf):
            return CustomException(PDFErrorType.FILE_NOT_FOUND)

        resume = tc.cleanText(pdf)

        prev = vectorizer.transform([resume])

        probabilities = model.predict_proba(prev)

        roleProbabilities = {
            role: prob for role, prob in zip(model.classes_, probabilities[0])
        }

        topProbabilities = dict(
            sorted(roleProbabilities.items(), key=lambda item: item[1], reverse=True)[
                :3
            ]
        )

        return {"The resume fits into the following professions:": topProbabilities}
