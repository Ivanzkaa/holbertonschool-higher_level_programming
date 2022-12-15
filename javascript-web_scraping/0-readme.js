#!/usr/bin/node

const fs = require("fs");
const file_dest = process.argv[2];

fs.readFile(file_dest, "utf8", function (error, data) {
    if (error) {
        console.log(error);
    } else {
        process.stdout.write(data);
    }
});
