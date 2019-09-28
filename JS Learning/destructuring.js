let a, b, c, d, e, f;
let names = ["Hasan", "Mahmud", "Ayeshe", "Siddika", "Habiba"];
[a, b, c, d, e, f] = names;
console.log(f);
let others;
[a, b, ...others] = names;
console.log(others);
let make, model;
({make,model} = {
    make:"BMW",
    model:"875li",
    year:2010,
    price:5000
})
//[{make,model}]=car;
console.log(make);