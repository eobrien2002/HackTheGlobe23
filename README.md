# HackTheGlobe23
This chatbot uses a combination of Word2Vec and BERT models. The chatbot is trained on a JSON file containing intent patterns and corresponding responses. The Word2Vec model is used to convert the text input into numerical vectors, which are then encoded using a LabelEncoder. The BERT tokenizer is used to tokenize the input text, which is then passed through the chatbot model to predict the intent. Finally, the predicted intent is used to map to an appropriate response from the intent data in the JSON file

train_model --> Notebook to train the custom BERT model on the intents file. This must be run first to create a version of the model on your local drive

Intents --> The predefined responses for the chatbot, Feel free to add

Chatbot --> Contains files to run the chatbot interface locally. Note, please move the `telehealth_chatbot.h5` file into the backend folder.
