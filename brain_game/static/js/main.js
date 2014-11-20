/**
 * Created by student on 11/19/14.
 */
//This file will hold main javascript functionality code

function flipCell(){
    console.log(this.getAttribute("id"));
    this.style.transform="rotate(50deg)";
}

function prepareEventHandlers(){
    var pg_elements = document.getElementsByTagName("*");
    for (var i =0; i<pg_elements.length; i++){
        if(pg_elements[i].getAttribute("class") == 'game_cell') {
            pg_elements[i].addEventListener('click', flipCell, false);
        }
    }
}

//
//function flipTyle(){
//    this.style.webkitTransform = "rotate(-2deg)";
//}

function init(){
    prepareEventHandlers();
}