import React, { useState } from "react";
import "../Styles/IdProcessor.css";

const CheckboxField = (props) => {
    const cardCoordinates = props.cardCoordinates;
    const selectedKey = props.selectedKey;
    const handleCheckboxChange = props.handleCheckboxChange;
    const addCheckbox = props.addCheckbox;
    const saveThreshold = props.saveThreshold
    const [showRegex, setShowRegex] = useState(false);
    const [showMrz, setShowMrz] = useState(false);
    const [showOcr, setShowOcr] = useState(false);
    const [showFieldType, setShowFieldType] = useState(false);
    const [showFieldArea, setShowFieldArea] = useState(false)
    const [showThreshold, setShowThreshold] = useState(false)

    const handleRegexCheckboxChange = (event) => {
        setShowRegex(event.target.checked);
    };

    const handleMrzCheckboxChange = (event) => {
        setShowMrz(event.target.checked);
    };
    const handleOcrCheckboxChange = (event) => {
        setShowOcr(event.target.checked);
    };
    const handleFieldTypeCheckboxChange = (event) => {
        setShowFieldType(event.target.checked);
    };
    const handleFieldAreaCheckboxChange = (event) => {
        setShowFieldArea(event.target.checked);
    };
    const handleThresholdChange = (event) => {
        setShowThreshold(event.target.checked);
    };
    const closeArea = () => {
        setShowThreshold(false)
        let checkbox = document.getElementById("showThreshold")
        if (checkbox) {
            checkbox.checked = false;
        }
    }

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
                <br />
                <label className="form-check-label" htmlFor="showFieldArea">
                    Add Field :
                </label>&nbsp;&nbsp;
                <input
                    type="checkbox"
                    id="showFieldArea"
                    onChange={handleFieldAreaCheckboxChange}
                />
                {showFieldArea && (
                    <div>
                        <label htmlFor="fieldText" className="form-check-label">
                            Enter Field :
                        </label>&nbsp;&nbsp;
                        <input type="text" id="fieldText" placeholder="Enter Field Name" />&nbsp;&nbsp;
                        <button className="btn btn-primary" onClick={addCheckbox}>
                            Add Field
                        </button>
                    </div>
                )}

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

            <div>
                <br />
                <label className="form-check-label" htmlFor="showOcr">
                    Ocr :
                </label>&nbsp;&nbsp;
                <input
                    type="checkbox"
                    id="showOcr"
                    onChange={handleOcrCheckboxChange}
                />
                {showOcr && (
                    <div>
                        <label className="form-check-label" htmlFor="ocrField">
                            Enter OCR Type :
                        </label>&nbsp;&nbsp;
                        <input
                            type="number"
                            id="ocrField"
                            required
                            placeholder="Enter Ocr Type"
                        />&nbsp;&nbsp;
                    </div>
                )}
            </div>

            <div>
                <br />
                <label className="form-check-label" htmlFor="showFieldType">
                    Field Type :
                </label>&nbsp;&nbsp;
                <input
                    type="checkbox"
                    id="showFieldType"
                    onChange={handleFieldTypeCheckboxChange}
                />
                {showFieldType && (
                    <div>
                        <label className="form-check-label" htmlFor="fieldType">
                            Enter Field Type :
                        </label>&nbsp;&nbsp;
                        <input
                            type="number"
                            id="fieldType"
                            required
                            placeholder="Enter Field Type"
                        />&nbsp;&nbsp;
                    </div>
                )}
            </div>

            <div>
                <br />
                <label className="form-check-label" htmlFor="showThreshold">
                    Threshold :
                </label>&nbsp;&nbsp;
                <input
                    type="checkbox"
                    id="showThreshold"
                    onChange={handleThresholdChange}
                />
                {showThreshold && (
                    <div>
                        <label className="form-check-label" htmlFor="threshold">
                            Enter Threshold value :
                        </label>&nbsp;&nbsp;
                        <input
                            type="number"
                            id="threshold"
                            required
                            placeholder="Enter Threshold Value"
                        />&nbsp;&nbsp;
                        <button className="btn btn-primary" onClick={() => { saveThreshold(); closeArea(); }}>
                            Save Threshold
                        </button>
                    </div>

                )}
            </div>

            <br />
        </div>
    );
};

export default CheckboxField;
