import React from "react"
import {  Route,  ReactLocation } from "react-location";
import Home from "./Home";
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



];

export const location = new ReactLocation();