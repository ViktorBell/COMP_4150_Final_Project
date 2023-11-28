// src/App.tsx

import React from 'react';
import './App.css';
import Register from './Register';
import Login from './Login';

import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link
} from "react-router-dom";

//import {Link, Router, Route} from 'react-router-dom';
//import {Switch} from "@mui/material";
//import Login from './Login';
//import {Link} from "@mui/material";
//import Link from 'react-router-dom'
//import Link from 'next/link'

const App: React.FC = () => {
  return (
      <Router>
      <div className="App">
        <header className="App-header">
          <h1>Fiction 2 Form</h1>
        </header>
        <main>
            <Register/>
            <div className="animated-boxes">
                <ul>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                </ul>
            </div>
            <div className={"login-button"}>
                <button className={"login-button-button"}><Link to={"/Login"}>Login</Link></button>
            </div>
        </main>
          <Routes>
              <Route path="/Login" element={<Login/>}></Route>
          </Routes>
          <p>Already have an account? <a href={"./Login.tsx"}>Login! </a></p>
      </div>
      </Router>
  );
}

export default App;
