import React from "react"
import {  Route,  ReactLocation } from "react-location";
import Footer from "./Footer";
import Home from "./Home";
import Tracks from "./Tracks";
import Yoga from "./Yoga";

export const routes: Route[] = [

{
        path:"/",
        element:<Home/>

},
{
        path:"/yoga",
        element:<Yoga/>
},

{
        path:"/tracks",
        element:<Tracks/>
},

{
        path:"/footer",
        element:<Footer/>
},



];

export const location = new ReactLocation();