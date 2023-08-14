import React from "react";
import "../Styles/IdProcessor.css"

const CroppedImagesDiv = (props) => {

    const selectedKey = props.selectedKey
    const croppedImageURL = props.croppedImageURL
    const cardCoordinates = props.cardCoordinates


    return (
        <div>
            {Object.keys(cardCoordinates).map((key) => (
                selectedKey === key && (
                    <div>
                        <label className="form-check-label">
                            <img src={croppedImageURL} alt="croppedKey" /> {selectedKey}
                        </label>
                    </div>
                )
            ))}
        </div>
    );
}

export default CroppedImagesDiv