var counter = 0;
function timeOut(){
    setTimeout(function(){
        console.log("Hi! " + counter);
        counter ++;
        timeOut();
    }, 2000);
}

// timeOut();

(function(){
    console.log("IIFE");
})();
