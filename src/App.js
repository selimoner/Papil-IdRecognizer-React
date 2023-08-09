import React from "react";
import PhotoUploader from "./Components/PhotoUploader";
import Navbar from "./Components/Navbar";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <div className="container">
      <br />
      <Navbar title="Papilon"></Navbar>
      <br />
      <PhotoUploader />
    </div>
  );
}

export default App;
