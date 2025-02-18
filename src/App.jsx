import React, { useEffect, useState } from "react";
import { Route, Routes, useLocation } from "react-router-dom";
// import Button from "./components/common/Button/Button";
import Navbar from "../src/components/Navbar/Navbar";
import Footer from "../src/components/Footer/Footer";
import Hidden from "../src/components/Hidden/Hidden";
import MainEvents from "./components/MainEvents/MainEvents";
// import Faq from "../src/components/Faq/Faq";
import Homepage from "./pages/Homepage";
import SingleEventPage from "./components/SingleEventPage/SingleEventPage";
import Leaderboard from "./pages/Leaderboard";
import AboutPage from "./pages/AboutPage";
import Register from "./components/common/Register/Register";
import ContactUs from "./components/ContactUs/ContactUs";
import Loading from "./components/common/Loading/Loading";
import Popup from "./components/common/Popup/Popup";
// import SwupOverlayTheme from "@swup/overlay-theme";
// import Swup from "swup";
/* Google Analytics */
import ReactGA from "react-ga";
const TRACKING_ID = "UA-257375779-1"; // OUR_TRACKING_ID
ReactGA.initialize(TRACKING_ID);

const App = () => {
  // const swup = new Swup({
  //   plugins: [
  //     new SwupOverlayTheme({
  //       color: "#2D2E82",
  //       duration: 500,
  //       direction: "to-right",
  //     }),
  //   ],
  // });
  const location = useLocation();
  useEffect(() => {
    window.scrollTo(0, 0);
    // console.log(location);
  }, [location]);
  const [loading, setLoading] = useState(true);

  setTimeout(() => setLoading(false), 3900);
  useEffect(() => {});
  return (
    <>
      {loading ? (
        <Loading />
      ) : (
        <>
          {/* <div
        // id={swup}
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          width: "100vw",
          height: "auto",
        }}
      > */}
          <Popup />
          <Navbar />
          <Routes>
            <Route path="/" element={<Homepage />} />
            <Route path="/events" element={<MainEvents />} />
            <Route path="/events/:eventId" element={<SingleEventPage />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/about" element={<AboutPage />} />
            <Route path="/register" element={<Register />} />
            <Route path="/contact" element={<ContactUs />} />
            <Route path="/hidden" element={<Hidden/>} />
            {/*   <Route path="/leaderboard/:eventId" element={<Leaderboard />} />
          <Route path="*" element={<NotFound />}></Route> */}
            {/* <Route path="/" element={<Landing />}></Route>  */}
            {/* <Route path="/" element={<Faq />}></Route>  */}
          </Routes>
          <Footer />
          {/* <Button /> */}
          {/* </div> */}
        </>
      )}
    </>
  );
};

export default App;
