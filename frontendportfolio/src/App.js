import React from 'react'

//Components
import Card from './Components/card'

function App() {
  return (
    <div className="App">
        <h1>Hello Mundo</h1>
        <Card image='https://i.vimeocdn.com/video/640225764_590x332.jpg' name ='My Cuscus' description='This is a documentary where we wanted to share the reality of women in Panama who have to suffer because of their "Cuscus" hair.' link='https://vimeo.com/221838129'/>
    </div>
  );
}

export default App
