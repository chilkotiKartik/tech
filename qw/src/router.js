import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { createBrowserHistory } from "history";

//Pages
import Home from './components/home';

import GroupDance from './components/sections/GroupDance';
import Euphony from './components/sections/Euphony';
import FacePainting from './components/sections/FacePainting';
import LAN from './components/sections/LANGaming';
import SING from './components/sections/Singing';
import FashionShow from './components/sections/fashion'
import League from './components/sections/League'
import EDM from './components/sections/EDM'
import Stage from './components/sections/Stage'
import Carnival from './components/sections/Carnival'
import Team from './components/sections/MeetTheTeam'

const history = createBrowserHistory();
export default (
    <BrowserRouter>
        <Routes>
            <Route exact path="/" element={<Home />} />
            <Route exact path="/groupdance" element={<GroupDance />} />
            <Route exact path="/overtone" element={<Euphony />} />
            <Route exact path="/facepainting" element={<FacePainting />} />
            <Route exact path="/lan" element={<LAN />} />
            <Route exact path="/singing" element={<SING />} />
            <Route exact path='/fashion' element={<FashionShow />} />
            <Route exact path="/lof" element={<League />} />
            <Route exact path="/edm" element={<EDM />} />
            <Route exact path="/stage" element={<Stage />} />
            <Route exact path="/mela" element={<Carnival />} />
            <Route exact path="/team" element={<Team />} />
        </Routes>
    </BrowserRouter>
)