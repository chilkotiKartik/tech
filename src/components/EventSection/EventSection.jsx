import React from "react";
import classes from "./EventSection.module.css";
import Button from "../common/Button/Button";
import event from "./event.svg";

const EventSection = () => {
  return (
    <>
      <section id="about" className={classes.aboutSec}>
        <div className={classes.about}>
          <div className={classes.details}>
            {/* <h3 className={classes.heading}>About</h3> */}
            <h2 className={classes.heading1}>EVENTS</h2>
            <p className={classes.para}>
              SAMBHAV reflects the spirit of the festival and its mission to
              provide a platform for individuals to push their limits and
              challenge themselves to turn their ideas and innovative projects
              into reality. The festival offers a diverse range of technical
              events and competitions designed to showcase the talents and
              skills of participants while fostering creativity, teamwork, and
              problem-solving abilities. With its focus on technology and
              innovation, Sambhav truly embodies its name and serves as a
              catalyst for making the impossible possible.
            </p>

            {/* <p className={classes.para}>
            Spectacular talent stretches boundaries to inspire the participating
            students and the rapt audience alike. A gigantic range of events
            from advanced robotics challenges to entrepreneurship hunts
            promising to zap up the cranial indices of participants. Skill,
            genius and knowledge trading infused with a handful of fun, and a
            titanic prize money sum of above half a million rupees to make Karma
            one of the most unique tech carnivals of the country.
          </p> */}
            <div className={classes.btn}>
              <Button link="/events" label="Explore" />
            </div>
          </div>

          <div className={classes.composition}>
            <img className={classes.images} src={event} alt="about" />
          </div>
        </div>
      </section>
    </>
  );
};

export default EventSection;
