var leftDiv = document.querySelector(".left");
var rightDiv = document.querySelector(".right");
var buttons = document.querySelectorAll("button");

const changeLeftDivWidth = () => {
    leftDiv.style.width = "75%";
    rightDiv.style.transition = "all 3s !important";
    rightDiv.style.boxShadow = "inset 0 0 0 1000px rgba(0,0,0,.75)";
}
const resetLeftDivWidth = () => {
    rightDiv.style.boxShadow = "none";
    leftDiv.style.width = "50%";
}

const changeRightDivWidth = () => {
    let buttons = document.querySelectorAll("button");
    for (let i = 0; i<buttons.length; i++){
        
        buttons[i].style.opacity = "30%";
    };
    rightDiv.style.width = "75%";
    leftDiv.style.transition = "all 3s !important";
    leftDiv.style.boxShadow = "inset 0 0 0 1000px rgba(0,0,0,.75)";
}

const resetRightDivWidth = () => {
    leftDiv.style.boxShadow = "none";
    rightDiv.style.width = "50%";
}