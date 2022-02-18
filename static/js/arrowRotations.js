let sentRotationValue = 0
let receivedRotationValue = 0
let allPrescriptionValue = 0
let prescriptionValue = 0

rotateArrow = (arrowClassName) => {
    switch (arrowClassName) {
        case "sentMessageArrow":
            sentRotationValue = makeHtmlDocumentChange(arrowClassName, sentRotationValue)
            break
        case "receivedMessageArrow":
            receivedRotationValue = makeHtmlDocumentChange(arrowClassName, receivedRotationValue)
            break
        case "allPrescriptionArrow":
            allPrescriptionValue = makeHtmlDocumentChange(arrowClassName, allPrescriptionValue)
            if (allPrescriptionValue == 180) {
                document.getElementById("presListText").innerHTML = "Hide"
            } else {
                document.getElementById("presListText").innerHTML = "View"
            }
            break
        case "prescriptionArrow":
            prescriptionValue = makeHtmlDocumentChange(arrowClassName, prescriptionValue)
            break
        default:
            break
    }
}

makeHtmlDocumentChange = (arrowClassName, rotateValue) => {
    newRotationValue = makeRotation(rotateValue)
    document.querySelector(`.${arrowClassName}`).style.transform = `rotate(${newRotationValue}deg)`
    return newRotationValue
}

makeRotation = (rotationValue) => {
    rotationValue += 180;
    if (rotationValue === 360) {
        rotationValue = 0;
    }
    return rotationValue
}