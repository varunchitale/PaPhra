import { all, takeLatest } from 'redux-saga/effects';
import * as constants from '../Actions/paraPhraserActions';
import { paraPhrase } from './paraPhraseSaga';

export default function* paraPhraseRootSaga() {
    yield all([
        takeLatest(constants.PARAPHRASE, paraPhrase),
    ]);
}