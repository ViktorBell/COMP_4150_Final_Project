// src/App.tsx

import React from 'react';
import './App.css';
import Register from './Register';
import Login from './Login';
import ProductPage from './ProductPage';

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

      <div className="App">
        <header className="App-header">
          <h1>Fiction 2 Form</h1>
            <p>3D Models - Customizations - Shipped to You</p>
        </header>
        <main>
            <div className="animated-boxes">
                <ul>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                </ul>
            </div>
            <div className={"login-button"}>
                <Link to={"/Login"}><button className="login-button-button">Login</button></Link>
                <Link to={"/ProductPage"}><button className="login-button-button">Products</button></Link>
                <Link to={"/Register"}><button className="login-button-button">Register</button></Link>
            </div>
        </main>
          <Routes>
              <Route path="/Login" element={<Login/>} ></Route>
              <Route path={"/ProductPage"} element={<ProductPage/>}></Route>
              <Route path="/Register" element={<Register/>}></Route>
          </Routes>
      </div>


  );
}

export default App;
