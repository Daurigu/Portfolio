import React, {useState, useEffect} from 'react'
import certificate from '../Images/certificate.jpg'

//Third-Party
import axios from 'axios'

//Components
import Card from '../Components/card'

function Certifications(){

    const [card, setCard] = useState(null)
    
    const urlCreative = 'http://127.0.0.1:8000/api/certification/card'
    let showContent = null
    let loading = <div class="spinner-border text-success m-5" role="status"><span class="visually-hidden">Loading...</span></div>

    //API CALLS
    useEffect( ()=> {
      axios.get(urlCreative).then(response => {
        setCard(response.data)
      })
    }, [] )

    if (card){
      showContent = card.map( (card)=>{
         return <Card image={certificate} name={card.name} description={card.description} link={card.link} type='2'/>
      } )
    }

    return(
        <div className="mt-5 pt-5">
          <div className="p-5">
            <h1 className='text-success'>Certifications</h1>
            <p className='text-secondary'>Click any of the certifications to get the full information</p>
          </div>
          <div className="row mt-5 justify-content-md-center">
            {showContent === null ? loading : showContent}
          </div>
          
        </div>
    )
}

export default Certifications