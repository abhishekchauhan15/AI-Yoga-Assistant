import React from 'react'
import './Styles/Footer.css'
import { GrYoga } from "react-icons/gr";
import { GoMarkGithub} from "react-icons/go";
import {IoLogoTwitter} from "react-icons/io5";
import {IoLogoLinkedin} from "react-icons/io";

export default function Footer() {
  return (
    <div className="footer">
        <h2 className="footer-head">BOOST YOUR FITNESS</h2>
        <hr className="line" color='black'></hr>
        <h1 className="title">YOGA-AI-TRAINER</h1>
        <div className="icons">
        <GrYoga/>
        </div>
      <div className="main-content">
        <div className="container-1">
        <h2 className="f-format">TRACKS WE OFFER</h2>
        <p className="png">
        Beginners Track <br></br>
        Power Yogaa Track <br></br>
        Immunity Booster Track <br></br>
        Yoga in Pregnancy Track <br></br>
        Cardiovascular Yoga Track <br></br>
        Yoga for Migraine Track <br></br>
        Yoga for Asthma Track
        </p>
        </div>

        <div className="container-2">
          <h2 className="l-format">ASANS SUPPORTED</h2>
          <div className="languages">
          <div className="language-1">
            <p>
            Vrksana Asana <br></br>
            Adho Mukha Asana <br></br>
            Balasana <br></br>
            Tad Asana <br></br>
            Trikon Asana <br></br>
            Virbhadra Asana 
           
          </p>
          </div>
        </div>
        </div>
      </div>
      <div className="icon-2">
      <a target="_blank" className="github" href="https://github.com/Kanika637/language-translator"><GoMarkGithub/> </a>
      <a target="_blank" className="linkedin" href="https://www.linkedin.com/in/kanika-gola-999968204/"> <IoLogoLinkedin/> </a>
      {/* <a className="mail" href="https://mail.google.com/mail/u/?authuser=jaideep2912@gmail.com" ><IoMail/> </a> */}
      <a target="_blank" className="twitter" href="https://twitter.com/jai_solania_29"><IoLogoTwitter/> </a>
      </div>
      </div>
  )
}
