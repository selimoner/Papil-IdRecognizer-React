import React from "react";
import "../Styles/IdProcessor.css"

const CheckboxField = (props) => {

    const cardCoordinates = props.cardCoordinates
    const selectedKey = props.selectedKey
    const handleCheckboxChange = props.handleCheckboxChange
    const addCheckbox = props.addCheckbox

    return (
        <div id="checkBoxDiv">
            {Object.keys(cardCoordinates).map((key) => (
                <div key={key} id="form-check" className="col-md-3 mb-2">
                    <label className="form-check-label">
                        <input
                            type="checkbox"
                            className="form-check-input"
                            checked={selectedKey === key}
                            onChange={() => handleCheckboxChange(key)}
                        />&nbsp;&nbsp;
                        {key}</label>
                </div>
            ))}
            <br /><br />
            <div>
                <label htmlFor="fieldText" className="form-check-label">Field : </label>&nbsp;&nbsp;
                <input type="text" id="fieldText" placeholder="Enter Field Name" />
                <br />
                <button className="btn btn-primary mt-3" onClick={addCheckbox}>Add Field</button>
            </div>

            <br />
        </div>
    )
}

export default CheckboxField