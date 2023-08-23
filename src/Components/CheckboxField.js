import React, { useState } from "react";
import "../Styles/IdProcessor.css";

const CheckboxField = (props) => {
    const cardCoordinates = props.cardCoordinates;
    const selectedKey = props.selectedKey;
    const handleCheckboxChange = props.handleCheckboxChange;
    const addCheckbox = props.addCheckbox;
    const [showRegex, setShowRegex] = useState(false);
    const [showMrz, setShowMrz] = useState(false);

    const handleRegexCheckboxChange = (event) => {
        setShowRegex(event.target.checked);
    };

    const handleMrzCheckboxChange = (event) => {
        setShowMrz(event.target.checked);
    };

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
                        {key}
                    </label>
                </div>
            ))}
            <br /><br />
            <div>
                <label htmlFor="fieldText" className="form-check-label">
                    Field :
                </label>&nbsp;&nbsp;
                <input type="text" id="fieldText" placeholder="Enter Field Name" />&nbsp;&nbsp;
                <button className="btn btn-primary mt-1" onClick={addCheckbox}>
                    Add Field
                </button>
            </div>
            <div>
                <br />
                <label className="form-check-label" htmlFor="showRegex">
                    Regex :
                </label>&nbsp;&nbsp;
                <input
                    type="checkbox"
                    id="showRegex"
                    onChange={handleRegexCheckboxChange}
                />
                {showRegex && (
                    <div>
                        <label className="form-check-label" htmlFor="regexField">
                            Enter Regex :
                        </label>&nbsp;&nbsp;
                        <input
                            type="text"
                            id="regexField"
                            required
                            placeholder="Enter Regex"
                        />&nbsp;&nbsp;
                    </div>
                )}

            </div>
            <div>
                <br />
                <label className="form-check-label" htmlFor="showMrz">
                    Mrz :
                </label>&nbsp;&nbsp;
                <input
                    type="checkbox"
                    id="showMrz"
                    onChange={handleMrzCheckboxChange}
                />
                {showMrz && (
                    <div>
                        <label className="form-check-label" htmlFor="mrzField">
                            Enter Mrz Type :
                        </label>&nbsp;&nbsp;
                        <input
                            type="text"
                            id="mrzField"
                            required
                            placeholder="Enter Mrz"
                        />&nbsp;&nbsp;
                    </div>
                )}
            </div>

            <br />
        </div>
    );
};

export default CheckboxField;
