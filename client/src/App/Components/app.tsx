import * as React from 'react';
import { Route, Switch } from 'react-router-dom';
import { Router } from 'react-router';
import { createBrowserHistory } from 'history';
import paraPhraserContainer from '../../ParaPhraser/Container/paraPhraserContainer';
import '../../Design/index.css';

const history = createBrowserHistory();

export interface Props {
}

export default class App extends React.Component<Props, {}> {
    constructor(props: Props) {
        super(props);
    }
    render() {
 
    var RoutingApp = (
    <div className="container-fluid">
      <Router history={history}>
        <div>
          <Switch>
            <Route path="/" component={paraPhraserContainer} />
          </Switch>
        </div>
      </Router>
    </div>);
    return RoutingApp;
}
}