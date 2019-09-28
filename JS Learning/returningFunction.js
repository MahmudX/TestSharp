var counter = 0;
function two(){
    return function(){
        console.log("Hello!");
    };
}
console.log("First: ");
two();
console.log("Second: ");
two()();
console.log("Third: ");
let func = two();
func();
