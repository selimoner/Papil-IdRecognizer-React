import React from "react";
import "../Styles/IdProcessor.css"

const FileInput = (props) => {
    const handlePhotoChange = props.handlePhotoChange
    const fileInputRef = props.fileInputRef
    const isPhotoUploaded = props.isPhotoUploaded
    const handleClearClick = props.handleClearClick
    const currentPhoto = props.currentPhoto

    return (
        <div className="col-sm" id="left-side">
            <input
                type="file"
                accept=".png, .jpeg, .jpg"
                onChange={handlePhotoChange}
                ref={fileInputRef}
                disabled={isPhotoUploaded}
            />
            {currentPhoto && (
                <div className="uploaded-photo">

                    <button className="btn btn-danger" onClick={handleClearClick}>
                        Clear
                    </button>
                    <br /><br />
                </div>
            )}
        </div>
    )
}

export default FileInput