import React, { useEffect } from "react";
import EventCard from "../common/EventCard/EventCard";
import classes from "./MainEvents.module.css";
// import SwupOverlayTheme from "@swup/overlay-theme";
// import Swup from "swup";
import { eventsData } from "../../assets/eventsData";
import ReactGA from "react-ga";

const MainEvents = () => {
  // const swup = new Swup({
  //   plugins: [
  //     new SwupOverlayTheme({
  //       color: "#2D2E82",
  //       duration: 600,
  //       direction: "to-right",
  //     }),
  //   ],
  // });
  useEffect(() => {
    ReactGA.pageview(window.location.pathname);
  });

  const newEventsData = eventsData;
   newEventsData.sort((a, b) => a.id - b.id);

  return (
    <>
      <div className={classes.events_section}>
        <h1 className={classes.heading}>Events</h1>
        <img src="x" alt="" />
        <div className={classes.events_container}>
          {newEventsData.map((eventData, i) => {
            return <EventCard eventData={eventData} key={i} />;
          })}
        </div>
      </div>
    </>
  );
};

export default MainEvents;
