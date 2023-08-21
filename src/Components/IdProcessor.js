import React, { useState, useRef, useEffect } from "react";
import "../Styles/IdProcessor.css"
import FileInput from "./FileInput";
import CheckboxField from "./CheckboxField"
import Canvas from "./Canvas";
import Buttons from "./Buttons";
import CroppedImage from "./CroppedImage";
import defaultFields from "./CardFields";
import InfoSelector from "./InfoSelector";
import ShowConfig from "./ShowConfig";
import ocr_type_template from "../OcrTemplate";
import config from "./Config.json"

function IdProcessor() {

    const croppedImage = new Image();
    const refImage = new Image();
    const [currentPhoto, setCurrentPhoto] = useState(null);
    const [isPhotoUploaded, setIsPhotoUploaded] = useState(false);
    const [isCropped, setIsCropped] = useState(false);
    const [selectedKey, setSelectedKey] = useState("");
    const [rectangleCoords, setRectangleCoords] = useState(null);
    const [croppedImageURL, setCroppedImageURL] = useState(null);
    const [cardCoordinates, setCardCoordinates] = useState(defaultFields);
    const [isButtonClicked, setButtonClicked] = useState(false);
    const [firstPhoto, setFirstPhoto] = useState(null);
    const [isInfoSaved, setInfoSaved] = useState(false);
    const [dictKey, setDictKey] = useState("");
    const [initialHeight, setInitialHeight] = useState(0);
    const [initialWidth, setInitialWidth] = useState(0);
    const [configFields, setConfigFields] = useState(config)
    const [clickCounter, setClickCounter] = useState(0)
    const [isSetCropped, setIsSetCropped] = useState(false)
    const fileInputRef = useRef(null);
    const canvasRef = useRef(null);
    const contextRef = useRef(null);
    const isDrawing = useRef(false);
    const rectStartPosition = useRef({ x: 0, y: 0 });
    const [isShowConfig, setShowConfig] = useState(false);
    // eslint-disable-next-line no-unused-vars
    const [refX, setRefX] = useState(0)
    // eslint-disable-next-line no-unused-vars
    const [refY, setRefY] = useState(0)
    // eslint-disable-next-line no-unused-vars
    const [refHeight, setRefHeight] = useState(0)
    // eslint-disable-next-line no-unused-vars
    const [refWidth, setRefWidth] = useState(0)
    const [counter, setCounter] = useState(0)
    // eslint-disable-next-line no-unused-vars
    const [regex, setRegex] = useState("")
    // eslint-disable-next-line no-unused-vars
    const [existingNames, setExistingNames] = useState({})
    // eslint-disable-next-line no-unused-vars
    const [refImageURL, setRefImageURL] = useState(null);
    const [isGetRef, setIsGetRef] = useState(false)

    useEffect(() => {
        let screenWidth = window.screen.availWidth;
        let screenHeight = window.screen.availHeight;
        if (currentPhoto) {
            const canvas = canvasRef.current;
            const context = canvas.getContext("2d");
            canvas.willReadFrequently = true;
            const image = new Image();
            const image2 = new Image();

            image.onload = () => {
                if (image.width > screenWidth && image.height > screenHeight) {
                    image.width = screenWidth - 200;
                    image.height = screenHeight - 200;
                }

                canvas.width = image.width;
                canvas.height = image.height;
                context.drawImage(image, 0, 0, canvas.width, canvas.height);
                contextRef.current = context.getImageData(0, 0, canvas.width, canvas.height);
                canvas.willReadFrequently = true;
            };
            image2.src = currentPhoto;
            image.src = currentPhoto;
        }

    }, [currentPhoto]);

    const goBack = () => {
        setCroppedImageURL(null);
        setCurrentPhoto(firstPhoto);
        setSelectedKey(null)
        setIsCropped(false)
        setConfigFields(config)
    }

    const handlePhotoChange = (e) => {
        const file = e.target.files[0];

        if (file && file.type.includes("image/") && !isPhotoUploaded) {
            const reader = new FileReader();

            reader.onload = () => {
                setCurrentPhoto(reader.result);
                setFirstPhoto(reader.result)
                setIsPhotoUploaded(true);
            };

            reader.readAsDataURL(file);
            setSelectedKey(null);
            setCardCoordinates(defaultFields);
        } else {
            setCurrentPhoto(null);
        }
    };

    const handleClearClick = () => {
        setCurrentPhoto(null);
        setIsPhotoUploaded(false);
        setRectangleCoords(null);
        fileInputRef.current.value = null;
        setCardCoordinates(defaultFields);
    };

    const handleMouseDown = (e) => {
        setButtonClicked(false);
        if (!isPhotoUploaded) return;
        isDrawing.current = true;
        rectStartPosition.current = {
            x: e.nativeEvent.offsetX,
            y: e.nativeEvent.offsetY,
        };
    };

    const handleMouseMove = (e) => {
        setButtonClicked(false)
        if (!isDrawing.current) return;

        const canvas = canvasRef.current;
        const context = canvas.getContext("2d");
        canvas.willReadFrequently = true;

        context.putImageData(contextRef.current, 0, 0);

        context.strokeStyle = "red";
        context.fillStyle = "red";
        context.lineWidth = 2;

        const rectWidth = e.nativeEvent.offsetX - rectStartPosition.current.x;
        const rectHeight = e.nativeEvent.offsetY - rectStartPosition.current.y;

        context.strokeRect(
            rectStartPosition.current.x + 5,
            rectStartPosition.current.y + 5,
            rectWidth - 10,
            rectHeight + 5
        );

        setRectangleCoords({
            x1: rectStartPosition.current.x,
            y1: rectStartPosition.current.y,
            x2: e.nativeEvent.offsetX,
            y2: e.nativeEvent.offsetY,
        });
        const x1y1 = `x1,y1 (${rectStartPosition.current.x}, ${rectStartPosition.current.y})`;
        const x1y2 = `x1,y2 (${rectStartPosition.current.x}, ${e.nativeEvent.offsetY})`;
        const x2y1 = `x2,y1 (${e.nativeEvent.offsetX}, ${rectStartPosition.current.y})`;
        const x2y2 = `x2,y2 (${e.nativeEvent.offsetX}, ${e.nativeEvent.offsetY})`;

        context.fillText(x1y1, rectStartPosition.current.x, rectStartPosition.current.y);
        context.fillText(x1y2, rectStartPosition.current.x, e.nativeEvent.offsetY);
        context.fillText(x2y1, e.nativeEvent.offsetX, rectStartPosition.current.y);
        context.fillText(x2y2, e.nativeEvent.offsetX, e.nativeEvent.offsetY);

    };

    const handleMouseUp = () => {
        isDrawing.current = false;
        setButtonClicked(false)
        if (rectangleCoords && selectedKey && handleButtonClick && isButtonClicked) {
            setCardCoordinates((prevCoordinates) => ({
                ...prevCoordinates,
                [selectedKey]: {
                    ...prevCoordinates[selectedKey],
                    ...rectangleCoords,
                },
            }));
            setRectangleCoords(null);
        }
    };

    const addCheckbox = () => {
        let fieldName = document.getElementById('fieldText').value;
        if (fieldName && !fieldName.includes(" ")) {
            setCardCoordinates((prevCoordinates) => ({
                ...prevCoordinates,
                [fieldName]: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 0,
                },
            }));
            clearCanvas();
            setSelectedKey(null);
        }
        else {
            alert("Your input can't be empty or have space value!")
        }
    }

    const handleGetCoordinates = () => {
        if (!rectangleCoords) return;

        let { x1, y1, x2, y2 } = rectangleCoords;
        if (x2 < x1) {
            let temp = x1;
            x1 = x2;
            x2 = temp;
        }
        if (y2 < y1) {
            let temp2 = y1;
            y1 = y2;
            y2 = temp2;
        }
        rectangleCoords.x1 = x1;
        rectangleCoords.x2 = x2;
        rectangleCoords.y1 = y1;
        rectangleCoords.y2 = y2;

        let x = x1
        let y = y1
        let h = y2 - y1
        let w = x2 - x1

        let ocr_type = null
        let ocr_type_zero = ocr_type_template[0]
        let ocrt_type_one = ocr_type_template[1]
        for (let i = 0; i < ocr_type_zero.length; i++) {
            if (ocr_type_zero[i] === selectedKey.toLowerCase()) {
                ocr_type = 0;
            }
        }

        for (let i = 0; i < ocrt_type_one; i++) {
            if (ocrt_type_one[i] === selectedKey.toLowerCase()) {
                ocr_type = 1;
            }
        }

        if (ocrt_type_one.includes(selectedKey)) {
            ocr_type = 1
        }
        let fieldName = selectedKey.toLowerCase()
        let fieldType = 0;

        if (!fieldName === "mrz" && !fieldName === "signature" && !fieldName === "image") {
            fieldType = 0
        }
        else if (fieldName === "image" || fieldName === "photo" || fieldName === "facial_image") {
            fieldType = 1
        }
        else if (fieldName === "mrz" || fieldName === "mrzfield" || fieldName === "mrz_field") {
            fieldType = 2
        }
        else if (fieldName === "signature" || fieldName === "sign" || fieldName === "imza") {
            fieldType = 3
        }

        setConfigFields((prevConfig) => ({
            [dictKey]: {
                ...prevConfig[dictKey]

            }
        }))

        if (rectangleCoords && selectedKey && handleButtonClick) {
            /*setConfigFields((prevConfig) => ({
                [dictKey]: {
                    ...prevConfig[dictKey],
                    fields: {
                        ...prevConfig[dictKey],
                        [counter]: {
                            name: selectedKey,
                            type: fieldType,
                            points: {
                                x: x,
                                y: y,
                                h: h,
                                w: w
                            }
                        }
                    }
                }
            }))*/

            if (!(selectedKey in existingNames)) {
                if (ocr_type === null) {
                    setConfigFields((prevConfig) => ({
                        [dictKey]: {
                            ...prevConfig[dictKey],
                            fields: {
                                ...prevConfig[dictKey]["fields"],
                                [counter]: {
                                    name: selectedKey,
                                    type: fieldType,
                                    points: {
                                        x: x,
                                        y: y,
                                        h: h,
                                        w: w
                                    },
                                }
                            }
                        }
                    }))
                    setCounter(counter + 1)
                }
                else {
                    setConfigFields((prevConfig) => ({
                        [dictKey]: {
                            ...prevConfig[dictKey],
                            fields: {
                                ...prevConfig[dictKey]["fields"],
                                [counter]: {
                                    name: selectedKey,
                                    type: fieldType,
                                    points: {
                                        x: x,
                                        y: y,
                                        h: h,
                                        w: w
                                    },
                                    ocr_type: ocr_type
                                }
                            }
                        }
                    }))
                    setCounter(counter + 1)
                }
            }

            else if (selectedKey in existingNames) {
                if (ocr_type === null) {
                    setConfigFields((prevConfig) => ({
                        [dictKey]: {
                            ...prevConfig[dictKey],
                            fields: {
                                ...prevConfig[dictKey]["fields"],
                                [counter]: {
                                    name: selectedKey,
                                    type: fieldType,
                                    points: {
                                        x: x,
                                        y: y,
                                        h: h,
                                        w: w
                                    },
                                }
                            }
                        }
                    }))
                    setCounter(counter + 1)
                }
                else {
                    setConfigFields((prevConfig) => ({
                        [dictKey]: {
                            ...prevConfig[dictKey],
                            fields: {
                                ...prevConfig[dictKey]["fields"],
                                [counter]: {
                                    name: selectedKey,
                                    type: fieldType,
                                    points: {
                                        x: x,
                                        y: y,
                                        h: h,
                                        w: w
                                    },
                                    ocr_type: ocr_type
                                }
                            }
                        }
                    }))
                    setCounter(counter + 1)
                }
            }
            else {
                alert("unidentified error!")
                return
            }

            let regexField = document.getElementById("regexField")
            let regexKey = ""
            if (regexField) {
                regexKey = regexField.value
            }
            if (regexKey === null) {
                regexKey = ""
            }
            if (!regexKey) {
                regexKey = ""
            }
            else if (typeof regexKey === "string" && regexKey.includes(" ")) {
                alert("Regex value can not have space value!")
            }
            else if (regexKey) {
                setRegex(regexKey)
            }
            else {
                alert("Unidentified Problem!")
                return
            }

            if (regexKey) {
                setConfigFields((prevConfig) => ({
                    [dictKey]: {
                        ...prevConfig[dictKey],
                        fields: {
                            ...prevConfig[dictKey]["fields"],
                            [counter]: {
                                ...prevConfig[dictKey]["fields"][counter],
                                regex: regexKey
                            }
                        }
                    }
                }))
            }
        }
    };

    const clearCanvas = () => {
        const canvas = canvasRef.current;
        const context = canvas.getContext("2d");
        canvas.willReadFrequently = true;
        context.clearRect(0, 0, canvas.width, canvas.height);
        context.putImageData(contextRef.current, 0, 0);
        setRectangleCoords(null);
    };

    const handleCrop = () => {
        if (!rectangleCoords) {
            alert("You didn't draw anything on the image!")
            return;
        };
        let { x1, y1, x2, y2 } = rectangleCoords;
        if (x2 < x1) {
            let temp = x1;
            x1 = x2;
            x2 = temp;
        }
        if (y2 < y1) {
            let temp2 = y1;
            y1 = y2;
            y2 = temp2;
        }
        let h = y2 - y1
        let w = x2 - x1
        setInitialHeight(h);
        setInitialWidth(w);

        const rectWidth = x2 - x1;
        const rectHeight = y2 - y1 + 10;

        const canvas = canvasRef.current;

        const croppedCanvas = document.createElement('canvas');
        const croppedContext = croppedCanvas.getContext('2d');
        canvas.willReadFrequently = true;

        croppedCanvas.width = rectWidth;
        croppedCanvas.height = rectHeight;
        const clearContext = canvas.getContext("2d");
        clearContext.clearRect(0, 0, canvas.width, canvas.height);
        clearContext.putImageData(contextRef.current, 0, 0);

        croppedContext.drawImage(
            canvas,
            x1, y1, rectWidth, rectHeight,
            0, 0, rectWidth, rectHeight
        );

        const croppedImageURL = croppedCanvas.toDataURL();

        croppedImage.src = croppedImageURL;

        setCroppedImageURL(croppedImageURL);
        setIsCropped(true);
        clearCanvas();
        setRectangleCoords(null);
        setIsSetCropped(true)
    };

    const handleSetCropped = () => {
        if (isPhotoUploaded && isCropped) {
            setCurrentPhoto(croppedImageURL)
            setCroppedImageURL(null);

            setConfigFields(config)

            config.iso_code.initial.h = initialHeight
            config.iso_code.initial.w = initialWidth

            setIsCropped(true);
            setIsSetCropped(false)
            setIsGetRef(true);

            var dataurl = croppedImageURL

            var a = document.createElement("a");
            a.href = dataurl;
            a.download = dictKey + "_initial.png";
            a.click();
        }
        else if (!isCropped) {
            alert("You didn't cropped anything!")
        }
        else {
            alert("No photo availible!")
        }
    }

    const handleCheckboxChange = (key) => {
        setSelectedKey(key === selectedKey ? "" : key);
    };

    const handleButtonClick = () => {
        handleCrop();
        setButtonClicked(true);
        handleGetCoordinates();
        setRectangleCoords(null);
        setShowConfig(true);
        setSelectedKey(null);
        const canvas = canvasRef.current;
        const context = canvas.getContext("2d");
        context.clearRect(0, 0, canvas.width, canvas.height);
        context.putImageData(contextRef.current, 0, 0);
    };

    const saveInfo = () => {
        let isoNumber = document.getElementById("isoNumber").value;
        let cardType = document.getElementById("cardTypeList").value;
        let side = document.getElementById("sideList").value;

        if (!isoNumber) {
            alert("You didn't put any iso number!")
            setInfoSaved(false)
            setSelectedKey(null)
            return

        }
        else if (!cardType) {
            alert("You didn't select any card type!")
            setInfoSaved(false)
            setSelectedKey(null)
            return
        }
        else if (!side) {
            alert("You didn't select any side!")
            setInfoSaved(false)
            setSelectedKey(null)
            return
        }
        if (cardType === "passport") {
            let mrzField = document.getElementById("mrzInput").value;
            if (!mrzField) {
                alert("Please fill the MRZ Field!");
                setInfoSaved(false);
                setSelectedKey(null);
            }
        }
        let key = isoNumber + '_' + cardType + '_' + side

        setDictKey(key);
        if (clickCounter === 0) {
            setConfigFields((prevConfig) => ({
                [key]: {
                    ...prevConfig.iso_code
                }
            }))
        }
        setClickCounter(clickCounter + 1);
        setInfoSaved(true)
    }

    const noCropping = () => {
        setIsCropped(true);
        setIsSetCropped(true)
    }

    const getRef = () => {
        if (!rectangleCoords) {
            alert("You didn't draw anything on the image!")
            return;
        }
        let { x1, y1, x2, y2 } = rectangleCoords;
        if (x2 < x1) {
            let temp = x1;
            x1 = x2;
            x2 = temp;
        }
        if (y2 < y1) {
            let temp2 = y1;
            y1 = y2;
            y2 = temp2;
        }
        let x = x1
        let y = y1
        let h = y2 - y1
        let w = x2 - x1
        setRefX(x)
        setRefY(y)
        setRefHeight(h)
        setRefWidth(w)
        config.iso_code.ref.h = h
        config.iso_code.ref.w = w
        config.iso_code.ref.x = x
        config.iso_code.ref.y = y


        const rectWidth = x2 - x1;
        const rectHeight = y2 - y1 + 10;

        const canvas = canvasRef.current;

        const croppedCanvas = document.createElement('canvas');
        const croppedContext = croppedCanvas.getContext('2d');
        canvas.willReadFrequently = true;

        croppedCanvas.width = rectWidth;
        croppedCanvas.height = rectHeight;
        const clearContext = canvas.getContext("2d");
        clearContext.clearRect(0, 0, canvas.width, canvas.height);
        clearContext.putImageData(contextRef.current, 0, 0);

        croppedContext.drawImage(
            canvas,
            x1, y1, rectWidth, rectHeight,
            0, 0, rectWidth, rectHeight
        );

        const refImageURL = croppedCanvas.toDataURL();

        refImage.src = refImageURL;

        setRefImageURL(refImageURL);

        var a = document.createElement("a");
        a.href = refImageURL;
        a.download = dictKey + ".png";
        a.click();

        clearCanvas()
    }

    return (
        <div className="container">
            <div id="photo-uploader" >
                <div id="fileInput">
                    <FileInput
                        handlePhotoChange={handlePhotoChange}
                        fileInputRef={fileInputRef}
                        isPhotoUploaded={isPhotoUploaded}
                        handleClearClick={handleClearClick}
                        currentPhoto={currentPhoto}
                        noCropping={noCropping}
                    ></FileInput>
                </div>
                <br />
                {isPhotoUploaded && currentPhoto && (
                    <div className="col-sm" id="right-side">

                        <div id="drawDiv">
                            <Canvas
                                canvasRef={canvasRef}
                                handleMouseDown={handleMouseDown}
                                handleMouseMove={handleMouseMove}
                                handleMouseUp={handleMouseUp}
                            ></Canvas>
                            <br />
                        </div>
                        <Buttons
                            selectedKey={selectedKey}
                            handleButtonClick={handleButtonClick}
                            handleCrop={handleCrop}
                            handleSetCropped={handleSetCropped}
                            isCropped={isCropped}
                            goBack={goBack}
                            clearCanvas={clearCanvas}
                            getRef={getRef}
                            isSetCropped={isSetCropped}
                            isInfoSaved={isInfoSaved}
                            isGetRef={isGetRef}
                        ></Buttons>
                        <br />
                        <div className="rightSide">
                            <CroppedImage
                                croppedImageURL={croppedImageURL}
                                selectedKey={selectedKey}
                            ></CroppedImage>
                            <br />
                        </div>
                        {isCropped && (
                            <div>
                                <InfoSelector
                                    saveInfo={saveInfo}
                                    dictKey={dictKey}
                                ></InfoSelector>
                                <br />
                            </div>
                        )}
                        <div className="rightSide">
                            <ShowConfig
                                isShowConfig={isShowConfig}
                                config={configFields}
                            ></ShowConfig>
                            {isInfoSaved && (
                                <div>
                                    <CheckboxField
                                        cardCoordinates={cardCoordinates}
                                        selectedKey={selectedKey}
                                        handleCheckboxChange={handleCheckboxChange}
                                        addCheckbox={addCheckbox}
                                    ></CheckboxField>
                                    <br />
                                </div>
                            )}
                        </div>
                    </div>
                )}
                <br />
            </div>
        </div>
    );
}
export default IdProcessor;