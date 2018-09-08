import { connect } from 'react-redux';
import ParaPhraser from '../Component/paraPhraser';
import ParaPhraserActions from '../Actions/paraPhraserActions';

export function mapStateToProps(appState: any) {
  return {
    data: appState.ParaPhrase.data as string,
    isDataRecieved: appState.ParaPhrase.isDataRecieved as boolean
  };
}

export function mapDispatchToProps(dispatch: any) {
  return {
    getParaPhrased: (input: string) => dispatch(ParaPhraserActions.paraPhrase(input))
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(ParaPhraser as any);
