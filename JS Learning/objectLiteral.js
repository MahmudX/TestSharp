let date = Date.now();
let car = {
    make : "BMW",
    model : "Cutlas Suprime",
    year : 1998,
    GetDesc : function(){
        console.log(this.make + " " + this.model);
    },
    GetPrice : function(){
        if (Date().year > 2010) {
            return 5700;
        }
        else{
            return 7500;
        }
    } 
};
let anotherCar = {
    n : {l : "Hi MF"}
};
console.log(anotherCar.n.l);
console.log(date);
car.GetDesc();