import React from 'react';
import ReactDOM from 'react-dom';

import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import UserEvents from './components/UserEvents'

const Routes = (
  <BrowserRouter>
    <Switch>
      <Route exact path='/' component={Home} />
      <Route path='/user/:username' component={UserEvents} />
    </Switch>
  </BrowserRouter>
)

ReactDOM.render(Routes, document.getElementById("content"))
