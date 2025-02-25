import React from 'react';
import classes from './Sponsor.module.css';
import SponsorImage from '../../assets/sponser.jpg'; // Replace with your sponsor image path

const Sponsor = () => {
  return (
    <div className={classes.sponsorSection}>
      <h2 className={classes.heading}>Our Sponsors</h2>
      <div className={classes.sponsorContent}>
        <img src={SponsorImage} alt="Sponsor" className={classes.sponsorImage} />
        <p className={classes.sponsorText}>
          We are grateful to Riha Band  for their generous support. Their contributions help us to achieve our goals and make our  cultural events successful.
        </p>
      </div>
    </div>
  );
};

export default Sponsor;