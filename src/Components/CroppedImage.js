import React from "react";
import "../Styles/IdProcessor.css"

const CroppedImage = (props) => {

    const croppedImageURL = props.croppedImageURL

    return (
        <div>
            {croppedImageURL && (
                <div>
                    <h3>Cropped Image:</h3>
                    <img src={croppedImageURL} alt="Cropped" />
                </div>
            )}
        </div>
    )
}

export default CroppedImage