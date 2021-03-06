import React, { PropTypes } from 'react';
import { Router, Route, IndexRoute } from 'react-router';
import { createAction } from 'redux-actions';

import { Global } from '../config/global';

import App from '../modules/app/index.jsx';
import List from '../modules/list';

const Routes = ({ history, store }) => {

  return <Router history={history} >
    <Route path="/"
           component={App}>
      <IndexRoute component={List}/>
    </Route>
  </Router>;
};


Routes.propTypes = {
  history: PropTypes.object.isRequired,
  store: PropTypes.object.isRequired,
};

export default Routes;
