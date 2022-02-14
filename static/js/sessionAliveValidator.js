const sessionEndingTime = new Date("{{sessionEndTime}}").getTime();
const checkLeadingZeroAdding = (num) => {
    return num.toString().length < 2 ? "0" + num : num
}
const sessionTimer = setInterval(() => {
    const timeNow = new Date().getTime();
    const remainingTime = sessionEndingTime - timeNow;
    const second = 1000;
    const minute = second * 60;
    const hour = minute * 60;

    minutesLeft = checkLeadingZeroAdding(Math.trunc((remainingTime % hour) / minute));
    secondsLeft = checkLeadingZeroAdding(Math.trunc((remainingTime % minute) / second));

    if (remainingTime <= 0) {
        document.getElementById("timer").innerHTML = "timeout"
        document.getElementById("session").style.backgroundColor = "#da614e"
    } else {
        document.getElementById("timer").innerHTML = minutesLeft + "min " + secondsLeft + "s"
        document.getElementById("session").style.backgroundColor = "#AFE1AF"
    }
}, 1000);