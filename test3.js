import React, { useState, useRef, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "../Styles/PhotoUploader.css";

function PhotoUploader() {
    const [currentPhoto, setCurrentPhoto] = useState(null);
    const [isPhotoUploaded, setIsPhotoUploaded] = useState(false);
    const [isDrawingMode, setIsDrawingMode] = useState(false);
    const [rectangleCoordinates, setRectangleCoordinates] = useState({
        startX: 0,
        startY: 0,
        endX: 0,
        endY: 0,
    });
    const fileInputRef = useRef(null);
    const canvasRef = useRef(null);

    const handlePhotoChange = (e) => {
        const file = e.target.files[0];

        if (file && file.type.includes("image/") && !isPhotoUploaded) {
            const reader = new FileReader();

            reader.onloadend = () => {
                setCurrentPhoto(reader.result);
                setIsPhotoUploaded(true);
            };

            reader.readAsDataURL(file);
        } else {
            setCurrentPhoto(null);
        }
    };

    const handleClearClick = () => {
        setCurrentPhoto(null);
        setIsPhotoUploaded(false);
        setIsDrawingMode(false);
        setRectangleCoordinates({
            startX: 0,
            startY: 0,
            endX: 0,
            endY: 0,
        });
        fileInputRef.current.value = null;
    };

    const toggleDrawingMode = () => {
        setIsDrawingMode((prev) => !prev);
    };

    const handleCanvasMouseDown = (e) => {
        if (isDrawingMode) {
            const canvas = canvasRef.current;
            const rect = canvas.getBoundingClientRect();
            const startX = e.clientX - rect.left;
            const startY = e.clientY - rect.top;

            setRectangleCoordinates({
                startX,
                startY,
                endX: startX,
                endY: startY,
            });
        }
    };

    const handleCanvasMouseMove = (e) => {
        if (isDrawingMode) {
            const canvas = canvasRef.current;
            const rect = canvas.getBoundingClientRect();
            const endX = e.clientX - rect.left;
            const endY = e.clientY - rect.top;

            setRectangleCoordinates((prev) => ({
                ...prev,
                endX,
                endY,
            }));
        }
    };

    const handleCanvasMouseUp = () => {
        // Add any additional logic you want to perform when the user stops drawing
    };

    const handleSaveClick = () => {
        console.log("Rectangle Coordinates:", rectangleCoordinates);
    };

    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext("2d");

        // Draw the photo on the canvas if it's available
        if (currentPhoto) {
            const img = new Image();
            img.onload = () => {
                ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
            };
            img.src = currentPhoto;
        }

        // Draw the rectangle on the canvas dynamically
        if (isDrawingMode) {
            ctx.strokeStyle = "red";
            ctx.lineWidth = 2;
            ctx.strokeRect(
                rectangleCoordinates.startX,
                rectangleCoordinates.startY,
                rectangleCoordinates.endX - rectangleCoordinates.startX,
                rectangleCoordinates.endY - rectangleCoordinates.startY
            );
        }
    }, [currentPhoto, isDrawingMode, rectangleCoordinates]);

    return (
        <div className="photo-uploader-container container">
            <div className="photo-uploader">
                <input
                    type="file"
                    accept=".png, .jpeg, .jpg"
                    onChange={handlePhotoChange}
                    ref={fileInputRef}
                    disabled={isPhotoUploaded}
                />
                {currentPhoto && (
                    <div className="uploaded-photo">
                        <img src={currentPhoto} alt="Uploaded" />
                        <br />
                        <button className="btn btn-danger" onClick={handleClearClick}>
                            Clear
                        </button>
                        <button
                            className={`btn ${isDrawingMode ? "btn-warning" : "btn-primary"}`}
                            onClick={toggleDrawingMode}
                        >
                            {isDrawingMode ? "Disable Drawing" : "Enable Drawing"}
                        </button>
                        {isDrawingMode && (
                            <button className="btn btn-success" onClick={handleSaveClick}>
                                Save
                            </button>
                        )}
                        <br />
                        <canvas
                            ref={canvasRef}
                            width={currentPhoto.width}
                            height={currentPhoto.height}
                            style={{ border: "1px solid black" }}
                            onMouseDown={handleCanvasMouseDown}
                            onMouseMove={handleCanvasMouseMove}
                            onMouseUp={handleCanvasMouseUp}
                        />
                    </div>
                )}
            </div>
        </div>
    );
}

export default PhotoUploader;
