// Declaration
class Car {
    constructor(make,model,year){
        this.make = make;
        this.model = model;
        this.year = year;
    }
    print(){
        console.log(`${this.make} ${this.model} ${this.year}`);
    }
}
let myCar = new Car('BMW', '751li', 2010);
myCar.print();
class SportsCar extends Car{
    
}