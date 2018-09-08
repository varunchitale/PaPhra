export const PARAPHRASE = 'PARAPHRASE';
export type PARAPHRASE = typeof PARAPHRASE;
export const PARAPHRASE_SUCCESS = 'PARAPHRASE_SUCCESS';
export type PARAPHRASE_SUCCESS = typeof PARAPHRASE_SUCCESS;
export const PARAPHRASE_FAILURE = 'PARAPHRASE_FAILURE';
export type PARAPHRASE_FAILURE = typeof PARAPHRASE_FAILURE;

export interface ParaPhrase {
    type: PARAPHRASE;
    payload: string;
}

export type paraPhraseAction = ParaPhrase;

export default class ParaPhraserActions {
    public static paraPhrase(input: string): ParaPhrase {
        return {
            type: PARAPHRASE,
            payload: input
        };
    }
}