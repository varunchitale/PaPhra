import * as constants from '../Actions/paraPhraserActions';
import { call, put } from 'redux-saga/effects';
import ExternalApi from '../../Utils/externalApi';
import { paraPhraseAction } from '../Actions/paraPhraserActions';

export function* paraPhrase(actions: paraPhraseAction) {
    try {
        var apiParameters = {
            url: '/chat',
            method: 'POST',
            parameters: { 'chat': actions.payload }
        };
        let response = yield call(ExternalApi.Api, apiParameters);
        yield put({ type: constants.PARAPHRASE_SUCCESS, payload: response.data });

    } catch (e) {
        yield put({ type: constants.PARAPHRASE_FAILURE, payload: '' });
    }
}