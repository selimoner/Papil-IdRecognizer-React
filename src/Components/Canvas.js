import React from "react";
import "../Styles/IdProcessor.css"

const Canvas = (props) => {

    const canvasRef = props.canvasRef
    const handleMouseDown = props.handleMouseDown
    const handleMouseMove = props.handleMouseMove
    const handleMouseUp = props.handleMouseUp

    return (
        <div id="canvasDiv">
            <canvas id="canvasElement"
                ref={canvasRef}
                className="mt-7 border"
                onMouseDown={handleMouseDown}
                onMouseMove={handleMouseMove}
                onMouseUp={handleMouseUp}
            />
        </div>
    )
}

export default Canvas