import React from 'react'
import './Styles/Home.css'
// import { FaPlayCircle } from "react-icons/fa";
import Yoga from './Styles/Images2/Yoga.png'

function Home() {
  return (
    <div className='h-page'>
        <div className='content'>
            <div className='menu'>
                <h5 className='home'>Home</h5>
                <h5 className='about'>About</h5>
                <h5 className='contact'>Contact</h5>
                <button className='in'>Sign in</button>
                <button className='up'>Sign up</button>
            </div>
            <div className='middle'>
                <div className='title'>
                    <h1 className='name-1'>Your Personal AI Yoga Trainer</h1>
                    <p className='intro'>Appointing personal AI yoga trainer at home to keep you fit and healthy. We provide Personal AI Yoga Trainer theme with appointments booking system.</p>
                    <button className='go'>Let's Start</button>
                    {/* <div className='icon'>
                    <p className="insta"><FaPlayCircle/></p>
                    </div> */}
                </div>
                <img className="img-1" src={Yoga} alt="Yoga"/>
            </div>
        </div>
    </div>
  )
}

export default Home