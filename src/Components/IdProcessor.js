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
    const [refImageURL, setRefImageURL] = useState(null);
    const [isGetRef, setIsGetRef] = useState(false)
    const [isKeyInList, setKeyInList] = useState(false)
    let key = ""
    const [keyValue, setValue] = useState(0)
    // eslint-disable-next-line no-unused-vars
    const [mrz, setMrz] = useState("")
    const [getHeight, setHeight] = useState(0)
    const [getWidth, setWidth] = useState(0)
    const [isNoCropClicked, setNoCropClicked] = useState(false)
    const [checker, setChecker] = useState(false)
    // eslint-disable-next-line no-unused-vars
    const [ocrType, setOcrType] = useState(0)
    // eslint-disable-next-line no-unused-vars
    const [field_type, setFieldType] = useState(0)
    // eslint-disable-next-line no-unused-vars
    const [thresholdValue, setThresholdValue] = useState(0.5)
    const defaultRegex = "(.+\\s?){1,}"

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
                setHeight(image.height)
                setWidth(image.width)
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
        setRectangleCoords(null);
        setCardCoordinates(defaultFields);
        setShowConfig(false)
        setChecker(false)
        setNoCropClicked(false)
        key = ""
        setDictKey("")
        clearCanvas()
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
            setConfigFields(config)
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
        setIsSetCropped(false)
        setInfoSaved(false)
        setIsCropped(false)
        setConfigFields(config)
        setShowConfig(false)
        setHeight(0)
        setWidth(0)
        setChecker(false)
        setNoCropClicked(false)
        key = ""
        setDictKey("")
        clearCanvas()
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
            rectStartPosition.current.x,
            rectStartPosition.current.y,
            rectWidth,
            rectHeight
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

        let ocrTypeField = document.getElementById("ocrField")
        let ocrTypeKey = null
        if (ocrTypeField) {
            ocrTypeKey = ocrTypeField.value
        }
        if (!ocrTypeKey) {
            ocrTypeKey = ocr_type
        }
        else if (ocrTypeKey) {
            setOcrType(ocrTypeKey)
        }
        else {
            alert("Unidentified Problem!")
            return
        }
        if (ocrTypeKey) {
            ocr_type = ocrTypeKey
        }

        let fieldTypeElement = document.getElementById("fieldType")
        let fieldTypeKey = null
        if (fieldTypeElement) {
            fieldTypeKey = fieldTypeElement.value
        }
        if (!fieldTypeKey) {
            fieldTypeKey = fieldType
        }
        else if (fieldTypeKey) {
            setFieldType(fieldTypeKey)
        }
        else {
            alert("Unidentified Problem!")
            return
        }
        if (fieldTypeKey) {
            fieldType = fieldTypeKey
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
        if (fieldType === 0) {
            regexKey = defaultRegex
        }

        let mrzField = document.getElementById("mrzField")
        let mrzKey = ""
        if (mrzField) {
            mrzKey = mrzField.value
        }
        if (mrzKey === null) {
            mrzKey = ""
        }
        if (!mrzKey) {
            mrzKey = ""
        }
        else if (typeof mrzKey === "string" && mrzKey.includes(" ")) {
            alert("MRZ value can not have space value!")
        }
        else if (mrzKey) {
            setMrz(mrzKey)
        }
        else {
            alert("Unidentified Problem!")
            return
        }

        if (isKeyInList === false) {
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
                if (regexKey && regexKey !== "") {
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
                    if (mrzKey && mrzKey !== "") {
                        setConfigFields((prevConfig) => ({
                            [dictKey]: {
                                ...prevConfig[dictKey],
                                fields: {
                                    ...prevConfig[dictKey]["fields"],
                                    [counter]: {
                                        ...prevConfig[dictKey]["fields"][counter],
                                        mrz_type: mrzKey
                                    }
                                }
                            }
                        }))
                    }
                }
                else if (mrzKey && mrzKey !== "") {
                    setConfigFields((prevConfig) => ({
                        [dictKey]: {
                            ...prevConfig[dictKey],
                            fields: {
                                ...prevConfig[dictKey]["fields"],
                                [counter]: {
                                    ...prevConfig[dictKey]["fields"][counter],
                                    mrz_type: mrzKey
                                }
                            }
                        }
                    }))
                }
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
                if (regexKey && regexKey !== "") {
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
                    if (mrzKey && mrzKey !== "") {
                        setConfigFields((prevConfig) => ({
                            [dictKey]: {
                                ...prevConfig[dictKey],
                                fields: {
                                    ...prevConfig[dictKey]["fields"],
                                    [counter]: {
                                        ...prevConfig[dictKey]["fields"][counter],
                                        mrz_type: mrzKey
                                    }
                                }
                            }
                        }))
                    }
                }
                else if (mrzKey && mrzKey !== "") {
                    setConfigFields((prevConfig) => ({
                        [dictKey]: {
                            ...prevConfig[dictKey],
                            fields: {
                                ...prevConfig[dictKey]["fields"],
                                [counter]: {
                                    ...prevConfig[dictKey]["fields"][counter],
                                    mrz_type: mrzKey
                                }
                            }
                        }
                    }))
                }
            }


            setCounter(counter + 1)
        }

        else if (isKeyInList === true) {
            if (ocr_type === null) {
                configFields[dictKey]["fields"][keyValue] = {
                    name: selectedKey,
                    type: fieldType,
                    points: {
                        x: x,
                        y: y,
                        h: h,
                        w: w
                    }
                }
                if (regexKey && regexKey !== "") {
                    configFields[dictKey]["fields"][keyValue] = {
                        name: selectedKey,
                        type: fieldType,
                        points: {
                            x: x,
                            y: y,
                            h: h,
                            w: w
                        },
                        regex: regexKey
                    }
                    if (mrzKey && mrzKey !== "") {
                        configFields[dictKey]["fields"][keyValue] = {
                            name: selectedKey,
                            type: fieldType,
                            points: {
                                x: x,
                                y: y,
                                h: h,
                                w: w
                            },
                            regex: regexKey,
                            mrz_type: mrzKey
                        }
                    }
                }
                else if (mrzKey && mrzKey !== "") {
                    configFields[dictKey]["fields"][keyValue] = {
                        name: selectedKey,
                        type: fieldType,
                        points: {
                            x: x,
                            y: y,
                            h: h,
                            w: w
                        },
                        mrz_type: mrzKey
                    }
                }

            }
            else {
                configFields[dictKey]["fields"][keyValue] = {
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

                if (regexKey && regexKey !== "") {
                    configFields[dictKey]["fields"][keyValue] = {
                        name: selectedKey,
                        type: fieldType,
                        points: {
                            x: x,
                            y: y,
                            h: h,
                            w: w
                        },
                        ocr_type: ocr_type,
                        regex: regexKey
                    }
                    if (mrzKey && mrzKey !== "") {
                        configFields[dictKey]["fields"][keyValue] = {
                            name: selectedKey,
                            type: fieldType,
                            points: {
                                x: x,
                                y: y,
                                h: h,
                                w: w
                            },
                            ocr_type: ocr_type,
                            regex: regexKey,
                            mrz_type: mrzKey
                        }
                    }
                }
                if (mrzKey && mrzKey !== "") {
                    configFields[dictKey]["fields"][keyValue] = {
                        name: selectedKey,
                        type: fieldType,
                        points: {
                            x: x,
                            y: y,
                            h: h,
                            w: w
                        },
                        ocr_type: ocr_type,
                        mrz_type: mrzKey
                    }
                }
            }
            closeAll()
        }
        else {
            alert("unidentified error!")
            return
        }
    };

    const closeAll = () => {
        const checkboxIds = [
            "showFieldArea",
            "showRegex",
            "showMrz",
            "showOcr",
            "showFieldType",
            "showThreshold",
        ];

        checkboxIds.forEach((id) => {
            const checkbox = document.getElementById(id);
            if (checkbox) {
                checkbox.checked = false;
            }
        });
    };

    const saveThreshold = () => {
        let thresholdField = document.getElementById("threshold")
        let threshold = null
        if (thresholdField) {
            threshold = thresholdField.value
        }
        if (threshold === null) {
            threshold = 0.5
        }
        if (!threshold) {
            threshold = 0.5
        }
        else if (threshold) {
            setThresholdValue(threshold)
        }
        else {
            alert("Unidentified Problem!")
            return
        }

        let thresholdTemp
        if (Number.isInteger(threshold)) {
            thresholdTemp = parseInt(threshold)
        }
        else {
            thresholdTemp = parseFloat(threshold)
        }

        if (threshold) {
            configFields[dictKey]["threshold"] = thresholdTemp
        }
    }

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
        const rectHeight = y2 - y1;

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
        setIsSetCropped(false)
        if (isNoCropClicked) {
            setIsSetCropped(true)
        }
    };

    const handleSetCropped = () => {
        if (isPhotoUploaded && isCropped) {
            setCurrentPhoto(croppedImageURL)
            setCroppedImageURL(null);

            setConfigFields(config)
            setConfigFields((prevConfig) => ({
                [dictKey]: {
                    ...prevConfig.iso_code
                }
            }))

            config.iso_code.initial.h = initialHeight
            config.iso_code.initial.w = initialWidth

            setIsCropped(true);
            setIsSetCropped(false)
            setIsGetRef(true);
            setShowConfig(true)
            setChecker(true)

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
    function getDictKey() {
        return dictKey
    }

    const handleCheckboxChange = (key) => {
        setSelectedKey(key === selectedKey ? "" : key);
        let dictKey = getDictKey();
        let keys = [];

        if (configFields[dictKey] && configFields[dictKey]["fields"]) {
            keys = Object.keys(configFields[dictKey]["fields"]);
        }
        let values = [];

        for (let i = 0; i < keys.length; i++) {
            values.push(configFields[dictKey]["fields"][keys[i]]["name"]);
        }

        for (let data in values) {
            if (values[data] === key) {
                setKeyInList(true)
                setValue(data)
                break;
            } else {
                setKeyInList(false)
            }
        }
    };

    const handleButtonClick = () => {
        handleCrop();
        setButtonClicked(true);
        handleGetCoordinates();
        setRectangleCoords(null);
        setShowConfig(true);
        setSelectedKey(null);
        setIsGetRef(true)
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
        key = isoNumber + '_' + cardType + '_' + side

        if (clickCounter === 0) {
            setConfigFields((prevConfig) => ({
                [key]: {
                    ...prevConfig.iso_code
                }
            }))
        }

        setDictKey(key);
        setClickCounter(clickCounter + 1);
        setInfoSaved(true)
        setIsSetCropped(true)
        setShowConfig(true)
    }

    const noCropping = () => {
        setIsCropped(true);
        configFields["iso_code"]["initial"]["h"] = getHeight
        configFields["iso_code"]["initial"]["w"] = getWidth
        setNoCropClicked(true)
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
        const rectHeight = y2 - y1;

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

    const changeKey = () => {
        if (clickCounter > 0) {
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
            key = isoNumber + '_' + cardType + '_' + side

            let temp = configFields[dictKey]
            setDictKey(key);

            setConfigFields((prevConfig) => ({
                [key]: {
                    temp
                }
            }))


        }
    }

    return (
        <div className="">
            <div id="" >
                <div id="fileInput">
                    <FileInput
                        handlePhotoChange={handlePhotoChange}
                        fileInputRef={fileInputRef}
                        isPhotoUploaded={isPhotoUploaded}
                        handleClearClick={handleClearClick}
                        currentPhoto={currentPhoto}
                        noCropping={noCropping}
                        checker={checker}
                        isNoCropClicked={isNoCropClicked}
                    ></FileInput>
                </div>
                <br />
                {isCropped && (
                    <div>
                        <InfoSelector
                            saveInfo={saveInfo}
                            dictKey={dictKey}
                            changeKey={changeKey}
                            clickCounter={clickCounter}
                        ></InfoSelector>
                        <br />
                    </div>
                )}
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
                        {isShowConfig && (
                            <div className="rightSide">
                                {isInfoSaved && (
                                    <div>
                                        <CheckboxField
                                            cardCoordinates={cardCoordinates}
                                            selectedKey={selectedKey}
                                            handleCheckboxChange={handleCheckboxChange}
                                            addCheckbox={addCheckbox}
                                            saveThreshold={saveThreshold}
                                        ></CheckboxField>
                                        <br />
                                    </div>
                                )}
                                <ShowConfig
                                    isShowConfig={isShowConfig}
                                    config={configFields}
                                ></ShowConfig>

                            </div>
                        )}

                    </div>
                )}
                <br />
            </div>
        </div>
    );
}
export default IdProcessor;