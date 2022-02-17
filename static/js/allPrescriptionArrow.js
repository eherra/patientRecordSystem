let allPrescriptionRotation = 0
rotateAllPrescriptionArrow = () => {
    console.log("perkel")
    allPrescriptionRotation += 180;
    if (allPrescriptionRotation === 360) {
        allPrescriptionRotation = 0;
    }
    document.querySelector(".allPrescriptionArrow").style.transform = `rotate(${allPrescriptionRotation}deg)`;
}