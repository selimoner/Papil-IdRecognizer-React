import React from "react";
import "../Styles/IdProcessor.css"

const CroppedImage = (props) => {

    const croppedImageURL = props.croppedImageURL
    const selectedKey = props.selectedKey

    return (
        <div>
            {croppedImageURL && (
                <div>
                    <h3>{selectedKey === null ? "Cropped Image:" : `${selectedKey} Cropped:`}</h3>
                    <img src={croppedImageURL} alt="Cropped" />
                </div>
            )}
        </div>
    )
}

export default CroppedImage