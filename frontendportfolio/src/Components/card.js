import React from 'react'

function Card(props){
    let typeImg, typePlacement, actButton, overlay, clickRedirect
    if (props.type==='1'){
        typeImg = "row card-body"
        typePlacement = 'card-img-top mt-2 rounded-3'
        actButton = <a id='override-btn-outline-success' href={props.link} className='btn btn-outline-success'>View</a>
        overlay = ''
        clickRedirect = ''
    }
    else{
        typeImg = "row card-img-overlay"
        typePlacement = 'card-img rounded-3 imgBlur mt-3 mb-3'
        actButton = ''
        overlay = 'overlay'
        clickRedirect = () => {
            window.location.href = props.link
        }
    }
    
    return(
        <div className="card border-0 m-3 shadow-lg container-sm col-11 col-sm-5 col-lg-3">
            <img src={props.image} className={typePlacement} alt=""/>
            <div onClick={clickRedirect} id={overlay}>
                <div className={typeImg}>
                    <h3 className='text-success'>{props.name}</h3>
                    <p>{props.description}</p>
                    {actButton}
                </div>
            </div>
            
        </div>
    )
}

export default Card
