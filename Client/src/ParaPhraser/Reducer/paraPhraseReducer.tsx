import * as constants from '../Actions/paraPhraserActions';
import ParaPhraseState from '../State/paraPhraseState';

export default function paraPhrasereducer(state: ParaPhraseState = { data: '', isDataRecieved: false }, actions: any) {
    switch (actions.type) {
        case constants.PARAPHRASE_FAILURE: {
            return { ...state, data: actions.payload, isDataRecieved: true };
        }
        default: {
            return { ...state };
        }
    }
}