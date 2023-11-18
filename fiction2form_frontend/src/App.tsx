// src/App.tsx

import React from 'react';
import './App.css';
import Register from './Register';

const App: React.FC = () => {
  return (
      <div className="App">
        <header className="App-header">
          <h1>Fiction 2 Form</h1>
        </header>
        <main>
          <Register />
        </main>
      </div>
  );
}

export default App;
