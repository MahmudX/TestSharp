function sayHello(name) {
    return function(){
        console.log("Howdy " + name);
    };    
}
let helloName = sayHello("Mahmud");
helloName();
