import React from "react";
import { Route, ReactLocation } from "react-location";
import Footer from "./components/Footer";
import Home from "./components/Home";
import Tracks from "./components/Tracks";
import Yoga from "./components/Yoga";
import Dashboard from "./components/Dashboard";

export const routes: Route[] = [
  {
    path: "/",
    element: <Home />,
  },
  {
    path: "/yoga",
    element: <Yoga />,
  },

  {
    path: "/tracks",
    element: <Tracks />,
  },

  {
    path: "/footer",
    element: <Footer />,
  },
{
                path: '/dashboard',
                element: <Dashboard/>
          
  },
];

export const location = new ReactLocation();
