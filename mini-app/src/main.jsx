import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles.css';

const telegram = window.Telegram?.WebApp;
telegram?.ready();
telegram?.expand();

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App telegram={telegram} />
  </React.StrictMode>,
);
