import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import UserEvents from './components/UserEvents'

const Routes = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route path='/' component={Home} />
        <Route path='/users/:id' component={UserEvents} />
      </Switch>
    </BrowserRouter>
  )
}

export default Routes;
