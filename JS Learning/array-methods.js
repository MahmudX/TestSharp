let names = ['Mahmud', 'Hasan', 'Habiba', 'Mahbuba'];
let others = ['Dragon', 'Minecraft', 'PUBG'];
let lost = [4, 8, 15, 16, 23, 42];
let fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55];

// var combine = lost.concat(fibonacci);
// console.log(combine);
// console.log(fibonacci.join(' ~ '));
/* console.log(lost);
console.log(lost.pop());
console.log(lost);
console.log(lost.shift());
console.log(lost);
console.log(lost);
console.log(lost.push(5, 2));
console.log(lost);
console.log(lost.unshift(5, 2, 3));
console.log(lost); 
console.log(names.reverse());
console.log(names.sort());*/

// Map Arrow
let filtered = fibonacci.filter((x) => {
    if (x > 10) return x
});
console.log(filtered);

names.forEach((x) => {
    console.log(`Hello ${x}`)
});