import React from 'react';
import ReactDOM from 'react-dom';

import App from './App';
import Chatbot from './Chatbot';




import { 
  
  createBrowserRouter,
  RouterProvider,
   
} from 'react-router-dom';

const router = createBrowserRouter([
  {
    path:"/",
    element:<App /> ,
  },
  {
    path:"chatbot",
    element:<Chatbot /> ,
  },



  
]);


//const root = ReactDOM.createRoot(document.getElementById('root'));
ReactDOM.render(
  <>
 
    <RouterProvider router={router} />
  
  </>,

  document.getElementById('root')

);
