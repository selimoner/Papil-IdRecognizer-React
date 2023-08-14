import React, { useState, useRef, useEffect } from "react";
import "../Styles/IdProcessor.css"

import FileInput from "./FileInput";
import CheckboxField from "./CheckboxField"
import Canvas from "./Canvas";
import Buttons from "./Buttons";
import CroppedImage from "./CroppedImage";
import ShowCoordinates from "./ShowCoordinates";
import defaultFields from "./CardFields";
import CroppedImagesDiv from "./CroppedImagesDiv";

function PhotoUploader() {

    const croppedImage = new Image();
    const [currentPhoto, setCurrentPhoto] = useState(null);
    const [isPhotoUploaded, setIsPhotoUploaded] = useState(false);
    const [isCropped, setIsCropped] = useState(false);
    const [selectedKey, setSelectedKey] = useState("");
    const [rectangleCoords, setRectangleCoords] = useState(null);
    const [croppedImageURL, setCroppedImageURL] = useState(null);
    const [cardCoordinates, setCardCoordinates] = useState(defaultFields);
    const [isButtonClicked, setButtonClicked] = useState(false);

    const fileInputRef = useRef(null);
    const canvasRef = useRef(null);
    const contextRef = useRef(null);
    const isDrawing = useRef(false);
    const rectStartPosition = useRef({ x: 0, y: 0 });
    const [showCoordinates, setShowCoordinates] = useState(false);

    useEffect(() => {
        let screenWidth = window.screen.availWidth;
        let screenHeight = window.screen.availHeight;
        if (currentPhoto) {
            const canvas = canvasRef.current;
            const context = canvas.getContext("2d");
            const image = new Image();

            image.onload = () => {
                if (image.width > screenWidth && image.height > screenHeight) {
                    image.width = screenWidth - 200;
                    image.height = screenHeight - 200;
                }

                canvas.width = image.width;
                canvas.height = image.height;
                context.drawImage(image, 0, 0, canvas.width, canvas.height);

                contextRef.current = context.getImageData(0, 0, canvas.width, canvas.height);
            };

            image.src = currentPhoto;
        }
    }, [currentPhoto]);

    const handlePhotoChange = (e) => {
        const file = e.target.files[0];

        if (file && file.type.includes("image/") && !isPhotoUploaded) {
            const reader = new FileReader();

            reader.onload = () => {
                setCurrentPhoto(reader.result);
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
        e.preventDefault();

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
        const x1y2 = `x2,y2 (${rectStartPosition.current.x}, ${e.nativeEvent.offsetY})`;
        const x2y1 = `x1,y2 (${e.nativeEvent.offsetX}, ${rectStartPosition.current.y})`;
        const x2y2 = `x2,y1 (${e.nativeEvent.offsetX}, ${e.nativeEvent.offsetY})`;

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


        if (rectangleCoords && selectedKey && handleButtonClick) {
            setCardCoordinates((prevCoordinates) => ({
                ...prevCoordinates,
                [selectedKey]: {
                    ...prevCoordinates[selectedKey],
                    ...rectangleCoords,
                },
            }));
            setRectangleCoords(null);
        }
        console.log("Updated Card Coordinates:", cardCoordinates);
    };

    const clearCanvas = () => {
        const canvas = canvasRef.current;
        const context = canvas.getContext("2d");
        context.clearRect(0, 0, canvas.width, canvas.height);
        context.putImageData(contextRef.current, 0, 0);
    };

    const handleCrop = () => {
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


        const rectWidth = x2 - x1;
        const rectHeight = y2 - y1 + 10;

        const canvas = canvasRef.current;

        const croppedCanvas = document.createElement('canvas');
        const croppedContext = croppedCanvas.getContext('2d');

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

    };

    const handleSetCropped = () => {
        if (isPhotoUploaded && isCropped) {
            setCurrentPhoto(croppedImageURL)
            setCroppedImageURL(null);
            setCardCoordinates(defaultFields)
        }
        else if (!isCropped) {
            alert("You didn't cropped anything!")
        }
        else {
            alert("No photo availible!")
        }
        setIsCropped(false);
    }

    const handleCheckboxChange = (key) => {
        setSelectedKey(key === selectedKey ? "" : key);
    };

    const handleButtonClick = () => {
        handleCrop();
        setButtonClicked(true);
        handleGetCoordinates();
        setRectangleCoords(null);
        setShowCoordinates(true);
        setSelectedKey(null);
        const canvas = canvasRef.current;
        const context = canvas.getContext("2d");
        context.clearRect(0, 0, canvas.width, canvas.height);
        context.putImageData(contextRef.current, 0, 0);
    };

    return (
        <div className="container">
            <div id="photo-uploader" className="row">
                <FileInput
                    handlePhotoChange={handlePhotoChange}
                    fileInputRef={fileInputRef}
                    isPhotoUploaded={isPhotoUploaded}
                    handleClearClick={handleClearClick}
                    currentPhoto={currentPhoto}
                ></FileInput>
                {isPhotoUploaded && currentPhoto && (
                    <div className="col-sm" id="right-side">
                        <CheckboxField
                            cardCoordinates={cardCoordinates}
                            selectedKey={selectedKey}
                            handleCheckboxChange={handleCheckboxChange}
                            addCheckbox={addCheckbox}
                        ></CheckboxField>
                        <br />
                        <Buttons
                            selectedKey={selectedKey}
                            handleButtonClick={handleButtonClick}
                            handleCrop={handleCrop}
                            handleSetCropped={handleSetCropped}
                            isCropped={isCropped}
                        ></Buttons>
                        <br />
                        <div id="drawDiv">
                            <Canvas
                                canvasRef={canvasRef}
                                handleMouseDown={handleMouseDown}
                                handleMouseMove={handleMouseMove}
                                handleMouseUp={handleMouseUp}
                            ></Canvas>
                            <br />

                        </div>
                        <CroppedImage
                            croppedImageURL={croppedImageURL}
                        ></CroppedImage>
                        <br /><br />
                        <ShowCoordinates
                            showCoordinates={showCoordinates}
                            cardCoordinates={cardCoordinates}
                        ></ShowCoordinates>
                        <CroppedImagesDiv
                            selectedKey={selectedKey}
                            croppedImageURL={croppedImageURL}
                            cardCoordinates={cardCoordinates}
                        ></CroppedImagesDiv>
                    </div>
                )}
                <br />
            </div>
        </div >
    );
}

export default PhotoUploader;