import React from "react";
import About from "../components/About/About";
import EventSection from "../components/EventSection/EventSection";
import classes from "./AboutPage.module.css";

const AboutPage = () => {
  return (
    <>
      <div className={classes.about_page}>
      <h1 className={classes.headingx}>About</h1>
        <About />
        <EventSection />
      </div>
    </>
  );
};

export default AboutPage;
