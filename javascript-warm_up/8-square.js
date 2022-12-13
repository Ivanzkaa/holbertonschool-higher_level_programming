#!/usr/bin/node

const square_size = Math.floor(Number(process.argv[2]));
if (isNaN(square_size)) {
    console.log("Missing size");
} else {
    for (let i = 0; i < square_size; i++) {
        let row = "";
        for (let b = 0; b < square_size; b++) row += "X";
        console.log(row);
    }
}

