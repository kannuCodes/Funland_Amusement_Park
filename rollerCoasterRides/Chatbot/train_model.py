
# MAKING THE DATASET  TO DIFFERENT LIST OF QUESTIONS AND ANSWERS
# -----------------------------------------------------------------

import os 
import json
# from dataset_loader import Chatbot_Dataset
from rollerCoasterRides.views import load_chatbot_dataset

data = load_chatbot_dataset()

questions = []
answers = []

for item in data :
    questions.append(item["word"])
    answers.append(item["meaning"])

print("Questions",questions[:5]) 
print("Answers:",answers[:5])  

# VECTORIZATION OF THE QUESTIONS FROM DATASET
# ------------------------------------------------------

from sklearn.feature_extraction.text import TfidfVectorizer

Vectorizer = TfidfVectorizer()


X =Vectorizer.fit_transform(questions)

print("Shape of TF-IDF Matrix : ",X.shape)

# TRAINING THE MODEL
# -----------------------------------------------------
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X,answers)

print("Model Trained Successfully")

#   website cannot always train and vectorise data everytime its loaded so now
# to save the model to directly load and decode the questions 

import pickle
# PICKLE is the library used to store objects to files 

# ---------------------------------------
# save the trained model
with open("chatbot_model.pkl","wb") as f:
    pickle.dump(model,f)

# save the vectorizer 
with open ("vectorizer.pkl","wb") as f:
    pickle.dump(Vectorizer , f)  

print("Model and  vectorizer saved successfully")      