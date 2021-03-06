import React from 'react'
import '../Styles/Tracks.css'
import Track from '../images/track.png'
import { Link } from 'react-location'

export default function Tracks() {
  return (
      <div className='track'>
          <h1 className='head'>Select What You Need !</h1>

          <div className='mid'>
          <div className='pic'>
          <img className="cover" src={Track} alt="Track"/>
          </div>
          <div className='button'>
              <Link to= "/yoga"><button className='bgnr'>Beginners Track</button><br></br></Link>
              <Link to= "/yoga"><button className='power'>Power Yogaa Track</button><br></br></Link>
              <Link to= "/yoga"><button className='power'>Immunity Booster Track</button><br></br></Link>
              <Link to= "/yoga"><button className='power'>Yoga in Pregnancy Track</button><br></br></Link>
              <Link to= "/yoga"><button className='power'>Cardiovascular Yoga Track</button><br></br></Link>
              <Link to= "/yoga"><button className='power'>Yoga for Migraine Track</button><br></br></Link>
              <Link to= "/yoga"><button className='power'>Yoga for Asthma Track</button></Link>
          </div>
          </div>
      </div>
  )
}
