function fullName() {
    console.log(this.firstName + " " + this.lastName);
}
let customerOne = {
    firstName: 'Suraia',
    lastName: 'Sharmin',
    print: fullName
};
let customerTwo = {
    firstName: 'Mahmudul',
    lastName: 'Hasan',
    print: fullName
};
let customerThree = {
    firstName: 'Ayesha',
    lastName: 'Siddika',
    print: fullName
};
customerOne.print();