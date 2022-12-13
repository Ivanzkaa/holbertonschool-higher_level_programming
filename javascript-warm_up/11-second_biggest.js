#!/usr/bin/node

function sortNumber (a, b) {
    return a - b;
}
let arg_len = process.argv.length;
if (arg_len === 2 || arg_len === 3) {
    console.log("0");
} else {
    let a_rray = [];
    for (let i = 2; i < arg_len; i++) {
        a_rray.push(process.argv[i]);
    }
    a_rray.sort(sortNumber);
    console.log(a_rray[a_rray.length - 2]);
}
