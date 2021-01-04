import React from 'react'

function Card(props){
    return(
        <div className="card container-sm">
            <img src={props.image} className='card-img-top mt-2' alt=""/>
            <div className="row card-body">
                <h3>{props.name}</h3>
                <p>{props.description}</p>
                <a href={props.link} className='btn btn-outline-success'>View</a>
            </div>
        </div>
    )
}

export default Card
