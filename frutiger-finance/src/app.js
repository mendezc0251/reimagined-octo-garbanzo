import React from 'react';
import ReactDOM from 'react-dom';
import "./styles.css"
function WelcomeButton(){
    return(
        <button className='styles.welbutton'>Welcome to Frutiger Finance!</button>
    )
}
export default function MyApp(){
    return(
        <div>
            <WelcomeButton/>
        </div>
    )
}