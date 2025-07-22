import React from 'react';
import '../css/hexagon-comp.css';

class Competition extends React.Component {
    render() {
        return(
            <div className="competition">
                <ul id="hexGrid" className="clr">

                    <li className="hex">
                        <div className="hexIn">
                            <img src={require('../assets/edm.jpg')} alt="pubg"/>   
                            <h1>SUNBURN Campus</h1>
                            <a href="/edm">GO!</a>
                        </div> 
                    </li>

                    <li className="hex">
                        <div className="hexIn">
                            <img src={require('../assets/streetfair3.jpeg')} alt="pubg"/>   
                            <h1>Carnival</h1>
                            <a href="/mela">GO!</a>
                        </div> 
                    </li>

                    <li className="hex">
                        <div className="hexIn">
                            <img src={require('../assets/stageplay2.jpeg')} alt="pubg"/>   
                            <h1>Curtain Call</h1>
                            <a href="/stage">GO!</a>
                        </div> 
                    </li>

                    <li className="hex">
                        <div className="hexIn">
                            <img src={require('../assets/pubg2.jpg')} alt="pubg"/>   
                            <h1>LAN Gaming</h1>
                            <a href="/lan">GO!</a>
                        </div> 
                    </li>

                    <li className="hex">
                        <div className="hexIn">
                            <img src={require("../assets/solosinging2.jpg")} alt="Solo-singing"/>   
                            <h1>Solo-Singing</h1> 
                            <a href="/Singing">GO!</a>                            
                        </div> 
                    </li>

                    <li className="hex">
                        <div className="hexIn">
                            <img src={require('../assets/bands2.jpg')} alt="Band"/>   
                            <h1>Battle of Bands</h1> 
                            <a href="/overtone">GO!</a>
                        </div> 
                    </li>
                    
                    <li className="hex">
                        <div className="hexIn">
                            <img src={require("../assets/FacePaint.jpg")} alt="face"/>   
                            <h1>Painting</h1> 
                            <a href="/facepainting">GO!</a>
                        </div> 
                    </li>

                    <li className="hex">
                        <div className="hexIn">
                            <img src={require("../assets/dance2.jpg")} alt="Dancing"/>   
                            <h1>Group Dance</h1> 
                            <a href="/groupdance">GO!</a>
                        </div> 
                    </li>

                    <li className="hex">
                        <div className="hexIn">
                            <img src={require("../assets/fanatics.jpg")} alt="BOF"/>      
                            <h1>League of Fanatics</h1> 
                            <a href="/lof">GO!</a>
                        </div> 
                    </li>

                    <li className="hex">
                        <div className="hexIn">
                            <img src={require("../assets/fashion.jpg")} alt="fashion"/>
                            <h1>Fashion Show</h1> 
                            <a href="/fashion">GO!</a>
                        </div> 
                    </li>
                    <li className="hex"></li>
                    
                </ul>
            </div>
        );
    }
}

export default Competition;
