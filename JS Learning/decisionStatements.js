var name = "Hasan";
if (name == "Mahmud") {
    console.log("My name is Mahmud");
}
else{
    console.log("I don't know my name");
}

switch (name) {
    case "Mahmud":
        console.log("My name is Mahmud.");
        break;
    case "Hasan":
        console.log("My name is Hasan.");
        break;
    default:
        console.log("I don't know who the f I am.");
        break;
}

var a = 1;
var b = '1';
var result = (a===b) ? "Equal" : "Not Equal";
console.log(result);