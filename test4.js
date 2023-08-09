import React, { useState, useRef, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "../Styles/PhotoUploader.css";
import ReactCrop from 'react-image-crop'
import 'react-image-crop/dist/ReactCrop.css'

function PhotoUploader() {

    const [currentPhoto, setCurrentPhoto] = useState(null);
    const [isPhotoUploaded, setIsPhotoUploaded] = useState(false);
    const [selectedKey, setSelectedKey] = useState("");
    const [rectangleCoords, setRectangleCoords] = useState(null);
    const [cardCoordinates, setCardCoordinates] = useState({
        card: {
            x1: 0,
            y1: 0,
            x2: 0,
            y2: 0,
        },
        idNumber: {
            x1: 0,
            y1: 0,
            x2: 0,
            y2: 0,
        },
        name: {
            x1: 0,
            y1: 0,
            x2: 0,
            y2: 0,
        },
        surname: {
            x1: 0,
            y1: 0,
            x2: 0,
            y2: 0,
        },
        dateOfBirth: {
            x1: 0,
            y1: 0,
            x2: 0,
            y2: 0,
        },
        documentNo: {
            x1: 0,
            y1: 0,
            x2: 0,
            y2: 0,
        },
        validUntil: {
            x1: 0,
            y1: 0,
            x2: 0,
            y2: 0,
        },
        gender: {
            x1: 0,
            y1: 0,
            x2: 0,
            y2: 0,
        },
        nationality: {
            x1: 0,
            y1: 0,
            x2: 0,
            y2: 0,
        },
        signature: {
            x1: 0,
            y1: 0,
            x2: 0,
            y2: 0,
        },
    });

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
            setCardCoordinates({
                card: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 0,
                },
                idNumber: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 0,
                },
                name: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 0,
                },
                surname: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 0,
                },
                dateOfBirth: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 0,
                },
                documentNo: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 0,
                },
                validUntil: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 0,
                },
                gender: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 0,
                },
                nationality: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 0,
                },
                signature: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 0,
                },
            });
        } else {
            setCurrentPhoto(null);
        }
    };

    const handleClearClick = () => {
        setCurrentPhoto(null);
        setIsPhotoUploaded(false);
        setRectangleCoords(null);
        fileInputRef.current.value = null;
        setCardCoordinates({
            card: {
                x1: 0,
                y1: 0,
                x2: 0,
                y2: 0,
            },
            idNumber: {
                x1: 0,
                y1: 0,
                x2: 0,
                y2: 0,
            },
            name: {
                x1: 0,
                y1: 0,
                x2: 0,
                y2: 0,
            },
            surname: {
                x1: 0,
                y1: 0,
                x2: 0,
                y2: 0,
            },
            dateOfBirth: {
                x1: 0,
                y1: 0,
                x2: 0,
                y2: 0,
            },
            documentNo: {
                x1: 0,
                y1: 0,
                x2: 0,
                y2: 0,
            },
            validUntil: {
                x1: 0,
                y1: 0,
                x2: 0,
                y2: 0,
            },
            gender: {
                x1: 0,
                y1: 0,
                x2: 0,
                y2: 0,
            },
            nationality: {
                x1: 0,
                y1: 0,
                x2: 0,
                y2: 0,
            },
            signature: {
                x1: 0,
                y1: 0,
                x2: 0,
                y2: 0,
            },
        });
    };

    const handleMouseDown = (e) => {
        e.preventDefault();

        if (!isPhotoUploaded) return;

        isDrawing.current = true;
        rectStartPosition.current = {
            x: e.nativeEvent.offsetX,
            y: e.nativeEvent.offsetY,
        };
    };

    const handleMouseMove = (e) => {
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
    };

    const handleGetCoordinates = () => {
        if (rectangleCoords && selectedKey) {
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

    const handleCrop = (currentPhoto) => {

    }

    const handleCheckboxChange = (key) => {
        setSelectedKey(key === selectedKey ? "" : key);
    };

    const handleButtonClick = () => {
        handleGetCoordinates();
        setRectangleCoords(null);
        setShowCoordinates(true);
    };

    return (
        <div className="container">
            <div id="photo-uploader" className="row">
                <div className="col-sm" id="left-side">
                    <input
                        type="file"
                        accept=".png, .jpeg, .jpg"
                        onChange={handlePhotoChange}
                        ref={fileInputRef}
                        disabled={isPhotoUploaded}
                    />
                    {currentPhoto && (
                        <div className="uploaded-photo">
                            {/*<img src={currentPhoto} alt="Uploaded" />*/}

                            <button className="btn btn-danger" onClick={handleClearClick}>
                                Clear
                            </button>
                            <br /><br />
                        </div>
                    )}
                </div>
                {isPhotoUploaded && currentPhoto && (
                    <div className="col-sm" id="right-side">
                        <div>
                            {Object.keys(cardCoordinates).map((key) => (
                                <div key={key} id="form-check" className="col-md-3 mb-2">
                                    <input
                                        type="checkbox"
                                        className="form-check-input"
                                        checked={selectedKey === key}
                                        onChange={() => handleCheckboxChange(key)}
                                    />&nbsp;&nbsp;
                                    <label className="form-check-label">{key}</label>
                                </div>
                            ))}

                        </div>
                        {selectedKey && (
                            <button className="btn btn-primary mt-3" onClick={handleButtonClick}>
                                Get Card Coordinates
                            </button>
                        )}
                        <button className="btn btn-warning mt-3" onClick={handleCrop}>
                            Crop Photo
                        </button>
                        <canvas
                            ref={canvasRef}
                            className="mt-7 border"
                            onMouseDown={handleMouseDown}
                            onMouseMove={handleMouseMove}
                            onMouseUp={handleMouseUp}
                        />

                    </div>
                )}

                {showCoordinates && (
                    <div className="coordinates-section">
                        <h3>Card Coordinates:</h3>
                        <pre>{JSON.stringify(cardCoordinates, null, 2)}</pre>
                    </div>
                )}
            </div>



        </div>
    );
}

export default PhotoUploader;
