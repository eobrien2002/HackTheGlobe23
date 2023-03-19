# HackTheGlobe23
This chatbot uses a combination of Word2Vec and BERT models. The chatbot is trained on a JSON file containing intent patterns and corresponding responses. The Word2Vec model is used to convert the text input into numerical vectors, which are then encoded using a LabelEncoder. The BERT tokenizer is used to tokenize the input text, which is then passed through the chatbot model to predict the intent. Finally, the predicted intent is used to map to an appropriate response from the intent data in the JSON file

# Instructions

1. Run train_model.ipynb 
- This will create the model called telehealth_chatbot.h5
2. Move telehealth_chatbot.h5 to the backend folder
- The backend folder is inside the Chatbot folder
3. cd Chatbot --> cd front-end --> npm i
- This installs all node_modules
4. cd Chatbot --> cd backend --> flask run
- This runs the api
5. cd Chatbot --> cd front-end --> npm start
- This hosts the website locally

