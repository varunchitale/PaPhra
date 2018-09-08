import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import  createSagaMiddleware  from 'redux-saga';
import { mainReducer } from './MainReducer/mainReducer';
import App from './App/Container/app';
import paraPhraseRootSaga from './ParaPhraser/Saga/paraPhraseRootSaga';

const sagaMiddleware = createSagaMiddleware();
const store = createStore(mainReducer, applyMiddleware(sagaMiddleware));

sagaMiddleware.run(paraPhraseRootSaga);

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root') as HTMLElement
);
