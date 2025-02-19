import { useState } from "react";
import classes from "./Faq.module.css";

const questions = [
  {
    question: "What is Antariksha 2K25?",
    answer:
      "Antariksha 2k25 is the one of biggest Technical event in the history of Akit.",
  },
  {
    question: "What are the Dates and Timings of event?",
    answer:
      "The event will start From 24-25 Feb",
  },
  {
    question: "How can I participate in the event?",
    answer:
      "Explore various events on the Antariksha website and register for the same",
  },
  {
    question: "Is there any entry fee for Antariksha 2k25?",
    answer:
      "No, there is not any entry fee to Take Part in Antariksha 2k25 .",
  },
];

const Faq = () => {
  const [clicked, setClicked] = useState(null);

  const toggle = (i) => {
    if (clicked === i) {
      return setClicked(null);
    }

    setClicked(i);
  };

  return (
    <section className={classes.faqSection}>
      <div className={classes.heading}>FAQ</div>
      <div className={classes.faq}>
        {questions.map((ques, i) => {
          return (
            <div className={classes.single} onClick={() => toggle(i)}>
              <div className={classes.question}>{ques.question}</div>
              <div
                className={`${
                  clicked === i ? classes.answer : classes.noAnswer
                }`}
              >
                {ques.answer}
              </div>
              <span className={classes.btn}>+</span>
            </div>
          );
        })}

        {/* <div className={classes.single}>
                <div className={classes.question}>How are you?</div>
                <div className={classes.answer}>I am fine</div>
                <span className={classes.btn}>+</span>
            </div> */}
      </div>
    </section>
  );
};

export default Faq;
