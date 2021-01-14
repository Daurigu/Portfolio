import React, {useState, useEffect} from 'react'

//Third-Party
import axios from 'axios'

//Components
import Card from '../Components/card'
import Sections from '../Components/Sections'

function Tech(){

  const [cards, setCard] = useState(null)
  const [sections, setSection] = useState(null)
  
  const urlCreative = 'http://127.0.0.1:8000/api/tech/card'
  const urlCreativeSect = 'http://127.0.0.1:8000/api/tech/section'
  
  let outputRender = []
  let loading = <div class="spinner-border text-success m-5" role="status"><span class="visually-hidden">Loading...</span></div>

  //API CALLS
  useEffect( ()=> {
    axios.get(urlCreative).then(response => {
      setCard(response.data)
    })
    axios.get(urlCreativeSect).then(response => {
      setSection(response.data)
    })
  }, [] )

  // MERGE SECTIONS WITH CARDS
  if(sections){
    sections.map(element => {
      outputRender.push(<Sections section={element.section} description={element.description}/>)
      if(cards){
        cards.map( card => {
          if (card.section === element.id){
            return outputRender.push(<Card image={card.image} name = {card.name} description={card.description} link={card.link} type='1'/>)
          }
          return 0
        })
      }
    return outputRender
    })
  }

  return(
      <div className='row justify-content-md-center'>
          {outputRender === [] ? loading : outputRender}
      </div>
  )
}

export default Tech