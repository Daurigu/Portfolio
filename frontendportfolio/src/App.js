import React from 'react'

// Views
import Creative from './Views/Creative'
import Tech from './Views/Tech'
import Certifications from './Views/Certifications'
import Home from './Views/Home'

// Components
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
      <div className="row App">
        <Router>
          <Sidebar />

          <Switch>
            <Route exact path='/'>
              <Home />
            </Route>

            <Route exact path='/home'>
              <Home />
            </Route>

            <Route path='/creative'>
              <div className='col-11'>
                <Creative />
              </div>
              <Footer />
            </Route>

            <Route path='/tech'>
              <div className='col-11'>
                <Tech />
              </div>
              <Footer />
            </Route>

            <Route path='/certification'>
              <div className='col-11'>
                <Certifications />
              </div>
              <Footer />
            </Route>

          </Switch>

        </Router>
      </div>
    </div>
  );
}

export default App
