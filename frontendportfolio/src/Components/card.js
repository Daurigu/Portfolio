import React from 'react'

function Card(props){
    
    let typeImg, typePlacement, actButton, clickRedirect

    if (props.type==='1'){
        typeImg = "card-body d-flex flex-column"
        typePlacement = 'card-img-top mt-2 rounded-3'
        actButton = <a id='override-btn-outline-success' href={props.link} className='btn btn-outline-success mt-auto'>View</a>
        clickRedirect = ''
    }
    else{
        typeImg = "row card-img-overlay"
        typePlacement = 'card-img rounded-3 imgBlur mt-3 mb-3'
        actButton = ''
        clickRedirect = () => {
            window.location.href = props.link
        }
    }
    
    return(
        <div className="card border-0 m-3 shadow-lg container-sm col-11 col-sm-5 col-lg-3">
            <img src={props.image} className={typePlacement} alt=""/>
            <div onClick={clickRedirect} class='imgContainer card-body d-flex flex-column m-0 p-0 pb-2'>
                <div className={typeImg}>
                    <h3 className='text-success'>{props.name}</h3>
                    <p>{props.description}</p>
                </div>
                {actButton}
            </div>
            
        </div>
    )
}

export default Card
