import React from 'react'
import './Styles/Yoga.css'
import { FaPlayCircle } from "react-icons/fa";
import Vrksana from './Styles/Images2/vrksana.jpg'
import Adho from './Styles/Images2/adho-mukha.png'
import Balasana from './Styles/Images2/balasana.jpg'
import Tadasan from './Styles/Images2/tad-asan.jpg'
import Trikon from './Styles/Images2/trikonasana.jpg'
import Virbhadra from './Styles/Images2/virabhadrasana.jpg'
import PracticeR from './Styles/Images2/Yoga practice right.png'
import PracticeL from './Styles/Images2/Yoga practice left.png'


function Yoga() {
  return (
    <div className='yoga'>
      <div className='menu'>
                <h5 className='home'>Home</h5>
                <h5 className='about'>About</h5>
                <h5 className='contact'>Contact</h5>
            </div>
      
    <img className="gifR" src={PracticeR} alt="PracticeR"/>
      <div className='group-1'>
        <div className='card-1'>
         <img className="asan-1" src={Vrksana} alt="Vrksana"/>
         <h2 className='asan-name-1'>Vrksana Asana</h2>
         <p className='asan-para-1'>A classic standing posture, It establishes strength and balance, and helps you feel centered.</p>
         <p className="btn"><FaPlayCircle/></p>
        </div>
        <div className='card-2'>
         <img className="asan-1" src={Adho} alt="Adho Mukha"/>
         <h2 className='asan-name-1'>Adho Mukha Asana</h2>
         <p className='asan-para-1'>It strengthens the core and improves circulation, while providing full-body stretch.</p>
         <p className="btn"><FaPlayCircle/></p>
        </div>
        <div className='card-3'>
         <img className="asan-1" src={Balasana} alt="Balasana"/>
         <h2 className='asan-name-1'>Balasana</h2>
         <p className='asan-para-1'>Balasana is a restful pose that can be sequenced between more challenging asanas.</p>
         <p className="btn"><FaPlayCircle/></p>
        </div>
    </div>


    <div className='group-2'>
        <div className='card-4'>
         <img className="asan-1" src={Tadasan} alt="Tad Asana"/>
         <h2 className='asan-name-1'>Tad Asana</h2>
         <p className='asan-para-1'>The foundation of all standing poses, It makes a resting pose, or tool to improve posture.</p>
         <p className="btn"><FaPlayCircle/></p>
        </div>
        <div className='card-5'>
         <img className="asan-1" src={Trikon} alt="Trikon Asana"/>
         <h2 className='asan-name-1'>Trikon Asana</h2>
         <p className='asan-para-1'>It is a quintessential standing pose that stretches and strengthens the whole body.</p>
         <p className="btn"><FaPlayCircle/></p>
        </div>
        <div className='card-6'>
         <img className="asan-1" src={Virbhadra} alt="Virbhadra Asana"/>
         <h2 className='asan-name-1'>Virbhadra Asana</h2>
         <p className='asan-para-1'>It is a foundational yoga pose that balances flexibility and strength in true warrior fashion.</p>
         <p className="btn"><FaPlayCircle/></p>
        </div>
    </div>
    <img className="gifL" src={PracticeL} alt="Practice"/>
    {/* <img className="gifR" src={PracticeR} alt="PracticeR"/> */}


    </div>
  )
}

export default Yoga