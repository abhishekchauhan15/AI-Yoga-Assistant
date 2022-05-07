import React from 'react'
import './Styles/Home.css'
import { FaPlayCircle } from "react-icons/fa";
import { FiArrowDown } from "react-icons/fi";
import Yoga from './Styles/Images2/Yoga.png'

function Home() {
  return (
    <div className='h-page'>
        <div className='content'>
            <div className='menu'>
                <h5 className='home'>Home</h5>
                <h5 className='about'>About</h5>
                <h5 className='contact'>Contact</h5>
                <button className='in'>Sign In</button>
                <button className='up'>Sign Up</button>
            </div>
            <div className='middle'>
                <div className='title'>
                    <h1 className='name-1'>Your Personal AI Yoga Trainer</h1>
                    <p className='intro'>Appointing personal AI yoga trainer at home to keep you fit and healthy. We provide Personal AI Yoga Trainer theme with appointments booking system.</p>
                    <button className='go'><p className="let">Let's Start</p></button>
                    <div className='icon'>
                        <p className="play"><FaPlayCircle/></p><p className="para">Ashtanga Yoga</p>
                        <p className="play-2"><FaPlayCircle/></p><p className="para-2">Hatha Yoga</p>
                        <p className='scroll'>SCROLL DOWN</p><p className="a-icon"><FiArrowDown/></p>
                    </div>
                </div>
                <img className="img-1" src={Yoga} alt="Yoga"/>
            </div>
        </div>
    </div>
  )
}

export default Home