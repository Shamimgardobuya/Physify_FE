import './App.css';
import Login from './components/Login';
import Question from './components/Question';
import { BrowserRouter,   Route, Routes} from "react-router-dom";
import Answers from './components/ListAnswers';
import Answer from './components/Answer';
import ListQuestions from './components/ListQuestions';

function App() {
  return (
    <main className="App">
      <h1> Physics App</h1>
      <BrowserRouter
      >
        <Routes>
          <Route element={<Login/>} path='/'/>
          <Route element={<Question/>} path='/question'/>
          <Route element={<Answer/>} path='/answer/:question_id'/>
          <Route element={<Answers />} path='questions/:id'/>
          <Route element={<ListQuestions />} path='/questions'/>

        </Routes>
      </BrowserRouter>
        <>
        </>
  

    </main>
  );
}

export default App;
