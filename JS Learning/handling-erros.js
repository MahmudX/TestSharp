let a = 7 * undefined / "panama";
console.log(a);

function beforeTryCatch() {
    let obj = undefined;
    console.log(obj.b);
    console.log("If previous line throws an ex");
}
// beforeTryCatch();
function afterTryCatch() {
    try {
        let obj = undefined;
        console.log(obj.b);
        console.log("If previous line throws an ex");
    } catch (error) {
        console.log('We catched an error named' + error.message + '.');
    }
}
afterTryCatch();