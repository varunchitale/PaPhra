import * as React from 'react';

export interface Props {
    data: string;
    isDataRecieved: boolean;
    getParaPhrased: (input: string) => void;
}

export interface State {
    clicked: boolean;
    input: string;
}

export default class ParaPhraser extends React.Component<Props, State> {
    constructor(props: Props) {
        super(props);
        this.state = {
            clicked: false,
            input: ''
        };
    }
    handleUpload() {
        this.setState({ clicked: true });
        this.props.getParaPhrased(this.state.input);
    }
    componentWillReceiveProps(nextProps: Props) {
        if (nextProps.isDataRecieved) {
            this.setState({ clicked: false });
        }
    }
    render() {
        var Loader = (
            <span className="loading">Fetching</span>
        );
        return (
            <>
                <div className="row">
                    <div className="col-md-6">
                        <div className="row">
                            <div className="col-md-12">
                                <textarea defaultValue={'Enter the data here'} className="form-control" onChange={(e) => { this.setState({ input: e.currentTarget.value }); }} />
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-md-12">
                                <br />
                                <button className="btn btn-success" onClick={() => this.handleUpload()}>{this.state.clicked ? Loader : 'Upload'}</button>
                            </div>
                        </div>
                    </div>
                    <div className="col-md-6">
                        I am Para Phraser output
                    </div>
                </div>
            </>
        );
    }
}