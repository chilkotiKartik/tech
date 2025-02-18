import React from 'react'
import { useNavigate } from 'react-router-dom'
import classes from "./ContactUs.module.css"
import Button from "../common/Button/Button"

const ContactUs = () => {
  const navigate = useNavigate();

  const handleSendClick = () => {
    // Add any form validation or submission logic here if needed
    navigate('/events');
  }

  return (
    <>
      <div className={classes.background}>
        {/* <div className={classes.registerForm}> */}
        <div className={classes.card}>
          <div className={classes.card2}>
              <h1 className={classes.heading}>Contact Us</h1>
              <div className={classes.userData}>
                <div className={classes.input_container}>
                  <label className={classes.input_label}>
                    Name<span className={classes.mandatory}>*</span>
                  </label>
                  <input className={classes.input}/>
                </div>
                <div className={classes.input_container}>
                  <label className={classes.input_label}>
                    Email<span className={classes.mandatory}>*</span>
                  </label>
                  <input className={classes.input}/>
                </div>
                <div className={classes.input_container}>
                  <label className={classes.input_label}>
                    Message<span className={classes.mandatory}>*</span>
                  </label>
                  <textarea className={classes.message}>Please Talk To Coordinator </textarea>
                </div>
              </div>
              <div className={classes.button}>
                <Button label="Send" onClick={"('/events')"} />
              </div>
            </div>
        </div>
        {/* </div> */}
      </div>
    </>
  )
}

export default ContactUs