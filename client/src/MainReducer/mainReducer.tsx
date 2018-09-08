import { combineReducers } from 'redux';
import paraPhrasereducer from '../ParaPhraser/Reducer/paraPhraseReducer';

export const mainReducer = combineReducers({
  ParaPhrase: paraPhrasereducer
});