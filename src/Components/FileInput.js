import React from "react";
import "../Styles/IdProcessor.css"

const FileInput = (props) => {
    const handlePhotoChange = props.handlePhotoChange
    const fileInputRef = props.fileInputRef
    const isPhotoUploaded = props.isPhotoUploaded
    const handleClearClick = props.handleClearClick
    const currentPhoto = props.currentPhoto
    const noCropping = props.noCropping
    const checker = props.checker
    const isNoCropClicked = props.isNoCropClicked

    return (
        <div className="col-sm" id="left-side">
            <label for="images" class="drop-container" id="dropcontainer">
                <span class="drop-title">Drop files here</span>
                or
                <input type="file" id="images" required accept=".png, .jpeg, .jpg"
                    onChange={handlePhotoChange}
                    ref={fileInputRef}
                    disabled={isPhotoUploaded} />
            </label>
            {currentPhoto && (
                <div className="uploaded-photo">
                    <button className="btn btn-danger mt-1" onClick={handleClearClick}>
                        Clear
                    </button>
                    &nbsp;&nbsp;
                    {!checker && !isNoCropClicked && (
                        <button className="btn btn-success mt-1" onClick={noCropping}>No Need Crop</button>
                    )}

                    <br />
                </div>
            )}
        </div>
    )
}

export default FileInput