import React, { useState } from "react";
import "../Styles/IdProcessor.css"

const Buttons = (props) => {

    const selectedKey = props.selectedKey
    const handleButtonClick = props.handleButtonClick
    const handleCrop = props.handleCrop
    const handleSetCropped = props.handleSetCropped
    const isCropped = props.isCropped
    const goBack = props.goBack
    const [isCroppedClicked, setIsClicked] = useState(false);
    const clearCanvas = props.clearCanvas
    const getRef = props.getRef;
    const isSetCropped = props.isSetCropped
    const isInfoSaved = props.isInfoSaved

    function isClicked() {
        setIsClicked(true);
    }

    return (
        <div id="buttonsDiv">
            &nbsp;&nbsp;
            <div id="processDiv">
                {selectedKey && (
                    <button className="btn btn-primary mt-1" onClick={handleButtonClick}>
                        Get Card Coordinates
                    </button>
                )}&nbsp;&nbsp;
                <button className="btn btn-warning mt-1" onClick={() => {
                    handleCrop();
                    isClicked();
                }}>
                    Crop Photo
                </button>
                &nbsp;&nbsp;
                {isCropped && isCroppedClicked && (
                    <button className="btn btn-info mt-1" onClick={handleSetCropped}>
                        Set Cropped Photo
                    </button>
                )}
                &nbsp;&nbsp;
                <button className="btn btn-danger mt-1" onClick={goBack}>Restore</button>
                &nbsp;&nbsp;
                <button onClick={clearCanvas} className="btn mt-1" style={{ background: "yellow" }}>Reset Canvas</button>
                &nbsp;&nbsp;
                {isSetCropped && isInfoSaved && (
                    <button onClick={getRef} className="btn btn-primary mt-1">Get Ref</button>
                )}

            </div>
        </div>
    )
}

export default Buttons