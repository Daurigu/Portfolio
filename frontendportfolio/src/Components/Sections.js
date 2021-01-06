import React from 'react'

function Sections(props){


    return(
        <div className='mt-5'>
            <h1 className='text-success'>{props.section}</h1>
            <p className='text-secondary'>{props.description}</p>
        </div>
    )
}

export default Sections