import * as React from 'react';
import './css/App.css';

export interface Props {
    delay: number;
    prompt: string;
}

export default class Snackbar extends React.Component<Props, { show: boolean }> {

    constructor(props: Props) {
        super(props);
        this.state = {
            show: true
        };
        this.hideSnackbar = this.hideSnackbar.bind(this);
    }

    hideSnackbar() {
        this.setState({ show: false });
    }

    render() {

        setTimeout(() => { this.hideSnackbar(); }, this.props.delay);
        return (
            <div className="container-fluid">
                <div className="main" >
                    <div onClick={this.hideSnackbar} className="react-snackbar-container">
                        {this.state.show ?
                            <div className="react-snackbar">
                                {this.props.prompt}
                            </div>
                            : null}
                    </div>
                </div>
            </div>
        );
    }
}