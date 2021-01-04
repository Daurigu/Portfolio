import React , {useState, useEffect} from 'react'
import axios from 'axios'

//Components
import Card from './Components/card'

function App() {

  const [cards, setCard] = useState(null)

  const url = 'http://127.0.0.1:8000/api/creative/card/'
  let content = null

  useEffect( ()=> {
    axios.get(url).then(response => {
      setCard(response.data)
    })
  }, [] )

  if(cards){
    content = 
    cards.map( card => (
      <Card image={card.image} name = {card.name} description={card.description} link={card.link}/>
    ))
  }

  //var informacion = cards.toString() != null ? cards.toString() : 'Nada loko'

  return (
    <div className="App">
        <h1>Hello Mundo</h1>
        {content}
    </div>
  );
}

export default App
