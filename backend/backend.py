import pickle
import joblib
from fastapi import FastAPI
import spacy
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import json
import pandas as pd


df_description=pd.read_csv(r'symptom_Description.csv')
df_precautions=pd.read_csv(r'symptom_precaution.csv')

nlp=spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)
    stemmed_tokens = []
    for token in doc:
        if token.is_alpha and not token.is_stop:
            lemma = token.lemma_.lower()
            stemmed_tokens.append(lemma)
    processed_text = ' '.join(stemmed_tokens)

    return processed_text

tfidf_vectorizer = joblib.load(r'tfidf.pkl') 
label_encoder = joblib.load(r'label_encoder.pkl')


app=FastAPI(title="Disease prediction API")
MODEL_PATH=r'voting_classifier_model_Disease_pred_97_percent_acc.pkl'
mymodel=joblib.load(MODEL_PATH)


@app.get("/disease_prediction/{sample_text}")

async def predict_disease(sample_text :str):
    sample_text_processed = preprocess_text(sample_text)
    sample_text_transformed = tfidf_vectorizer.transform([sample_text_processed])
    result = label_encoder.inverse_transform(mymodel.predict(sample_text_transformed))
    return result[0]
    # return sample_text


