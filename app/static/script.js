$(document).ready(function () {
    $('input[type=radio][name=alcohol]').change(function() {
        if (document.getElementById('alcohol-0').checked) {
            $('#drinks').show()
        } else {
            $('#drinks').hide()
        }
    });
    $('input[type=checkbox][name=avec]').change(function() {
        if (document.getElementById('avec').checked) {
            $('#avec-info').show();
            $('#avec_consent').prop("checked", false);
        } else {
            $('#avec-info').hide();
            $('#avec_consent').prop("checked", true);
        }
    });
        $('input[type=radio][name=avec_alcohol]').change(function() {
        if (document.getElementById('avec_alcohol-0').checked) {
            $('#avec-drinks').show();
        } else {
            $('#avec-drinks').hide();
        }
    })
});








document.addEventListener('DOMContentLoaded', function(){
var heart1 = document.getElementById("heart1");
var heart2 = document.getElementById("heart2");
var heart3 = document.getElementById("heart3");
var heart4 = document.getElementById("heart4");
var heart5 = document.getElementById("heart5");
var mouse = {x: 0, y: 0}; //mouse.x, mouse.y
document.addEventListener("mousemove", getMouse);


heart1.style.position = "absolute"; //css
heart2.style.position = "absolute"; //css
heart3.style.position = "absolute"; //css
heart4.style.position = "absolute"; //css
heart5.style.position = "absolute"; //css

var heart1pos = {x: 0, y: 0};
var heart2pos = {x: 0, y: 0};
var heart3pos = {x: 0, y: 0};
var heart4pos = {x: 0, y: 0};
var heart5pos = {x: 0, y: 0};

setInterval(followMouse, 50, heart2pos, heart1pos, heart1);
setInterval(followMouse, 50, heart3pos, heart2pos, heart2);
setInterval(followMouse, 50, heart4pos, heart3pos, heart3);
setInterval(followMouse, 50, heart5pos, heart4pos, heart4);
setInterval(followMouse, 50, mouse, heart5pos, heart5);


function getMouse(e) {
    mouse.x = e.pageX -10;
    mouse.y = e.pageY -10;
}

function followMouse(target, beepos, bee) {
    //1. find distance X , distance Y
    var distX = target.x - beepos.x;
    var distY = target.y - beepos.y;
    //Easing motion
    //Progressive reduction of distance
    beepos.x += distX / (3 );
    beepos.y += distY / (3 );

    bee.style.left = beepos.x + "px";
    bee.style.top = beepos.y + "px";


}

    // your code goes here
}, false);

