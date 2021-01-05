import React from 'react'

function Sections(props){
    return(
        <div>
            <h1>{props.section}</h1>
            <p>{props.description}</p>
        </div>
    )
}

export default Sections