#!/usr/bin/node

const fs = require("fs");
const fileDest = process.argv[2];

fs.readFile(fileDest, "utf8", function (error, data) {
    if (error) {
        console.log(error);
    } else {
        process.stdout.write(data);
    }
});
