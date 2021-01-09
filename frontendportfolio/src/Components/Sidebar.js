import React,{useState,useEffect} from 'react'

import { createPopper } from '@popperjs/core';



function Sidebar(){
    const popcorn = document.querySelector('#popcorn');
    const tooltip = document.querySelector('#tooltip');

    createPopper(popcorn, tooltip, {
        placement: 'left',
    });

    let idUl
    const size = useWindowSize();
    if (size.width <= 575){
        idUl = 'idUlUno' 
    }
    else{
        idUl = 'idUlDos'
    }

    return(
        <div className='nav flex-column col-1 wrapper'>
            <ul id={idUl} className='fixed-top'>
                <li className='list-unstyled'>
                    <a href='./home' id='override-btn-outline-success' className='btn btn-outline-success' data-toggle="tooltip" data-placement="left" title="Tooltip on right">
                        <span className="material-icons">home</span>
                    </a>
                </li>
                <li className='list-unstyled mt-3'>
                    <a href='./tech' id='override-btn-outline-success' className='btn btn-outline-success '>
                        <span className="material-icons">code</span>
                    </a>
                </li>
                <li className='list-unstyled mt-3'>
                    <a href='./creative' id='override-btn-outline-success' className='btn btn-outline-success '>
                        <span className="material-icons">history_edu</span>
                    </a>
                </li>
                <li className='list-unstyled mt-3'>
                    <a href='./certification' id='override-btn-outline-success' className='btn btn-outline-success '>
                        <span className="material-icons">fact_check</span>
                    </a>
                </li>

            </ul>
        </div>
    )
}

export default Sidebar

function useWindowSize() {
    const [windowSize, setWindowSize] = useState({
        width: undefined,
        height: undefined,
    });

    useEffect(() => {
        // Handler to call on window resize
        function handleResize() {
            // Set window width/height to state
            setWindowSize({
                width: window.innerWidth,
                height: window.innerHeight,
            });
        }

        // Add event listener
        window.addEventListener("resize", handleResize);

        // Call handler right away so state gets updated with initial window size
        handleResize();

        // Remove event listener on cleanup
        return () => window.removeEventListener("resize", handleResize);
    }, []);

    return windowSize;
    }