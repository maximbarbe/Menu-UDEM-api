var leftDiv = document.querySelector(".left");
var rightDiv = document.querySelector(".right");
var buttons = document.querySelectorAll("button");


const changeLeftDivWidth = () => {
    leftDiv.style.width = "75%";
    rightDiv.style.transition = "all 3s !important";
    rightDiv.style.boxShadow = "inset 0 0 0 1000px rgba(0,0,0,.75)";
    for (let i = 0; i<buttons.length; i++) {
        buttons[i].classList.remove("btn");
        buttons[i].classList.remove("disabled");
        buttons[i].style.color = "white";
    }
}
const resetLeftDivWidth = () => {
    rightDiv.style.boxShadow = "none";
    leftDiv.style.width = "50%";
}

const changeRightDivWidth = () => {
    rightDiv.style.width = "75%";
    leftDiv.style.transition = "all 3s !important";
    leftDiv.style.boxShadow = "inset 0 0 0 1000px rgba(0,0,0,.75)";
    for (let i = 0; i<buttons.length; i++) {
        buttons[i].classList.add("btn");
        buttons[i].classList.add("disabled");
        buttons[i].style.fontSize="0.75vw"
    }
}

const resetRightDivWidth = () => {
    for (let i = 0; i<buttons.length; i++) {
        buttons[i].classList.remove("btn");
        buttons[i].classList.remove("disabled");
        buttons[i].style.color = "white";
    }
    leftDiv.style.boxShadow = "none";
    rightDiv.style.width = "50%";
}


