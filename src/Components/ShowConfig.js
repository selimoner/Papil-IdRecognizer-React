import React from "react";
import "../Styles/IdProcessor.css"

const ShowConfig = (props) => {
    const isShowConfig = props.isShowConfig
    const config = props.config

    return (
        <div className="col-md-6 mb-4">
            <div>
                <div className="coordinates-section">
                    <h3>Config : </h3>
                    <pre>{JSON.stringify(config, null, 2)}</pre>
                </div>

            </div>
        </div>
    )
}

export default ShowConfig;