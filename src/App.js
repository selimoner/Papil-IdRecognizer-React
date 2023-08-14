import React from "react";
import IdProcessor from "./Components/IdProcessor";
import Navbar from "./Components/Navbar";
import "bootstrap/dist/css/bootstrap.min.css";
import "./Styles/App.css"

function App() {
  return (
    <div className="container">
      <br />
      <Navbar title="Papilon"></Navbar>
      <div>
        <IdProcessor></IdProcessor>
      </div>
    </div>
  );
}

export default App;
