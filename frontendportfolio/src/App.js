import React from 'react'

//Views
import Creative from './Views/Creative'
import Tech from './Views/Tech'
import Certifications from './Views/Certifications'
import Sidebar from './Components/Sidebar'
import Footer from './Components/footer'

// Third-party
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom'

function App() {
  return (
    <div className="App container">
      <div className="row">
        <Router>
          <Sidebar />
          <Switch>
            <Route exact path='/'>
              
            </Route>
            <Route path='/creative'>
              <div className='col-11'>
                <Creative />
              </div>
            </Route>
            <Route path='/tech'>
              <div className='col-11'>
                <Tech />
              </div>
            </Route>
            <Route path='/certification'>
              <div className='col-11'>
                <Certifications />
              </div>
            </Route>
          </Switch>
        </Router>
      </div>
      <Footer />
    </div>
  );
}

export default App
