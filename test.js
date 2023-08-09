import React, { useState, useRef } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "../Styles/PhotoUploader.css";

function PhotoUploader() {
    // State tanımlamaları
    const [currentPhoto, setCurrentPhoto] = useState(null); // Yüklü olan fotoğrafın verisini içeren state
    const [isPhotoUploaded, setIsPhotoUploaded] = useState(false); // Fotoğrafın yüklenip yüklenmediğini tutan state
    const fileInputRef = useRef(null); // Dosya seçim input'u için referans oluşturuluyor

    // Fotoğraf seçildiğinde tetiklenen olay
    const handlePhotoChange = (e) => {
        const file = e.target.files[0];

        // Dosyanın bir fotoğraf (png, jpeg, jpg) olup olmadığını kontrol ediyoruz
        if (file && file.type.includes("image/") && !isPhotoUploaded) {
            const reader = new FileReader();

            // Dosya yüklendiğinde bu blok çalışacak
            reader.onloadend = () => {
                setCurrentPhoto(reader.result); // Dosyanın verisini state'e kaydediyoruz
                setIsPhotoUploaded(true); // Fotoğrafın yüklendiğini belirten state'i güncelliyoruz
            };

            reader.readAsDataURL(file); // Dosyanın verisini okuyoruz
        } else {
            // Eğer dosya bir fotoğraf değilse, hiç dosya seçilmemişse veya zaten bir fotoğraf yüklenmişse
            // mevcut fotoğrafı temizliyoruz
            setCurrentPhoto(null);
        }
    };

    // 'Clear' butonuna tıklandığında tetiklenen olay
    const handleClearClick = () => {
        setCurrentPhoto(null); // Mevcut fotoğrafı temizliyoruz
        setIsPhotoUploaded(false); // Fotoğrafın yüklendiğini belirten state'i güncelliyoruz
        fileInputRef.current.value = null; // Dosya seçim input değerini temizliyoruz
    };

    // JSX dönüşü
    return (
        <div className="photo-uploader-container container">
            <div className="photo-uploader">
                {/* Fotoğraf seçim input */}
                <input
                    type="file"
                    accept=".png, .jpeg, .jpg"
                    onChange={handlePhotoChange}
                    ref={fileInputRef}
                    disabled={isPhotoUploaded} // Fotoğraf yüklendiyse dosya seçimi devre dışı bırakılır
                />
                {/* Mevcut fotoğraf varsa, yüklendiği bölüm */}
                {currentPhoto && (
                    <div className="uploaded-photo">
                        <img src={currentPhoto} alt="Uploaded" />
                        <br />
                        {/* Fotoğrafı temizlemek için buton */}
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