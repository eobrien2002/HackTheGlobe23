# Import necessary libraries
import json
import random
import numpy as np
import nltk
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense, Input
from keras.optimizers import Adam
from transformers import TFBertModel, BertTokenizer
from gensim.models import Word2Vec
import tensorflow as tf
from keras.callbacks import EarlyStopping
import tensorflow as tf
from keras.models import load_model
from keras.utils import custom_object_scope
from transformers import TFBertModel
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Read in the training data from intents.json file
with open('intents.json') as json_file:
    data = json.load(json_file)

# Download the nltk punkt tokenizer
nltk.download("punkt",quiet=True)

# Extract sentences and labels from the training data
sentences, y, labels = [], [], []
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        # Tokenize each pattern into individual words and add to sentences
        sentences.append(nltk.word_tokenize(pattern.lower()))
        # Append the corresponding label for this pattern to y
        y.append(intent["tag"])
    # Add this label to the list of unique labels if it's not already present
    if intent["tag"] not in labels:
        labels.append(intent["tag"])

# Train Word2Vec model on the tokenized sentences
word2vec = Word2Vec(sentences, min_count=1, vector_size=100)

# Convert text to numerical vectors using the trained Word2Vec model
max_len = max([len(s) for s in sentences])
# Initialize a numpy array to hold the numerical vector representations of the training data
X = np.zeros((len(sentences), max_len, 100))
# Loop through each sentence and its corresponding numerical vector representation
for i, sentence in enumerate(sentences):
    # Loop through each word in the sentence and its corresponding numerical vector representation
    for j, word in enumerate(sentence):
        # Retrieve the numerical vector representation of the word from the trained Word2Vec model and store it in X
        X[i, j] = word2vec.wv[word]


# Encode the labels using a LabelEncoder from scikit-learn
label_encoder = LabelEncoder()
y_vec = label_encoder.fit_transform(y)

# Initialize a BERT tokenizer from the transformers library
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Define a function to tokenize a list of sentences using the BERT tokenizer
def tokenize(sentences, tokenizer, max_len):
    input_ids, input_mask, input_type_ids = [], [], []

    for sent in sentences:
        # Tokenize each sentence using the BERT tokenizer with max_length and truncation
        tokens = tokenizer(sent, padding="max_length", truncation=True, max_length=max_len)
        # Append the tokenized inputs to the respective lists
        input_ids.append(tokens["input_ids"])
        input_mask.append(tokens["attention_mask"])
        input_type_ids.append(tokens["token_type_ids"])

    return np.array(input_ids), np.array(input_mask), np.array(input_type_ids)

# Register a custom object for the TFBertModel layer
with custom_object_scope({'TFBertModel': TFBertModel}):
    # Load the saved chatbot model
    model = load_model('telehealth_chatbot.h5')


# Define a function to predict the intent of a user's input using the chatbot model
def predict_intent(text, model, tokenizer, word2vec, label_encoder):
    # Tokenize the input text using nltk punkt tokenizer and join the tokens into a string
    tokens = nltk.word_tokenize(text.lower())
    tokenized_text = " ".join(tokens)
    # Tokenize the input text using the BERT tokenizer
    input_ids, input_mask, input_type_ids = tokenize([tokenized_text], tokenizer, max_len)
    # Predict the intent using the chatbot model and return
    probabilities = model.predict([input_ids, input_mask, input_type_ids],verbose=False)[0]
    intent_idx = np.argmax(probabilities)
    # Convert the predicted intent index back into its original label using the LabelEncoder
    return label_encoder.inverse_transform([intent_idx])[0]


with open('intents.json') as file:
    intent_data_chatbot = json.load(file)['intents']


@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()
    user_input = data['message']

    # predict intent
    intent = predict_intent(user_input, model, tokenizer, word2vec, label_encoder)

    # map intent to response
    for intent_data in intent_data_chatbot:
        if intent_data['tag'] == intent:
            # Choose a random response from the responses associated with this intent
            response = random.choice(intent_data['responses'])
            break
    
    return ({'message': response})

if __name__ == '__main__':
    app.run()


    
