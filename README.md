# HackTheGlobe23
## Overview
This chatbot uses a combination of Word2Vec and BERT models. The chatbot is trained on a JSON file containing intent patterns and corresponding responses. The Word2Vec model is used to convert the text input into numerical vectors, which are then encoded using a LabelEncoder. and fed into the BERT tokenizer. The BERT tokenizer is used to tokenize the input text, which is then passed through the BERT architecture to train a custom model to predict the intent of the user's message. The fine-tuned BERT model predicts the intent tag which is mapped to an appropriate response from the intent data in the JSON file.

## Instructions

### 1. Run train_model.ipynb 
This notebook will fine-tune the BERT model and save it locally as telehealth_chatbot.h5
### 2. Move telehealth_chatbot.h5 to the backend folder
The backend folder is inside the Chatbot folder. 
## 3. cd Chatbot --> cd front-end --> npm i
This installs all node_modules for the React App
### 4. cd Chatbot --> cd backend --> flask run
This runs the API which sends a JSON file with the response from the backend to the front end
### 5. cd Chatbot --> cd front-end --> npm start
This hosts the website locally

