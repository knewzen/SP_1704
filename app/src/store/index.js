import { createStore, combineReducers } from 'redux'
import application from '../application/reducer';
import infrastructure from '../infrastructure/reducer';

const store = createStore(combineReducers({
  application,
  infrastructure,
}));

export default store;