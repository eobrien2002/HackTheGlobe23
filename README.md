# HackTheGlobe23
This code seems to implement a chatbot using a combination of Word2Vec and BERT models. The chatbot is trained on a JSON file containing intent patterns and corresponding responses. The Word2Vec model is used to convert the text input into numerical vectors, which are then encoded using a LabelEncoder. The BERT tokenizer is used to tokenize the input text, which is then passed through the chatbot model to predict the intent. Finally, the predicted intent is used to map to an appropriate response from the intent data in the JSON file

train_model --> Notebook to train the custom BERT model on the intents file.

Chatbot_main --> Script to run the chatbot.

Intents --> The predefined responses for the chatbot, Feel free to add

***Working on compressing a version of the model so it can be deployed on a dummy-phone
