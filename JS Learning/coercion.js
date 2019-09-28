// Implimentation of biot savrt law

function GetMF(I, r, dl){
    return Math.pow(10,-7) * ((I*dl*r)/Math.pow(r,3));
}


let result = GetMF(10,2,3);
console.log(result);
