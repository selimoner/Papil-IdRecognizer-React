import React, { useState } from "react";
import cardNames from "./CardNames";
import "../Styles/IdProcessor.css";

const InfoSelector = (props) => {

    // eslint-disable-next-line no-unused-vars
    const [isoNumber, setIsoNumber] = useState("");
    const [selectedCardType, setSelectedCardType] = useState("");
    const [selectedSide, setSelectedSide] = useState("");

    const saveInfo = props.saveInfo;
    let dictKey = props.dictKey;
    const changeKey = props.changeKey
    let clickCounter = props.clickCounter

    return (
        <div className="rightSide">
            <h4 style={{ textAlign: "center" }}>Key Generator</h4>
            <div>
                {dictKey && (
                    <h5>Generated Key : {dictKey}</h5>
                )}
                <br />
                <label htmlFor="isoNumber">Enter Iso Number:</label>&nbsp;&nbsp;
                <input
                    id="isoNumber"
                    name="isoNumber"
                    type="text"
                    placeholder="ISO Number"
                    onChange={(e) => setIsoNumber(e.target.value)}
                />
                &nbsp;&nbsp;&nbsp;&nbsp;
            </div>
            <br />
            <div>
                <label htmlFor="cardType">Select Card Type:</label>&nbsp;&nbsp;
                <select
                    name="cardType"
                    id="cardTypeList"
                    value={selectedCardType}
                    onChange={(e) => setSelectedCardType(e.target.value)}
                    required
                >
                    <option value="">Select card Type</option>
                    {Object.entries(cardNames.cardNames).map((key) => (
                        <option key={key[0]} value={key[1]}>
                            {key[1]}
                        </option>
                    ))}
                </select>
                &nbsp;&nbsp;
            </div>
            <br />
            <div>
                <label htmlFor="side">Select Side:</label>&nbsp;&nbsp;
                <select
                    name="side"
                    id="sideList"
                    value={selectedSide}
                    onChange={(e) => setSelectedSide(e.target.value)}
                    required
                >
                    <option value="">Select side</option>
                    {Object.entries(cardNames.isFront).map((key) => (
                        <option key={key[0]} value={key[1]}>
                            {key[1]}
                        </option>
                    ))}
                </select>
                &nbsp;&nbsp;&nbsp;&nbsp;
            </div>
            <br />
            <button type="button" className="btn btn-primary" onClick={saveInfo}>
                Save
            </button>&nbsp;&nbsp;
            {clickCounter > 0 && (
                <button type="button" className="btn btn-warning" onClick={changeKey}>
                    Change Key
                </button>
            )}

        </div>
    );
};
export default InfoSelector;