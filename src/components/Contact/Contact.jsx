import Faq from "../Faq/Faq";
import classes from "./Contact.module.css";

const Contact = () => {
  return (
    <section id="contact" className={classes.contact}>
      <div className={classes.contactBox}>
        <div className={classes.contentBox}>
          <Faq />
           <div className={classes.persons}>
            <div className={classes.personBox}>
              <h3 className={classes.personHeading}>Rudransh Joshi </h3>
              <div className={classes.details}>
                <p>
                  Event Head <br></br>Antariksha 2K25
                </p>
                <a className={classes.anchor} href="tel:+918630822921">
                  +91 8630822921
                </a>
              </div>
            </div>
            <div className={classes.personBox}>
              <h3 className={classes.personHeading}>Uttam Tiwari</h3>
              <div className={classes.details}>
                <p>
                Event Head<br></br>Antariksha 2K25
                </p>
                <a className={classes.anchor} href="tel:+919548826516">
                  +91 9548826516
                </a>
              </div>
            </div>
          </div> 

          
        </div>
      </div>
    </section>
  );
};

export default Contact;
