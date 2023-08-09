import React, { useState, useRef } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "../Styles/PhotoUploader.css";

function PhotoUploader() {
    const [currentPhoto, setCurrentPhoto] = useState(null);
    const [isPhotoUploaded, setIsPhotoUploaded] = useState(false);
    const fileInputRef = useRef(null);

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
        fileInputRef.current.value = null;
    };

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
                        <br />
                    </div>
                )}
            </div>
        </div>
    );
}

export default PhotoUploader;
