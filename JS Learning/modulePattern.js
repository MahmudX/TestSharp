let counter = (function(){
    // Privet Field
    let count = 0;
    function print(message){
        console.log(message + " --- " +
        count);
    }

    // Return an object
    return{
        value : count,
        increament : function(){
            count += 1;
            print("After increament: ");
        },
        reset: function(){
            print("Before Reset: ");
            count = 0;
            print("After Reset: ");
        }
    };
})();

console.log(counter.value);
counter.increament();
counter.increament();
counter.increament();
counter.increament();
counter.increament();
counter.increament();
counter.reset();
