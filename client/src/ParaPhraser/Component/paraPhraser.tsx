import * as React from 'react';

export interface Props {

}

export interface State {

}

export default class ParaPhraser extends React.Component<Props, State> {
    constructor(props: Props) {
        super(props);
    }
    render() {
        return (
            <>
                <div className="row">
                    <div className="col-md-12">
                        I am Para Phraser
                    </div>
                </div>
                <div className="row">
                    <div className="col-md-6">
                        <div className="row">
                            <div className="col-md-12">
                                <input type="text" className="form-control" />
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-md-12">
                                <br />
                                <button className="btn btn-success" >Upload</button>
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