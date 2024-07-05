import os

import joblib
import numpy as np
from dotenv import load_dotenv
from model.mapping import mapping

load_dotenv()
classModel = joblib.load(os.getenv("classModel"))
levelModel = joblib.load(os.getenv("levelModel"))
vectorizer = joblib.load(os.getenv("vectorizer"))


class ClassifierService:

    def classClassifie(prev):

        probabilities = classModel.predict_proba(prev)

        topIndex = np.argsort(probabilities[0])[::-1][:3]

        topProbabilities = []

        for idx in topIndex:
            className = [
                key for key, value in mapping.classMapping.items() if value == idx
            ][0]

            if probabilities[0][idx] * 100 > 30.0:
                classProb = probabilities[0][idx] * 100
                topProbabilities.append(f"{className.capitalize()} ({classProb:.2f}%)")

        return topProbabilities

    def levelClassifie(prev):

        probabilities = levelModel.predict_proba(prev)

        index = np.argsort(probabilities[0])[::-1][:1]

        level = [key for key, value in mapping.levelMapping.items() if value == index]

        return level
