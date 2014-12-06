var PLAYER = 1;
var GUESS = 1;
var MOVES  = 0;


function flipCell(){
    console.log(this.getAttribute("data-cell-pos"));
    this.style.transform="rotateY(180deg)";
    this.setAttribute("data-side", 'flipped');
}

function updateGlobalVariables(){
    if(GUESS === 1){
        GUESS += 1;
    } else {
        GUESS = 1;
        MOVES += 1;
        //reset the last to blocks to unflipped and rotate
    }
}

function handleUserMove(){
    if (this.getAttribute("data-side") === 'unflipped'){
        flipCell.call(this);
        updateGlobalVariables();
        setFields();
        console.log("The current state is: " + this.getAttribute("data-side"));
    } else{
        console.log("You can\'t flip this. It is already in a " + this.getAttribute("data-side") + " state.");
    }
}

function setTime(){
    $('#duration').value(now());
}

function startTimer(){
    var today = new Date();
    var hour = today.getHours();
    var minutes = today.getMinutes();
    var seconds = today.getSeconds();
    var myTime = new Date();
    var mySuper = myTime.getSeconds();
    $('#duration').val(setTimeout(function(){startTimer()}, 1000));
}

function setFields(){
    $('#player').val(PLAYER);
    $("#guess").val(GUESS);
    $("#moves").val(MOVES);
}

function prepareEventHandlers(){
    var pg_elements = document.getElementsByTagName("*");
    for (var i =0; i<pg_elements.length; i++){
        if(pg_elements[i].getAttribute("class") == 'game_cell') {
            pg_elements[i].addEventListener('click', handleUserMove, false);
        }
    }
}

function init(){
    prepareEventHandlers();
    setFields();
    //startTimer();
}