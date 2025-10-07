// import logo from './logo.svg';
// import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import HomePage from './pages/Home.jsx';
import LoginPage from './pages/FreeLancer/LoginPage.jsx';
import SignInPage from './pages/Company/signin.jsx';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<HomePage/>}/>
        <Route path='/freelancer' element={<LoginPage/>}/>
        <Route path='/company' element={<SignInPage/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
