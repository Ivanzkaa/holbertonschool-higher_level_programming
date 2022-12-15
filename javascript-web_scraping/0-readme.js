#!/usr/bin/node

const fp = require("fp");
fp.readFile(process.argv[2], "utf8", function (error, content) {
    console.log(error || content);
});
