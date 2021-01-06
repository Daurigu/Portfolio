import React from 'react'

function Card(props){
    return(
        <div className="card border-0 m-3 shadow-lg container-sm col-11 col-sm-5  col-lg-3">
            <img src={props.image} className='card-img-top mt-2 rounded-3' alt=""/>
            <div className="row card-body">
                <h3 className='text-success'>{props.name}</h3>
                <p>{props.description}</p>
                <a href={props.link} className='btn btn-outline-success'>View</a>
            </div>
        </div>
    )
}

export default Card
