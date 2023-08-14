import React from "react";
import "../Styles/IdProcessor.css"

const ShowCoordinates = (props) => {

    const showCoordinates = props.showCoordinates
    const cardCoordinates = props.cardCoordinates

    return (
        <div className="col-md-6 mb-4">
            <div>
                {showCoordinates && (
                    <div className="coordinates-section">
                        <h3>Card Coordinates:</h3>
                        <pre>{JSON.stringify(cardCoordinates, null, 2)}</pre>
                    </div>
                )}
            </div>
        </div>
    )
}

export default ShowCoordinates