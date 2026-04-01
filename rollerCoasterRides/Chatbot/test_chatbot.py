import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "chatbot_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")


with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

# stopwords_path = os.path.join(BASE_DIR, "stopWords.txt")

# with open(stopwords_path, "r") as f:
#     stopwords = set(line.strip() for line in f if line.strip())


# stopwords = [ "a","an","the","is","am","are","was","were","be","been","being", "what","which","who","whom","whose","this","that","these","those", "and","or","but","if","because","as","until","while", "of","at","by","for","with","about","against","between","into", "through","during","before","after","above","below","to","from", "up","down","in","out","on","off","over","under", "again","further","then","once", "here","there","when","where","why","how", "all","any","both","each","few","more","most","other","some","such", "no","nor","not","only","own","same","so","than","too","very", "can","will","just","should","now", "i","me","my","mine","we","our","ours","you","your","yours", "he","him","his","she","her","hers","it","its","they","them","their","theirs" ]

stopwords = [
    "a", "an", "the",
    "is", "am", "are", "was", "were", "be", "been", "being",
    "what", "which", "who", "whom", "whose", "this", "that", "these", "those",
    "and", "or", "but", "if", "because", "as", "until", "while",
    "of", "at", "by", "for", "with", "about", "against", "between", "into",
    "through", "during", "before", "after", "above", "below", "to", "from",
    "up", "down", "in", "out", "on", "off", "over", "under",
    "again", "further", "then", "once",
    "here", "there", "when", "where", "why", "how",
    "all", "any", "both", "each", "few", "more", "most", "other", "some", "such",
    "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very",
    "can", "will", "just", "should", "now",
    "i", "me", "my", "mine", "we", "our", "ours", "you", "your", "yours",
    "he", "him", "his", "she", "her", "hers", "it", "its", "they", "them", "their", "theirs"
]
# Function 
def clean_text(text):
    words = text.lower().split()
    filtered = [word for word in words if word not in stopwords]
    return " ".join(filtered)



print("Chatbot is ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    # Exit check FIRST
    if user_input.lower() == "exit":
        break

    # Clean input
    to_model = clean_text(user_input)

    # Convert to vector
    user_vector = vectorizer.transform([to_model])

    # Predict
    prediction = model.predict(user_vector)

    print("Bot:", prediction[0])





# import os 
# import pickle 

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# model_path = os.path.join(BASE_DIR,"chatbot_model.pkl")
# vectorizer_path = os.path.join(BASE_DIR,"vectorizer.pkl")

# with open(model_path,"rb") as f:
#     model = pickle.load(f)

# # Load vectorizer
# with open(vectorizer_path,"rb") as f:
#     vectorizer = pickle.load(f)

# print("Chatbot is ready! Type 'exit' to stop. \n")

# while True:
#     user_input = input("You: ")
#     stopwords = [
#     "a", "an", "the",
#     "is", "am", "are", "was", "were", "be", "been", "being",
#     "what", "which", "who", "whom", "whose", "this", "that", "these", "those",
#     "and", "or", "but", "if", "because", "as", "until", "while",
#     "of", "at", "by", "for", "with", "about", "against", "between", "into",
#     "through", "during", "before", "after", "above", "below", "to", "from",
#     "up", "down", "in", "out", "on", "off", "over", "under",
#     "again", "further", "then", "once",
#     "here", "there", "when", "where", "why", "how",
#     "all", "any", "both", "each", "few", "more", "most", "other", "some", "such",
#     "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very",
#     "can", "will", "just", "should", "now",
#     "i", "me", "my", "mine", "we", "our", "ours", "you", "your", "yours",
#     "he", "him", "his", "she", "her", "hers", "it", "its", "they", "them", "their", "theirs"
#     ]
#     def clean_text(user_input):
#      user_input = user_input.lower().split()
#      filtered = [word for word in user_input if word not in stopwords]
#      ask = " ".join(filtered)
#      return ask 
#     user_input = "What is this amusement park about?"
#     to_model=clean_text(user_input)
#     if user_input.lower() == "exit":
#         break

#     user_vector = vectorizer.transform([to_model])

#     prediction = model.predict(user_vector)

#     print("Bot:",prediction[0])