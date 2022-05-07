import './App.css';
import React from 'react'
import { Router, Outlet } from 'react-location';
import { routes, location } from "./router"



function App() {
    return (
        <Router routes={routes} location={location}>
        <div className="App" >
            <Outlet />
        </div>
        </Router>
    );
}

export default App;
