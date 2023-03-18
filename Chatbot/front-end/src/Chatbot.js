//Chatbot.js
import React, { useState } from 'react'
import { Button } from 'react-bootstrap'
import ChatMessage from './ChatMessage'
import './chatbot.css'

export default function Chatbot() {
  const [messages, setMessages] = useState([            
    {
      message: 'Hello, How can I help you today?'
    }

  ]);

  const [text, setText] = useState('')                  //user input state variable


  //this method deals with the post request
  const fetchChatbot = (message) => {
    const inputData = {
      message: message,
  
    };
    return fetch('http://localhost:5000/get_response', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
        'Access-Control-Allow-Credentials': true,
        'Server': 'Werkzeug/2.2.3 Python/3.11.2',
      },
      body: JSON.stringify(inputData)
    })
      .then(res => res.json())
      

  };


  //when button is clicked 
  const onSend = () => {
    console.log(text);

    let list = [...messages, { message: text, user: true }];  //list variable will store all the messages that the chatbot will output
    fetchChatbot(text).then((botreply) => {   //call the post request method
      list = [...list, botreply];                     //append the result from this method to the list of messages the bot will show
      setMessages(list);                                //set the message to the list 
      setText('');                                      //set user input text to empty 
    });

    setMessages(list);
    setText('');


    setTimeout(() => {
      document.querySelector('#copyright').scrollIntoView();
    });
  };


  return (

    <div class="local">
      <div className='d-flex align-items-center justify-content-center mt-1'>
    
        <h2 className='text-primary'>GoKlinik</h2>
      </div>
      <div className='chat-message'>
        {messages.length > 0 && messages.map((data) => <ChatMessage {...data} />)}
        <div className='d-flex mt-2'>
          <input type='text' className='form-control' value={text} onChange={(e) => setText(e.target.value)} />
          <Button type='primary' className='ms-3' onClick={onSend}>Send</Button>
        </div>
        <div id='copyright' className='mt-3'>
          
        </div>
      </div>
    </div>

  )
}


