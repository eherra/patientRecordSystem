let prescriptionRotation = 0
rotatePrescriptionArrow = () => {
    prescriptionRotation += 180;
    if (prescriptionRotation === 360) {
        prescriptionRotation = 0;
    }
    document.querySelector(".prescriptionArrow").style.transform = `rotate(${prescriptionRotation}deg)`;
}