#!/usr/bin/node

const fs = require('fs');
const fileDest = process.argv[2];
const content = process.argv[3];

fs.writeFile(fileDest, content, "utf-8", function (err, data) {
    if (err) {
        console.log(err);
    }
});
