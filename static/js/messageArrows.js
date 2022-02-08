let sentRotation = 0
rotateSentArrow = () => {
    sentRotation += 180;
    if (sentRotation === 360) {
        sentRotation = 0;
    }
    document.querySelector(".sentArrow").style.transform = `rotate(${sentRotation}deg)`;
}

let receivedRotation = 0
rotateReceivedArrow = () => {
    receivedRotation += 180;
    if (receivedRotation === 360) {
        receivedRotation = 0;
    }
    document.querySelector(".receivedArrow").style.transform = `rotate(${receivedRotation}deg)`;
}