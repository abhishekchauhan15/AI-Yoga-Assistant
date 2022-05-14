import React from "react"
import {  Route,  ReactLocation } from "react-location";
import Home from "./components/Home";
import Tracks from "./components/Tracks";
import Yoga from "./components/Yoga";

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



];

export const location = new ReactLocation();