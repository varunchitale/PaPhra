import axios from 'axios';
import { getConfig } from './token';
export default class ExternalApi {
    public static Api(parameters: any) {
        let ROOTURL = 'http://13.127.162.123:5656';
        switch (parameters.method) {
            case 'GET': {
                return axios.get(ROOTURL + parameters.url, getConfig());
            }
            case 'POST': {
                return axios.post(ROOTURL + parameters.url, parameters.parameters, getConfig());
            }
            case 'DELETE': {
                return axios.delete(ROOTURL + parameters.url, { data: parameters.parameters });
            }
            case 'PUT': {
                return axios.put(ROOTURL + parameters.url, parameters.parameters, getConfig());
            }
            default: {
                return;
            }
        }
    }
}
