#!/usr/bin/node
exports .incrementAndCall = function(number, theFunction) {
    number++; // Increment the number
    theFunction(number); // Call the given function with the incremented number as argument
};
