#!/usr/bin/node
exports.incrementAndCall = function(number, theFunction) {
    number++; // Increment the number
    theFunction(number); 
};
