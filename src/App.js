import logo from './logo.svg';
import './App.css';
import Login from './components/Login';
import Logout from './components/Logout';
import Profile from './components/Profile';
import Question from './components/Question';
import UpvoteButton from './components/UpvoteButton';
import { useAuth0 } from '@auth0/auth0-react';
import { BrowserRouter, Router,   Route, Routes} from "react-router-dom";
import Answers from './components/ListAnswers';
import Test from './components/Test';
import Rend from './components/Rend';
import Answer from './components/Answer';
import ListQuestions from './components/ListQuestions';

function App() {
  const { isLoading, error } = useAuth0()
  return (
    <main className="App">
      {console.log("ususbdsub")}
      <h1> Physics App</h1>
      <BrowserRouter
      >
        <Routes>
          <Route element={<Login/>} path='/'/>
          <Route element={<Question/>} path='/question'/>
          <Route element={<Answer/>} path='/answer'/>
          <Route element={<Answers />} path='/answers'/>
          <Route element={<ListQuestions />} path='/questions'/>

          

          



        </Routes>
      </BrowserRouter>
        <>
      {/* <Login/> */}
          {/* <Login/> */}
     
        </>
  
    

     
    </main>
  );
}

export default App;
