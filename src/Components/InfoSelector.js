import React, { useState } from "react";
import cardNames from "./CardNames";
import "../Styles/IdProcessor.css";

const InfoSelector = (props) => {

    const [isoNumber, setIsoNumber] = useState("");
    const [selectedCardType, setSelectedCardType] = useState("");
    const [selectedSide, setSelectedSide] = useState("");

    const saveInfo = props.saveInfo;
    let dictKey = props.dictKey;

    return (
        <div className="rightSide">
            <h4 style={{ textAlign: "center" }}>Key Generator</h4>
            <div>
                <label htmlFor="isoNumber">Enter Iso Number:</label>&nbsp;&nbsp;
                <input
                    id="isoNumber"
                    name="isoNumber"
                    type="number"
                    placeholder="ISO Number"
                    //value={isoNumber}
                    onChange={(e) => setIsoNumber(e.target.value)}
                    defaultValue="729"
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

                {selectedCardType === "passport" && (
                    <div>
                        <br />
                        <label htmlFor="mrzInput">MRZ : </label>&nbsp;&nbsp;
                        <input type="text" id="mrzInput" required placeholder="Enter MRZ" />
                    </div>
                )}
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
            </button> <h5>Generated Key : {dictKey}</h5>
        </div>
    );
};
export default InfoSelector;