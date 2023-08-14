import React from "react";
import "../Styles/IdProcessor.css"

const Buttons = (props) => {

    const selectedKey = props.selectedKey
    const handleButtonClick = props.handleButtonClick
    const handleCrop = props.handleCrop
    const handleSetCropped = props.handleSetCropped
    const isCropped = props.isCropped

    return (
        <div id="buttonsDiv">
            {selectedKey && (
                <button className="btn btn-primary mt-3" onClick={handleButtonClick}>
                    Get Card Coordinates
                </button>
            )}&nbsp;&nbsp;
            <button className="btn btn-warning mt-3" onClick={handleCrop}>
                Crop Photo
            </button>
            &nbsp;&nbsp;
            {isCropped && (
                <button className="btn btn-info mt-3" onClick={handleSetCropped}>
                    Set Cropped Photo
                </button>
            )}
            &nbsp;&nbsp;
            <button className="btn btn-success mt-3">
                Get JSON info
            </button>
        </div>
    )
}

export default Buttons