import logo from './logo.svg';
import './App.css';
// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import TaskList from './components/TaskList';
// Import other components as needed

const App = () => {
    return (
        <Router>
            <div>
                <h1>Task Management</h1>
                <Routes>
                    <Route path="/" element={<TaskList />} />
                    {/* Add routes for other components here */}
                </Routes>
            </div>
        </Router>
    );
};

export default App;

