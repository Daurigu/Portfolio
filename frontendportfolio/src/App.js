import React from 'react'

//Views
import Creative from './Views/Creative'
import Tech from './Views/Tech'
import Sidebar from './Components/Sidebar'


function App() {
  return (
    <div className="App container">
      <Sidebar />
      <Creative />
      <Tech />
    </div>
  );
}

export default App
