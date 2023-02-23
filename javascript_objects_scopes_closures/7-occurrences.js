#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let num_occurences = 0;
    for (let i in list) {
        if (list[i] === searchElement) {
            num_occurences++;
        }
    }
    return num_occurences;
};
